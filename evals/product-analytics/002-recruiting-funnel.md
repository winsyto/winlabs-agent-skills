# Eval 002 — Recruiting funnel

## Scenario

Un equipo de Talent Acquisition necesita medir un proceso concreto y mejorar eficiencia sin degradar calidad o equidad.

## User request

> Diseñá las métricas para nuestro funnel de recruiting, desde postulación hasta contratación. Necesitamos detectar cuellos de botella y reducir el tiempo de cobertura sin bajar la calidad.

## Expected activation

Sí. `product-analytics` debe activarse porque se solicitan definición, jerarquía e interpretación de métricas para un workflow ordenado.

## Context

- Etapas: postulación, screening, entrevista, oferta, aceptación e ingreso.
- Actores: candidatos, recruiters, hiring managers y áreas solicitantes.
- Decisiones: dónde intervenir, qué etapa demora y si acelerar perjudica calidad o experiencia.
- Diferentes roles tienen volúmenes y dificultad de cobertura distintos.
- No existe definición acordada de “calidad de contratación”.

## Expected characteristics

- Definir población de entrada, unidad —candidato o vacante— y ventanas del funnel.
- Explicar conversión entre etapas con denominadores coherentes y tratamiento conceptual de abandonos o reaperturas.
- Separar time-to-fill de tiempos por etapa y espera entre actores.
- Incorporar dimensiones diagnósticas justificadas, como familia de rol o seniority.
- Proponer guardrails para calidad, candidate experience y equidad cuando sean medibles y pertinentes.
- Marcar “quality of hire” como concepto que requiere definición conjunta, no como cifra universal.
- Asociar patrones de métricas con decisiones o investigaciones.

## Required concepts

- funnel y conversion;
- efficiency;
- quality;
- guardrails;
- segmentation;
- comparación entre períodos, targets internos o cohorts de vacantes;
- multi-actor interpretation.

## Forbidden / undesirable behavior

- Sumar porcentajes de conversión con denominadores incompatibles.
- Tratar “cantidad de postulantes” como éxito por sí sola.
- Optimizar velocidad sin guardrails.
- Inventar un target universal de días o conversiones.
- Recomendar ATS, SQL, eventos, dashboards o gráficos.
- Usar atributos sensibles como dimensiones sin reconocer privacidad, equidad y tamaño de muestra.

## Success criteria

1. El funnel está definido como secuencia analítica y no como dibujo visual.
2. Conversión, tiempo y calidad habilitan decisiones diferentes y explícitas.
3. Los guardrails evitan que reducir time-to-fill sea el único objetivo.
4. Las dimensiones propuestas responden a hipótesis diagnósticas.
5. Los conceptos sin definición organizacional quedan marcados como pendientes.
