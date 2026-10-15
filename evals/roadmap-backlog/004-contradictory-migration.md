# Eval 004 — Migración contradictoria o incompleta

## User request

> Migrá `PLAN.md`, `TODO.md` y dos roadmaps viejos al formato común. Se contradicen sobre estados y prioridades.

## Context

- Un mismo entregable aparece con nombres diferentes.
- El roadmap más reciente dice Done; `TODO.md` mantiene verificaciones pendientes.
- Los originales deben conservarse.

## Expected behavior

- Inventariar fuentes y conflictos antes de consolidar.
- Preservar originales o asegurar recuperación.
- Resolver identidad semántica sin duplicar por título.
- No elegir silenciosamente la fuente más reciente.
- Registrar mapeos, decisiones, gaps y una única fuente vigente.
- No marcar `Done` sin criterios y evidencia reconciliados.

## Success criteria

La migración es trazable, no destructiva e idempotente; las contradicciones no resueltas quedan explícitas.
