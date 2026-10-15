#!/usr/bin/env python3
"""Validate the deterministic structure of a roadmap-backlog directory."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


VALID_STATES = {"Pending", "Ready", "WIP", "Blocked", "Done", "Cancelled"}
REQUIRED_FILES = ("roadmap.md", "wip.md", "bitacora.md", "parking-lot.md")
ITEM_RE = re.compile(r"\bF\d{2,}-\d{3,}\b")
PHASE_RE = re.compile(r"\bF\d{2,}\b")
INITIATIVE_RE = re.compile(r"\bINI-\d{3,}\b")
PARKING_RE = re.compile(r"\bPL-\d{3,}\b")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ITEM_HEADING_RE = re.compile(r"^##\s+(F\d{2,}-\d{3,})\s+[—-]", re.MULTILINE)
INITIATIVE_HEADING_RE = re.compile(r"^#\s+(INI-\d{3,})\s+[—-]", re.MULTILINE)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: Path
    message: str
    line: int | None = None


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def read_markdown(path: Path, findings: list[Finding]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        findings.append(Finding("ERROR", "read-failed", path, str(exc)))
        return ""


def iter_table_rows(text: str):
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells and not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            yield number, cells


def check_links(root: Path, path: Path, text: str, findings: list[Finding]) -> None:
    for match in LINK_RE.finditer(text):
        raw_target = match.group(1).strip().split()[0].strip("<>")
        if not raw_target or raw_target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(raw_target.split("#", 1)[0])
        if re.match(r"^[A-Za-z]:[\\/]", target) or target.startswith(("/", "\\")):
            findings.append(
                Finding("ERROR", "absolute-link", path, f"El enlace debe ser relativo: {raw_target}", line_number(text, match.start()))
            )
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            findings.append(
                Finding("ERROR", "broken-link", path, f"No existe el destino: {raw_target}", line_number(text, match.start()))
            )


def item_blocks(text: str):
    matches = list(ITEM_HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        yield match.group(1), match.start(), text[match.start():end]


def check_item_block(path: Path, item_id: str, offset: int, block: str, findings: list[Finding]) -> None:
    state_match = re.search(r"^- \*\*Estado:\*\*\s*([^\n]+)", block, re.MULTILINE)
    if not state_match:
        findings.append(Finding("ERROR", "missing-state", path, f"{item_id} no declara Estado.", line_number(block, 0) + line_number(path.read_text(encoding='utf-8'), offset) - 1))
        return
    state = state_match.group(1).strip().strip("`")
    if state not in VALID_STATES:
        findings.append(Finding("ERROR", "invalid-state", path, f"{item_id} usa estado inválido: {state}", line_number(path.read_text(encoding='utf-8'), offset + state_match.start())))

    evidence_match = re.search(r"^### Evidencia de finalización\s*$([\s\S]*?)(?=^### |^## |\Z)", block, re.MULTILINE)
    evidence = evidence_match.group(1).strip() if evidence_match else ""
    if state == "Done" and (not evidence or re.search(r"\b(pendiente|ninguna|sin evidencia)\b", evidence, re.IGNORECASE)):
        findings.append(Finding("ERROR", "done-without-evidence", path, f"{item_id} está Done sin evidencia utilizable.", line_number(path.read_text(encoding='utf-8'), offset)))
    if state == "Cancelled" and not re.search(r"\b(motivo|cancelad|retirad)\b", block, re.IGNORECASE):
        findings.append(Finding("WARNING", "cancelled-without-reason", path, f"{item_id} está Cancelled sin motivo reconocible.", line_number(path.read_text(encoding='utf-8'), offset)))


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not root.is_dir():
        return [Finding("ERROR", "missing-root", root, "La ruta de roadmap no existe o no es un directorio.")]

    for name in REQUIRED_FILES:
        path = root / name
        if not path.is_file():
            findings.append(Finding("ERROR", "missing-required-file", path, f"Falta {name}."))

    backlog_dir = root / "backlog"
    backlog_files = sorted(backlog_dir.glob("backlog-fase-*.md")) if backlog_dir.is_dir() else []
    if not backlog_files:
        findings.append(Finding("ERROR", "missing-backlogs", backlog_dir, "Debe existir un backlog por fase."))

    markdown_files = sorted(root.rglob("*.md"))
    texts = {path: read_markdown(path, findings) for path in markdown_files}
    for path, text in texts.items():
        check_links(root, path, text, findings)

    canonical_items: dict[str, Path] = {}
    for path in backlog_files:
        text = texts.get(path, "")
        detail_states: dict[str, str] = {}
        phase_match = re.search(r"^- \*\*ID de fase:\*\*\s*(F\d{2,})\s*$", text, re.MULTILINE)
        suffix_match = re.search(r"backlog-fase-(\d{2,})\.md$", path.name)
        if not phase_match:
            findings.append(Finding("ERROR", "missing-phase-id", path, "El backlog no declara ID de fase."))
        elif suffix_match and phase_match.group(1) != f"F{suffix_match.group(1)}":
            findings.append(Finding("ERROR", "phase-file-mismatch", path, f"{phase_match.group(1)} no coincide con el nombre del archivo."))

        headings = list(ITEM_HEADING_RE.finditer(text))
        for match in headings:
            item_id = match.group(1)
            if item_id in canonical_items:
                findings.append(Finding("ERROR", "duplicate-item-id", path, f"{item_id} también se define en {canonical_items[item_id].relative_to(root)}.", line_number(text, match.start())))
            else:
                canonical_items[item_id] = path
        for item_id, offset, block in item_blocks(text):
            check_item_block(path, item_id, offset, block, findings)
            state_match = re.search(r"^- \*\*Estado:\*\*\s*([^\n]+)", block, re.MULTILINE)
            if state_match:
                detail_states[item_id] = state_match.group(1).strip().strip("`")

        table_ids = set()
        table_states: dict[str, str] = {}
        header: list[str] | None = None
        for number, cells in iter_table_rows(text):
            if "ID" in cells and "Estado" in cells:
                header = cells
                continue
            if header and len(cells) == len(header):
                row = dict(zip(header, cells))
                item_id = row.get("ID", "")
                if ITEM_RE.fullmatch(item_id):
                    if item_id in table_ids:
                        findings.append(Finding("ERROR", "duplicate-summary-item", path, f"{item_id} aparece más de una vez en la tabla resumen.", number))
                    table_ids.add(item_id)
                    state = row.get("Estado", "")
                    table_states[item_id] = state
                    if state not in VALID_STATES:
                        findings.append(Finding("ERROR", "invalid-table-state", path, f"{item_id} usa estado inválido en la tabla: {state}", number))
        for item_id in sorted(table_ids - set(ITEM_HEADING_RE.findall(text))):
            findings.append(Finding("ERROR", "summary-without-detail", path, f"{item_id} aparece en el resumen sin definición detallada."))
        for item_id in sorted(table_ids & set(detail_states)):
            if table_states[item_id] != detail_states[item_id]:
                findings.append(Finding("ERROR", "state-mismatch", path, f"{item_id} tiene estado {table_states[item_id]} en el resumen y {detail_states[item_id]} en el detalle."))

    roadmap_path = root / "roadmap.md"
    if roadmap_path in texts:
        linked_backlogs = {
            Path(unquote(target.split("#", 1)[0])).name
            for target in LINK_RE.findall(texts[roadmap_path])
            if "backlog-fase-" in target
        }
        actual_backlogs = {path.name for path in backlog_files}
        for name in sorted(actual_backlogs - linked_backlogs):
            findings.append(Finding("ERROR", "unlinked-backlog", roadmap_path, f"El roadmap no enlaza {name}."))

    wip_path = root / "wip.md"
    if wip_path in texts:
        for item_id in sorted(set(ITEM_RE.findall(texts[wip_path])) - set(canonical_items)):
            findings.append(Finding("ERROR", "unknown-wip-item", wip_path, f"WIP referencia un ítem inexistente: {item_id}."))

    initiative_defs: dict[str, Path] = {}
    for path in sorted((root / "iniciativas").glob("*.md")) if (root / "iniciativas").is_dir() else []:
        for match in INITIATIVE_HEADING_RE.finditer(texts.get(path, "")):
            initiative_id = match.group(1)
            if initiative_id in initiative_defs:
                findings.append(Finding("ERROR", "duplicate-initiative-id", path, f"{initiative_id} también se define en {initiative_defs[initiative_id].relative_to(root)}."))
            else:
                initiative_defs[initiative_id] = path

    parking_path = root / "parking-lot.md"
    seen_parking: set[str] = set()
    if parking_path in texts:
        for number, cells in iter_table_rows(texts[parking_path]):
            if cells and PARKING_RE.fullmatch(cells[0]):
                if cells[0] in seen_parking:
                    findings.append(Finding("ERROR", "duplicate-parking-id", parking_path, f"ID duplicado: {cells[0]}", number))
                seen_parking.add(cells[0])

    for path, text in texts.items():
        if path.parent.name == "backlog":
            continue
        for item_id in sorted(set(ITEM_RE.findall(text)) - set(canonical_items)):
            findings.append(Finding("ERROR", "unknown-item-reference", path, f"Referencia a ítem inexistente: {item_id}."))
        for initiative_id in sorted(set(INITIATIVE_RE.findall(text)) - set(initiative_defs)):
            findings.append(Finding("ERROR", "unknown-initiative-reference", path, f"Referencia a iniciativa inexistente: {initiative_id}."))
        for parking_id in sorted(set(PARKING_RE.findall(text)) - seen_parking):
            findings.append(Finding("ERROR", "unknown-parking-reference", path, f"Referencia de parking lot inexistente: {parking_id}."))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida estructura, IDs, estados, enlaces y referencias de roadmap-backlog.")
    parser.add_argument("roadmap", nargs="?", default="roadmap", type=Path, help="Ruta al directorio roadmap/.")
    parser.add_argument("--strict", action="store_true", help="Trata advertencias como error de salida.")
    args = parser.parse_args()

    root = args.roadmap.resolve()
    findings = validate(root)
    for finding in findings:
        location = str(finding.path)
        if finding.line is not None:
            location += f":{finding.line}"
        print(f"{finding.severity} [{finding.code}] {location}: {finding.message}")

    errors = sum(f.severity == "ERROR" for f in findings)
    warnings = sum(f.severity == "WARNING" for f in findings)
    print(f"Resumen: {errors} error(es), {warnings} advertencia(s).")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
