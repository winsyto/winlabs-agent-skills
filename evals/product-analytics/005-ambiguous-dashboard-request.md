# Eval 005 — Ambiguous dashboard request

## Scenario

La palabra “dashboard” no permite saber si el problema es definir qué medir o representar métricas ya acordadas. El eval prueba clarificación y routing condicional.

## User request

> Necesito un dashboard para este módulo.

## Expected activation

Condicional. `product-analytics` debe intervenir primero si objetivo, audiencia decisora y métricas no están definidos. Debe derivarse a `dashboard-ux` si el usuario ya tiene un contrato métrico y necesita layout, interacción o visualización.

## Context

- No se aporta información sobre el módulo.
- No se conoce la audiencia, decisión, objetivo ni estado de las métricas.
- La solicitud admite al menos dos intenciones materialmente diferentes.

## Expected characteristics

- Hacer una clarificación breve centrada en qué decisión debe apoyar y si las métricas ya están definidas.
- Explicar el routing sin imponer trabajo innecesario.
- Si faltan métricas, comenzar por objetivo, actor y decisión usando `product-analytics`.
- Si existen métricas acordadas, solicitar el inventario o contrato y derivar a `dashboard-ux`.
- En una solicitud mixta, proponer secuencia analytics → handoff semántico → dashboard UX.

## Required concepts

- decision to support;
- audience o actor;
- conditional activation;
- semantic handoff;
- scope boundary.

## Forbidden / undesirable behavior

- Asumir automáticamente que “dashboard” significa UI.
- Asumir automáticamente que requiere una nueva lista de KPIs.
- Recomendar layout, charts o herramientas antes de aclarar la intención.
- Responder con una lista genérica de métricas del módulo.
- Bloquear con un cuestionario extenso cuando una o dos preguntas discriminantes bastan.

## Success criteria

1. La respuesta distingue las dos intenciones posibles.
2. Las preguntas de clarificación cambian materialmente el routing.
3. `product-analytics` solo se activa para definir contenido semántico.
4. `dashboard-ux` recibe un handoff cuando el problema pasa a representación.
5. No se invade implementación frontend, SQL o tracking.
