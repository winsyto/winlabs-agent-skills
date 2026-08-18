# Eval 004 — Negative UI request

## Scenario

La solicitud es puramente visual y de implementación. Contiene la palabra “dashboard”, pero no pide definir métricas.

## User request

> Rediseñá este dashboard en React: quiero las cuatro KPI cards arriba, un gráfico de líneas debajo, modo oscuro y mejor comportamiento responsive. Conservá exactamente las métricas actuales.

## Expected activation

No. `product-analytics` no debe activarse. La solicitud corresponde a dashboard UX y/o implementación frontend.

## Context

- Las métricas ya están definidas y deben conservarse.
- El usuario solicita layout, componentes, visual styling y responsive behavior.
- No hay pedido de revisar relevancia, definición o interpretación de métricas.

## Expected characteristics

- Reconocer que `product-analytics` no es la capacidad apropiada.
- Derivar la parte visual a `dashboard-ux` cuando esté operativa y la implementación a una capacidad frontend.
- No abrir una discusión de KPIs no solicitada.

## Required concepts

- non-activation;
- boundary con dashboard UX;
- boundary con implementación.

## Forbidden / undesirable behavior

- Proponer una North Star, jerarquía o lista nueva de KPIs.
- Redefinir métricas que el usuario pidió conservar.
- Dar recomendaciones de product analytics como condición para realizar el trabajo visual.
- Afirmar que `product-analytics` implementa React, CSS, charts o responsive design.

## Success criteria

1. La skill no se aplica al contenido de la solicitud.
2. El routing distingue diseño UX de implementación frontend.
3. No se introduce alcance analítico no pedido.
