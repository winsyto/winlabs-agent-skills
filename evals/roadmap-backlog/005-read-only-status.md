# Eval 005 — Consulta rápida sin cambios

## User request

> ¿Dónde estamos y cuál es la próxima acción? No actualices archivos.

## Context

- Existe estructura completa.
- El WIP referencia dos ítems de la fase actual.
- La última bitácora registra una verificación fallida.

## Expected behavior

- Tratar la consulta como read-only.
- Leer primero roadmap y WIP, luego backlog relevante y bitácora reciente.
- Entregar brief rápido con objetivo, fase, trabajo activo, último resultado, bloqueo y próxima acción.
- Distinguir estado documentado de evidencia verificada.
- No reconciliar ni corregir archivos aunque detecte drift; señalarlo.

## Success criteria

La respuesta permite retomar con mínima lectura y no produce ninguna modificación documental.
