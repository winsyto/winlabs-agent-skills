# Eval 003 — Feature adoption

## Scenario

Un producto existente lanzó una feature colaborativa y necesita distinguir descubrimiento, adopción, engagement y resultado.

## User request

> Lanzamos comentarios con menciones en nuestro editor. ¿Cómo medimos si la feature fue adoptada y realmente mejora la colaboración?

## Expected activation

Sí. `product-analytics` debe activarse porque la solicitud requiere definir adopción, engagement y outcomes de una feature.

## Context

- Producto B2B con cuentas y equipos.
- La feature está habilitada solo para algunos planes durante el rollout.
- Usuarios pueden leer comentarios sin crear uno.
- El objetivo no es maximizar comentarios, sino resolver coordinación dentro del documento.
- No hay baseline de “mejor colaboración”.

## Expected characteristics

- Definir población elegible y exposición antes de calcular adopción.
- Distinguir discovery, first meaningful use, adoption, repeat engagement y outcome.
- Considerar adopción a nivel usuario y cuenta sin mezclarlas.
- Cuestionar “cantidad de comentarios” como outcome y proponer señales de valor más cercanas al objetivo.
- Incluir cohorts por momento de exposición si ayudan a interpretar retención de uso.
- Incorporar guardrails como ruido, menciones ignoradas o efectos adversos pertinentes.
- Explicar qué decisiones habilitarían distintos patrones sin afirmar causalidad.

## Required concepts

- eligible population;
- adoption;
- engagement frequency, depth o breadth cuando corresponda;
- cohort y repeat behavior;
- outcome vs activity;
- guardrails;
- comparación contra baseline o grupos comparables.

## Forbidden / undesirable behavior

- Usar todos los usuarios como denominador cuando no todos son elegibles.
- Definir adopción únicamente como click o apertura.
- Equiparar más comentarios con mejor colaboración.
- Inventar un porcentaje objetivo.
- Diseñar eventos, queries, dashboards, layout o gráficos.
- Concluir que la feature causó mejoras solo por correlación.

## Success criteria

1. La respuesta separa claramente exposición, adopción, engagement y outcome.
2. Las unidades usuario y cuenta están justificadas.
3. Cada métrica principal incluye comparación y “So what?”.
4. Al menos un guardrail protege contra optimizar volumen sin valor.
5. Se explicitan las limitaciones para demostrar mejora de colaboración.
