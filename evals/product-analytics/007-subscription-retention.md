# Eval 007 — Subscription retention

## Scenario

Un SaaS por suscripción observa cancelaciones, pero no sabe si el problema es comercial, de adopción o de valor recurrente. El caso debe separar outcomes de producto y negocio.

## User request

> Vendemos un SaaS de planificación con suscripción mensual por cuenta. Queremos entender y mejorar la retención: qué métricas deberíamos usar para distinguir churn comercial, falta de engagement y pérdida de valor del producto.

## Expected activation

Sí. `product-analytics` debe activarse porque se requiere definir retención, churn, engagement y su relación con outcomes de producto y negocio.

## Context

- La cuenta es la unidad contractual; varios usuarios pueden entrar o salir de una cuenta activa.
- Algunas cuentas usan el producto semanalmente y otras solo durante ciclos mensuales de planificación.
- Existen upgrades, downgrades, cancelaciones y reactivaciones.
- La fecha de alta y el plan están disponibles.
- No existe una definición acordada de cuenta “engaged” ni un target de retención.

## Expected characteristics

- Separar retención contractual, revenue retention, continuidad de uso valioso y retención de usuarios.
- Elegir la cuenta como unidad principal de suscripción sin perder diagnósticos a nivel usuario.
- Definir churn y reactivación conceptualmente, con población y ventanas.
- Proponer engagement basado en acciones de valor y ritmo mensual, no en actividad diaria genérica.
- Usar cohortes con ancla y madurez comparables.
- Distinguir outcomes de negocio de drivers de producto.
- Incorporar guardrails o diagnósticos para expansión que oculte pérdida de cuentas o segmentos.
- Marcar targets y relaciones predictivas como pendientes de evidencia.

## Required concepts

- account retention;
- churn;
- revenue vs product outcome;
- value-based engagement;
- cohorts;
- anchor and maturity;
- drivers;
- guardrails;
- comparison context.

## Forbidden / undesirable behavior

- Confundir usuarios activos con cuentas retenidas.
- Definir churn sin población elegible ni período.
- Usar DAU como requisito para un producto de ritmo mensual.
- Tratar revenue retention como prueba suficiente de valor para todas las cuentas.
- Comparar cohortes con distinta madurez.
- Inventar un benchmark o target de churn.
- Recomendar eventos, SQL, herramientas, dashboards o gráficos.

## Success criteria

1. Retención de cuenta, revenue, usuario y comportamiento valioso responden preguntas distintas.
2. Churn, engagement y cohortes tienen unidad, ancla y ventana coherentes.
3. La jerarquía conecta drivers de producto con outcomes de negocio sin confundirlos.
4. Las comparaciones y gaps permiten investigar causas antes de actuar.
5. No se fuerza una North Star ni una frecuencia de uso inapropiada.
