# Eval 005 — Ambiguous dashboard request

## Scenario

La palabra “dashboard” no permite saber si falta definir contenido analítico o diseñar su experiencia. El eval prueba clarificación mínima y routing conjunto.

## User request

> Necesito un dashboard para este módulo.

## Expected activation

Condicional. `dashboard-ux` debe intervenir si existen audiencia, decisiones y métricas suficientes. Si falta el contrato analítico, debe pedir definición previa o activar `product-analytics`; si el pedido es mixto, debe proponer la secuencia analytics → dashboard UX.

## Context

- No se describe el módulo.
- No se conoce la audiencia ni la decisión.
- No se sabe si existen métricas, definiciones o comparaciones.
- El término dashboard podría referirse a estrategia métrica, UX o implementación.

## Expected characteristics

- Hacer una clarificación breve centrada en audiencia/decisión y existencia de métricas acordadas.
- Explicar routing condicional sin iniciar trabajo innecesario.
- Si el contrato existe, solicitarlo y continuar con estructura e interacción.
- Si falta, derivar a `product-analytics` antes de diseñar.
- Si solo se pide código o apariencia, derivar a la capacidad correspondiente.
- Permitir supuestos mínimos únicamente después de conocer la intención principal.

## Required concepts

- audience and decision;
- metric contract gate;
- conditional activation;
- semantic handoff;
- mixed-request sequencing;
- scope boundary.

## Forbidden / undesirable behavior

- Asumir que “dashboard” significa automáticamente UI.
- Asumir que necesita automáticamente una nueva lista de KPIs.
- Diseñar una grilla, sidebar, cards o charts antes de aclarar intención.
- Ejecutar a la vez analytics, UX y frontend sin autorización ni inputs.
- Formular un cuestionario exhaustivo cuando una o dos preguntas discriminantes bastan.
- Inventar audiencia, métricas o modo como hechos.

## Success criteria

1. La respuesta distingue analytics, dashboard UX e implementación.
2. Las preguntas pueden cambiar materialmente el routing.
3. `dashboard-ux` solo avanza si existe contenido semántico suficiente.
4. La secuencia mixta conserva un handoff explícito.
5. No se producen KPIs, layout ni código prematuramente.
