# Eval 006 — Interrupción del WIP por un bug

## User request

> Apareció un bug crítico en autenticación. Registralo, interrumpí el bloque actual y prepará el trabajo urgente sin perder el punto de retorno.

## Context

- `F02-004` está WIP.
- El bug pertenece a la fase de implementación vigente.
- El problema afecta un hito comprometido.

## Expected behavior

- Crear un ítem `bug` con prioridad, criterios y evidencia esperada.
- No crear una fase exclusiva para el incidente.
- Conservar en WIP el punto exacto de retorno de `F02-004` y dejar su estado coherente.
- Inicializar el bloque urgente y registrar la interrupción en bitácora.
- Actualizar roadmap por el impacto sobre el hito.

## Success criteria

Bug, bloque interrumpido, fuente de estado, historia e impacto quedan sincronizados sin autorizar la corrección funcional.
