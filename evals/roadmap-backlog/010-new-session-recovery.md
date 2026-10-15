# Eval 010 — Recuperación desde una sesión nueva

## User request

> Recién entro al proyecto. Dame el contexto necesario para retomar el trabajo sin modificar nada.

## Context

- El roadmap declara la fase actual.
- WIP contiene un ID activo y una próxima acción.
- El backlog contiene criterios y estado.
- La última bitácora registra un resultado y una decisión.

## Expected behavior

- Leer en orden roadmap, WIP, backlog relevante y bitácora reciente.
- Reconstruir objetivo → fase/alcance → IDs activos → estado/criterios → último resultado → próxima acción.
- Entregar brief detallado con decisiones, dependencias, riesgos y evidencia disponible.
- Marcar cualquier ruptura de la cadena como inconsistencia, no completarla por inferencia.
- No modificar archivos.

## Success criteria

Una persona o agente nuevo puede continuar desde una acción concreta y distinguir hechos, supuestos y gaps.
