# Eval 007 — Cierre de bloque y preparación del siguiente

## User request

> Cerrá el bloque actual: un ítem terminó y otro quedó pendiente. Prepará el siguiente bloque de trabajo.

## Context

- Un ítem cumple criterios y tiene evidencia.
- El segundo conserva una verificación pendiente.
- Existe un ítem Ready de mayor prioridad para continuar.

## Expected behavior

- Marcar `Done` solo el ítem con evidencia.
- Mantener o devolver el incompleto al estado defendible y conservar el pendiente.
- Transferir decisiones duraderas y registrar el cierre en bitácora.
- Actualizar avance y resumen del roadmap.
- Reemplazar WIP solo después de esos pasos e iniciar el próximo ítem Ready.

## Success criteria

El cierre no oculta remanentes, el backlog gobierna estados y el nuevo WIP contiene contexto y próxima acción exacta.
