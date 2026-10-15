"""Behavioral checks for roadmap-backlog's optional validator."""

from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR_PATH = REPO_ROOT / ".agents" / "skills" / "roadmap-backlog" / "scripts" / "validate_roadmap.py"
TEMPLATES = REPO_ROOT / ".agents" / "skills" / "roadmap-backlog" / "assets" / "templates"
SPEC = importlib.util.spec_from_file_location("validate_roadmap", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_valid(root: Path) -> None:
    write(
        root / "roadmap.md",
        "# Roadmap\n\n| ID | Fase | Backlog |\n| --- | --- | --- |\n"
        "| F00 | Preparación | [Backlog](backlog/backlog-fase-00.md) |\n\n"
        "- [WIP](wip.md)\n- [Bitácora](bitacora.md)\n- [Parking](parking-lot.md)\n",
    )
    write(
        root / "wip.md",
        "# WIP\n\n- **Estado del bloque:** Activo\n- **Ítems involucrados:** F00-001\n",
    )
    write(root / "bitacora.md", "# Bitácora\n\n## 2026-10-15\n\n- **Ítems:** F00-001\n")
    write(
        root / "parking-lot.md",
        "# Parking lot\n\n| ID | Descripción | Motivo | Condición | Iniciativa |\n"
        "| --- | --- | --- | --- | --- |\n",
    )
    write(
        root / "backlog" / "backlog-fase-00.md",
        "# F00 — Preparación\n\n- **ID de fase:** F00\n\n"
        "| ID | Título | Tipo | Prioridad | Estado | Alcance |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        "| F00-001 | Definir contrato | research | 1 | Ready | MVP |\n\n"
        "## F00-001 — Definir contrato\n\n"
        "- **Descripción:** Definir el contrato verificable.\n"
        "- **Tipo:** research\n- **Prioridad:** 1\n- **Estado:** Ready\n- **Alcance:** MVP\n"
        "- **Dependencias:** ninguna\n\n### Criterios de aceptación\n\n- [ ] Contrato revisado.\n\n"
        "### Evidencia de finalización\n\n- Pendiente hasta completar.\n",
    )


class ValidatorTests(unittest.TestCase):
    def test_materialized_templates_validate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "roadmap"
            (root / "backlog").mkdir(parents=True)
            for name in ("roadmap.md", "wip.md", "bitacora.md", "parking-lot.md"):
                shutil.copyfile(TEMPLATES / name, root / name)
            backlog_template = (TEMPLATES / "backlog-fase.md").read_text(encoding="utf-8")
            for number in ("00", "01"):
                write(root / "backlog" / f"backlog-fase-{number}.md", backlog_template.replace("FXX", f"F{number}"))
            self.assertEqual([], VALIDATOR.validate(root))

    def test_valid_roadmap_has_no_findings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "roadmap"
            build_valid(root)
            self.assertEqual([], VALIDATOR.validate(root))

    def test_detects_structural_and_reference_errors(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "roadmap"
            build_valid(root)
            (root / "wip.md").unlink()
            backlog = root / "backlog" / "backlog-fase-00.md"
            backlog.write_text(backlog.read_text(encoding="utf-8").replace("Ready", "Started"), encoding="utf-8")
            (root / "roadmap.md").write_text(
                (root / "roadmap.md").read_text(encoding="utf-8") + "\n[Rotura](missing.md)\n",
                encoding="utf-8",
            )
            codes = {finding.code for finding in VALIDATOR.validate(root)}
            self.assertTrue({"missing-required-file", "broken-link", "invalid-state", "invalid-table-state"} <= codes)

    def test_detects_cross_document_inconsistency(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "roadmap"
            build_valid(root)
            backlog = root / "backlog" / "backlog-fase-00.md"
            backlog.write_text(backlog.read_text(encoding="utf-8").replace("| Ready |", "| WIP |", 1), encoding="utf-8")
            wip = root / "wip.md"
            wip.write_text(wip.read_text(encoding="utf-8") + "\n- INI-999\n- PL-999\n", encoding="utf-8")
            codes = {finding.code for finding in VALIDATOR.validate(root)}
            self.assertTrue({"state-mismatch", "unknown-initiative-reference", "unknown-parking-reference"} <= codes)


if __name__ == "__main__":
    unittest.main()
