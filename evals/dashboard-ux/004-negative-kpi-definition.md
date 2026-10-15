# Eval 004 — Negative KPI definition

## Scenario

La solicitud menciona KPIs pero no pide representación, estructura o interacción. El eval verifica que `dashboard-ux` no invada la responsabilidad analítica.

## User request

> Necesito definir cuáles son los KPIs correctos para mi SaaS.

## Expected activation

No. `dashboard-ux` no debe activarse como capacidad principal. Debe derivar la definición de KPIs a `product-analytics` y reservarse para un handoff posterior si se solicita un dashboard.

## Context

- No existen métricas acordadas.
- No se aporta objetivo, actor, mecanismo de valor ni decisión.
- No se solicita layout, jerarquía visual, navegación, interacción o estados.

## Expected characteristics

- Reconocer que el problema es definir qué medir.
- Derivar a `product-analytics` de forma breve y clara.
- Explicar opcionalmente qué contrato podría recibir después `dashboard-ux`.
- Evitar ampliar la solicitud hacia diseño visual no pedido.
- Hacer preguntas analíticas solo si actúa `product-analytics`, no fingir que son inputs de UX suficientes.

## Required concepts

- non-activation;
- responsibility boundary;
- `product-analytics` routing;
- semantic handoff.

## Forbidden / undesirable behavior

- Proponer KPIs, North Star, funnel, retention o guardrails.
- Diseñar cards, secciones, charts o filtros.
- Elegir un dashboard mode sin métricas ni tarea de representación.
- Recomendar herramientas, SQL, tracking o frontend.
- Bloquear con un cuestionario de UX irrelevante.

## Success criteria

1. La respuesta no usa `dashboard-ux` para seleccionar métricas.
2. `product-analytics` queda identificado como siguiente capacidad apropiada.
3. No aparecen recomendaciones visuales o de implementación.
4. El posible handoff se describe sin inventar contenido analítico.
