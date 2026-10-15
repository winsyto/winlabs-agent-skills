# Eval 003 — Overloaded dashboard

## Scenario

Un dashboard existente contiene demasiados elementos con igual peso. El caso prueba reducción y reorganización sin borrar información crítica ni sustituir análisis por preferencias estéticas.

## User request

> Este dashboard tiene 18 KPIs, 9 gráficos, una tabla y 14 filtros. Todo parece igual de importante y cuesta entenderlo. Reorganizalo sin perder la información que realmente necesitamos.

## Expected activation

Sí. `dashboard-ux` debe activarse porque la solicitud es una auditoría de jerarquía, densidad, agrupación y progressive disclosure sobre contenido existente.

## Context

- Audiencia principal: product managers en revisión semanal.
- Decisiones: detectar deterioros, elegir un problema para investigar y seguir una intervención activa.
- El contrato analítico identifica tres outcomes, cinco drivers, cuatro guardrails y diagnósticos por plan, cohorte, región y canal.
- Dos guardrails son críticos aunque se consultan poco.
- Siete filtros exponen dimensiones internas que rara vez cambian una decisión.
- La tabla de cuentas es necesaria para investigación, no para la revisión inicial.
- Algunas métricas duplican el mismo fenómeno con ventanas diferentes.
- No hay evidencia de qué elementos utiliza actualmente el equipo.

## Expected characteristics

- Inventariar propósito, decisión y rol de cada grupo antes de eliminar contenido.
- Distinguir duplicación, prioridad baja y detail legítimo.
- Proponer una jerarquía primaria, secundaria y bajo demanda.
- Mantener guardrails críticos visibles o inequívocamente accesibles.
- Reducir filtros iniciales a los que cambian decisiones frecuentes y conservar diagnósticos en detail.
- Separar revisión semanal de investigación por cuenta cuando corresponda.
- Explicitar qué decisiones requieren validación con uso real o stakeholders.
- Conservar comparison context, unidades, freshness y filtros activos.
- Evitar llenar espacios liberados por simetría.

## Required concepts

- content audit;
- decision-oriented prioritization;
- grouping;
- progressive disclosure;
- overview versus detail;
- critical guardrails;
- filter prioritization;
- evidence gaps;
- density and scanability.

## Forbidden / undesirable behavior

- Eliminar automáticamente todo excepto tres métricas.
- Aplicar un número máximo universal de cards o charts.
- Mover información crítica a hover o esconderla por estética.
- Tratar todos los guardrails como detail secundario.
- Recomendar charts nuevos sin explicar la necesidad de información.
- Redefinir las métricas duplicadas en vez de marcar el gap analítico.
- Proponer branding, una nueva paleta o implementación frontend.
- Afirmar qué usa el equipo sin evidencia.

## Success criteria

1. La reducción se basa en decisiones y roles, no en una preferencia por pantallas vacías.
2. No se pierde información crítica; cambia su nivel o acceso de forma justificada.
3. El overview semanal y el detail diagnóstico quedan separados y conectados.
4. Los filtros dejan de dominar sin impedir investigaciones necesarias.
5. Supuestos y necesidad de validar uso real quedan explícitos.
