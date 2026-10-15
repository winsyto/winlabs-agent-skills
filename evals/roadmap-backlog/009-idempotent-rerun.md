# Eval 009 — Nueva ejecución sin duplicados

## User request

> Volvé a aplicar la migración anterior después de incorporar una nota nueva.

## Context

- La estructura canónica ya existe.
- Las fases, ítems y el evento original de migración ya fueron registrados.
- Solo una nota agrega evidencia a un ítem existente.

## Expected behavior

- Buscar por ID e identidad semántica antes de crear.
- Actualizar el ítem existente con la evidencia nueva.
- No duplicar fases, ítems, decisiones ni entradas de bitácora.
- Mantener la misma fuente vigente y registrar solo el cambio material nuevo.
- Ejecutar nuevamente controles de coherencia.

## Success criteria

La segunda ejecución converge sobre la estructura existente y el diff contiene únicamente la evidencia nueva y sus consecuencias reales.
