# Eval 001 — Executive dashboard

## Scenario

Una empresa B2B ya acordó su sistema de medición y necesita convertirlo en una vista mensual para dirección. El caso prueba síntesis, prioridad y comparison context sin transformar el dashboard en una consola operativa.

## User request

> Diseñá la estructura de un dashboard mensual para CEO y COO. Las métricas ya están definidas; necesito saber qué va primero, qué queda como contexto y hasta dónde permitir drill-down.

## Expected activation

Sí. `dashboard-ux` debe activarse porque el contenido analítico existe y la solicitud trata jerarquía, estructura y exploración.

## Context

- Audiencia: CEO y COO; revisión conjunta mensual de 30 minutos.
- Decisiones: reasignar inversión entre onboarding y customer success, priorizar riesgos y decidir qué investigar.
- Outcome principal: proporción de cuentas que completan su workflow de valor y renuevan.
- Drivers definidos: activación de cuentas, tiempo hasta primer valor y adopción sostenida.
- Guardrails definidos: retrabajo, tickets críticos y concentración del uso en una sola persona.
- Comparaciones acordadas: target trimestral y mismo período del año anterior.
- Freshness: cierre del mes anterior; no requiere tiempo real.
- Detail disponible: segmento, plan y cohorte; el ejecutivo no gestiona cuentas individuales.

## Expected characteristics

- Identificar un modo ejecutivo y explicar cómo afecta síntesis, densidad y profundidad.
- Priorizar outcome, variación material, target y guardrails críticos sobre drivers secundarios.
- Mantener visible el período, comparison anchor y freshness.
- Separar overview, contexto explicativo y detail bajo demanda.
- Limitar el drill-down a preguntas que puedan cambiar una decisión ejecutiva.
- Explicar qué información debe permanecer secundaria o derivarse a otra vista.
- Incluir estados relevantes sin convertirlos en implementación.
- Proponer requisitos responsive y de accesibilidad proporcionales.

## Required concepts

- audience and decisions;
- executive dashboard mode;
- primary versus secondary content;
- comparison context;
- overview versus detail;
- limited drill-down;
- freshness;
- guardrail prominence;
- assumptions and gaps.

## Forbidden / undesirable behavior

- Redefinir KPIs, targets, denominadores o estrategia de retención.
- Devolver una grilla genérica de cards con igual prominencia.
- Mostrar detalle operativo o una lista de cuentas en la vista inicial.
- Prescribir cantidades universales de KPIs, charts o colores.
- Recomendar tiempo real, SQL, tracking, librerías o React/CSS.
- Usar wireframe ASCII si no aclara una relación relevante.
- Ocultar comparison anchor, período o freshness en tooltips.

## Success criteria

1. La jerarquía se justifica por las decisiones y riesgos de la audiencia.
2. El overview permite entender situación, comparación y puntos de atención rápidamente.
3. El detail está disponible pero no domina ni desorienta.
4. Drivers y guardrails aportan contexto sin competir todos como titulares.
5. La propuesta conserva el contrato analítico y no invade implementación.
