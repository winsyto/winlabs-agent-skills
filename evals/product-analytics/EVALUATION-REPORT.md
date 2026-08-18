# Reporte de evaluación conductual de `product-analytics`

## Environment

- **Fecha:** 2026-08-18.
- **Repositorio:** `winlabs-agent-skills`.
- **Branch:** `main`.
- **Remoto:** `origin` → `https://github.com/winsyto/winlabs-agent-skills.git`.
- **Commit base:** `179f64b6c7cbd367bdc386f6cff70901e2d72131` (`feat(product-analytics): v0.1 Experimental`).
- **Estado de la skill:** Experimental.
- **Estado inicial del working tree:** limpio.
- **Método:** evaluación manual/semi-estructurada. Para cada caso se determinó activación, se seleccionaron referencias según el routing del entrypoint, se simuló una respuesta concreta y se comparó semánticamente con characteristics, required concepts, forbidden behavior y success criteria. No se evaluó coincidencia literal ni se asignaron puntuaciones numéricas.

### Limitaciones

- La evaluación fue realizada en la misma conversación que desarrolló la implementación; no es una revisión ciega ni independiente y puede existir sesgo de confirmación.
- La preparación exigió leer todas las referencias. Progressive disclosure se evaluó por la selección que un agente debería hacer en cada escenario, no midiendo carga real de contexto.
- No existe runner ni instrumentación del selector automático de skills. La activación se evaluó a partir de la description, el request y el comportamiento simulado.
- Los outputs se probaron con contexto ficticio y sin datos reales, stakeholders ni targets validados. La evaluación cubre razonamiento conceptual y boundaries, no exactitud de cálculos.
- No se ejecutó forward testing en Claude Code ni en otro agente.

## Summary

| Eval | Activation | Quality | Boundaries | Result |
| --- | --- | --- | --- | --- |
| 001 — SaaS core metrics | Pass | Pass | Pass | PASS |
| 002 — Recruiting funnel | Pass | Pass | Pass | PASS |
| 003 — Feature adoption | Pass | Pass | Pass | PASS |
| 004 — Negative UI request | Pass | Pass | Pass | PASS |
| 005 — Ambiguous dashboard request | Pass | Pass | Pass | PASS |
| 006 — B2B operational module | Pass | Pass | Pass | PASS |
| 007 — Subscription retention | Pass | Pass | Pass | PASS |
| 008 — Multi-actor workflow | Pass | Pass | Pass | PASS |

Resultado global: **8 PASS, 0 PARTIAL, 0 FAIL**.

## Per-eval findings

## Eval 001 — SaaS core metrics

### Expected behavior

Activar `product-analytics`, transformar un objetivo abierto en pocas métricas específicas y distinguir cuenta, usuario y proyecto. Mantener separadas jerarquía, definición, outcomes de negocio y producto; no forzar una North Star ni inventar targets.

### Observed behavior

La respuesta simulada:

- declaró como supuesto que la cuenta es la unidad primaria de relación comercial, el proyecto la unidad del outcome operativo y el usuario una unidad diagnóstica;
- formuló decisiones sobre onboarding, valor recurrente, calidad del workflow y crecimiento sostenible antes de elegir métricas;
- propuso outcomes como cumplimiento útil de proyectos y continuidad de cuentas, con renovación como outcome de negocio tardío;
- trató activation, tiempo hasta primer valor, adopción del workflow y uso recurrente por cuenta como drivers o diagnósticos, no como equivalentes al outcome;
- definió métricas principales con población, numerador/denominador, ventana, comparación y acción habilitada;
- dejó activation, baseline, targets y benchmarks como supuestos o gaps a validar;
- incorporó guardrails de retrabajo, proyectos reabiertos o deterioro de calidad sin convertirlos en un catálogo genérico;
- evitó MRR, DAU, CAC o LTV como lista automática y no recomendó tracking, SQL, herramientas o visualizaciones.

### References used

- `metric-hierarchy.md`: separar outcomes, drivers, guardrails y evaluar North Star sin forzarla.
- `metric-definition.md`: definir unidades, ventanas, comparaciones y “So what?”.
- `lifecycle-analysis.md`: activation, engagement y retention con ritmo apropiado.

No fue necesario `interpretation-and-diagnostics.md`: el caso diseña el sistema y no interpreta un movimiento observado.

### Strengths

- Cadena clara objetivo → decisión → métrica.
- Unidades diferenciadas y jerarquía pequeña.
- Comparaciones y gaps explícitos.
- North Star tratada como opción.

### Problems

No se observaron fallas. El evento de activation y la cadence de retención quedan correctamente pendientes de validación contextual.

### Result

**PASS**

## Eval 002 — Recruiting funnel

### Expected behavior

Activar la skill para un workflow ordenado. Definir funnel, conversiones, tiempos, eficiencia, calidad y equidad con denominadores coherentes, unidades explícitas y guardrails.

### Observed behavior

La respuesta simulada:

- eligió la vacante como unidad para time-to-fill y throughput, y el candidato como unidad para conversiones entre etapas;
- definió conversión total y por etapa sin mezclar denominadores;
- distinguió tiempo total, tiempo de procesamiento y espera entre actores, recomendando mediana y percentiles en lugar de un único promedio;
- trató familia de rol, seniority y complejidad como dimensiones guiadas por hipótesis, no como ranking directo de recruiters;
- propuso como guardrails retiros de candidatos, reaperturas, experiencia del candidato, calidad posterior y equidad, con cautelas de privacidad y tamaño de muestra;
- marcó `quality of hire` como definición organizacional pendiente y no inventó un target universal;
- vinculó cuellos de botella con decisiones de capacidad, proceso o investigación sin atribuir causalidad automáticamente.

### References used

- `metric-definition.md`: unidades, tasas, tiempos, ventanas y comparaciones.
- `lifecycle-analysis.md`: funnel, conversiones, abandonos, reaperturas y maduración.
- `interpretation-and-diagnostics.md`: segmentación por complejidad, equidad, explicaciones alternativas y acciones.

No fue necesario `metric-hierarchy.md`: la estructura outcome/driver/guardrail del entrypoint fue suficiente para este funnel acotado.

### Strengths

- Separación correcta entre vacante y candidato.
- Eficiencia balanceada con calidad y equidad.
- Diagnósticos asociados con decisiones concretas.

### Problems

No se observaron fallas. La calidad posterior necesita definición y evidencia reales, tal como exige el eval.

### Result

**PASS**

## Eval 003 — Feature adoption

### Expected behavior

Activar la skill y separar elegibilidad, exposición, primer uso significativo, adopción, engagement y outcome. Evitar tratar volumen de comentarios como valor o afirmar efecto causal.

### Observed behavior

La respuesta simulada:

- limitó denominadores a planes, cuentas y usuarios elegibles durante el rollout;
- separó descubrimiento, primer thread con interacción significativa, adopción por cuenta y repetición del comportamiento;
- mantuvo unidades usuario y cuenta como lecturas distintas;
- cuestionó cantidad de comentarios y propuso validar una señal de coordinación resuelta, por ejemplo respuesta pertinente o cierre del thread dentro de una ventana acordada;
- usó cohortes por momento de habilitación con igual madurez y dejó pendiente una baseline comparable;
- incorporó guardrails como menciones ignoradas, threads sin resolver, notificaciones silenciadas, ruido o retrabajo;
- presentó cualquier mejora como asociación o hipótesis y derivó la demostración causal a evidencia adicional.

### References used

- `metric-hierarchy.md`: distinguir outcome de actividad y seleccionar guardrails.
- `metric-definition.md`: elegibilidad, unidades, ventanas y comparación.
- `lifecycle-analysis.md`: exposición, adopción, engagement, repetición y cohorts.

No fue necesario `interpretation-and-diagnostics.md`: el caso solicita definición, no diagnóstico de datos observados.

### Strengths

- Actividad y valor no se confunden.
- Elegibilidad y rollout quedan dentro de la definición.
- Guardrails relevantes y causalidad prudente.

### Problems

No se observaron fallas. La señal de “coordinación resuelta” permanece correctamente como hipótesis a validar.

### Result

**PASS**

## Eval 004 — Negative UI request

### Expected behavior

No activar `product-analytics`. Derivar diseño visual a `dashboard-ux` y React/CSS a una capacidad frontend sin revisar KPIs ni agregar trabajo analítico.

### Observed behavior

La respuesta simulada fue deliberadamente breve: indicó que las métricas están fijadas y el pedido es visual/de implementación, por lo que `product-analytics` no corresponde. Separó el routing entre `dashboard-ux` para experiencia visual y una capacidad frontend para React/CSS. No propuso métricas, North Star, charts ni condiciones analíticas.

### References used

Ninguna. La description y la sección “No usar cuando” resuelven la no activación.

### Strengths

- No activación inequívoca.
- Routing de diseño e implementación separado.
- Ausencia total de scope creep analítico.

### Problems

No se observaron fallas.

### Result

**PASS**

## Eval 005 — Ambiguous dashboard request

### Expected behavior

No asumir intención. Hacer una aclaración breve que distinga definición métrica de diseño visual y enrutar según la respuesta.

### Observed behavior

La respuesta simulada preguntó únicamente:

1. qué audiencia y decisión debe apoyar el dashboard;
2. si las métricas y sus definiciones ya están acordadas.

Explicó el routing condicional: si faltan objetivo, decisiones o métricas, aplicar `product-analytics`; si el contrato métrico ya existe y falta representación, derivar a `dashboard-ux`; si el pedido es mixto, completar primero el contrato semántico y hacer el handoff. No propuso KPIs ni layout antes de obtener la respuesta.

### References used

Ninguna. El caso se resuelve con las reglas de activación y handoff del entrypoint.

### Strengths

- Dos preguntas discriminantes, sin cuestionario excesivo.
- Routing visible y reversible.
- No presupone analytics ni UI.

### Problems

No se observaron fallas.

### Result

**PASS**

## Eval 006 — B2B operational module

### Expected behavior

Activar la skill y definir efficiency, throughput, adoption, quality y guardrails sin premiar cierres administrativos, actividad superficial o selección de trabajo fácil.

### Observed behavior

La respuesta simulada:

- definió solicitud como unidad primaria de throughput y calidad, y empleado, agente o área como unidades de adopción y diagnóstico;
- exigió acordar que “resuelta” significa resultado aceptado o no reabierto, no mero cambio de estado;
- definió throughput como solicitudes válidamente resueltas por período y segmento de complejidad;
- separó tiempo activo, espera y tiempo end-to-end, usando mediana y percentiles;
- midió adopción sobre empleados o áreas elegibles que completan el workflow de valor y su uso sostenido, no logins;
- incluyó captura de trabajo que todavía llega por canales externos como gap o diagnóstico de cobertura;
- propuso reaperturas, retrabajo, satisfacción, backlog envejecido y selección de casos fáciles como guardrails;
- recomendó construir baseline por categoría y madurez antes de acordar targets.

### References used

- `metric-hierarchy.md`: outcomes, drivers, guardrails y riesgo de gaming.
- `metric-definition.md`: unidades, throughput, tiempos, baseline y reglas de resolución.
- `lifecycle-analysis.md`: elegibilidad, primer uso y adopción sostenida.

No fue necesario `interpretation-and-diagnostics.md`: el caso define medición; el ajuste por complejidad pudo especificarse en la definición sin interpretar resultados reales.

### Strengths

- Cierre administrativo no sustituye valor.
- Throughput y eficiencia incluyen calidad y complejidad.
- Adoption se basa en workflow útil.

### Problems

No se observaron fallas. La definición de resolución y el tratamiento de canales externos quedan correctamente como validaciones previas.

### Result

**PASS**

## Eval 007 — Subscription retention

### Expected behavior

Activar la skill y distinguir retención contractual, churn, revenue, engagement de producto y cohorts con unidades y ritmos apropiados.

### Observed behavior

La respuesta simulada:

- eligió cuenta como unidad contractual y conservó usuario como diagnóstico de amplitud o concentración de uso;
- separó account retention, cancelación/churn, reactivación, gross/net revenue retention y continuidad del comportamiento de valor;
- definió churn sobre cuentas elegibles al inicio del período y trató reactivaciones y ventanas de gracia explícitamente;
- evitó DAU y propuso engagement alrededor del ciclo mensual de planificación, con frecuencia, amplitud y profundidad solo cuando representan valor;
- organizó cohortes por alta o activation y las comparó a la misma edad;
- mantuvo revenue y renovación como outcomes de negocio, y activation/engagement como drivers hipotéticos a validar;
- incluyó guardrails para que expansión de pocas cuentas no oculte pérdida de logos, segmentos o uso saludable;
- dejó target de retención y capacidad predictiva como gaps de evidencia.

### References used

- `metric-hierarchy.md`: separar outcomes de producto y negocio, drivers y guardrails.
- `metric-definition.md`: churn, revenue retention, poblaciones, ventanas y targets.
- `lifecycle-analysis.md`: ritmo mensual, retention, engagement, cohorts y reactivation.

No fue necesario `interpretation-and-diagnostics.md`: no se proporcionaron movimientos observados que exigieran diagnóstico causal.

### Strengths

- Cuenta y usuario no se confunden.
- Engagement respeta el ritmo mensual.
- Cohortes comparables y revenue no sustituye valor.

### Problems

No se observaron fallas. La acción de valor y las reglas contractuales requieren validación del negocio, como corresponde.

### Result

**PASS**

## Eval 008 — Multi-actor workflow

### Expected behavior

Activar la skill, modelar outcomes y unidades por actor, representar trade-offs y evitar una única métrica global de volumen o revenue.

### Observed behavior

La respuesta simulada:

- distinguió organización, especialista, solicitud y resolución como unidades;
- definió outcomes para organizaciones —resolución pertinente, previsible y de calidad— y para especialistas —oportunidades adecuadas, compensación y carga sostenible—;
- propuso una salud del intercambio basada en matching y resolución satisfactoria, sin declararla North Star única;
- mantuvo revenue por resolución satisfactoria como outcome de negocio tardío, no como sustituto del valor bilateral;
- trató relevancia del match, aceptación, tiempo hasta match y resolución como drivers hipotéticos;
- incorporó guardrails de concentración, rechazos por mala adecuación, disputas, reaperturas, carga, compensación y acceso desigual;
- seleccionó categoría, complejidad o capacidad como dimensiones solo cuando cambiarían decisiones de matching o capacidad;
- explicó trade-offs y acciones con lenguaje no causal.

### References used

- `metric-hierarchy.md`: productos multi-actor, unidades, North Star opcional, trade-offs y gaming.
- `metric-definition.md`: definiciones y comparaciones por actor.
- `interpretation-and-diagnostics.md`: dimensiones guiadas por hipótesis, composición, alternativas y acciones.

No fue necesario `lifecycle-analysis.md`: el pedido exige jerarquía y equilibrio, no funnel, adopción o retención.

### Strengths

- Valor bilateral y unidades explícitas.
- Ningún agregado oculta a un actor.
- Guardrails convierten trade-offs en decisiones observables.

### Problems

No se observaron fallas. Los thresholds de equilibrio y calidad permanecen correctamente pendientes de evidencia.

### Result

**PASS**

## Progressive disclosure validation

| Reference | Evals que la necesitaron | Motivo observado |
| --- | --- | --- |
| `metric-hierarchy.md` | 001, 003, 006, 007, 008 | Outcomes, drivers, North Star opcional, guardrails o productos multi-actor. |
| `metric-definition.md` | 001, 002, 003, 006, 007, 008 | Unidades, poblaciones, denominadores, ventanas, comparaciones y “So what?”. |
| `lifecycle-analysis.md` | 001, 002, 003, 006, 007 | Activation, funnel, adoption, engagement, retention o cohorts. |
| `interpretation-and-diagnostics.md` | 002, 008 | Segmentación sensible, mix, trade-offs, hipótesis y acciones diagnósticas. |

- Los evals 004 y 005 no requirieron referencias.
- Ningún escenario necesitó cargar las cuatro referencias.
- `metric-definition.md` fue la referencia más frecuente, coherente con el objetivo de definir métricas conceptualmente.
- El solapamiento sobre comparaciones es controlable: `metric-definition.md` establece el contrato de comparación; `interpretation-and-diagnostics.md` se usa cuando hay que explicar diferencias observadas.
- El solapamiento sobre guardrails también conserva responsabilidades: `metric-hierarchy.md` los selecciona; `interpretation-and-diagnostics.md` guía cómo leer sus movimientos.

Resultado: **PASS**. No se detectó solapamiento que justifique modificar routing o referencias.

## Boundary validation

### Negative UI request

La skill no se activó, no revisó KPIs y no produjo layout, charts, componentes o frontend. El routing distinguió `dashboard-ux` de implementación.

Resultado: **PASS**.

### Ambiguous dashboard request

La respuesta no asumió intención. Preguntó por decisión/audiencia y por existencia del contrato métrico; luego explicó las dos rutas y su posible secuencia.

Resultado: **PASS**.

### Otras fronteras

En los seis casos positivos no se generaron SQL, eventos, tracking plans, schemas, herramientas BI, charts ni afirmaciones causales no respaldadas.

Resultado: **PASS**.

## Quality validation

Los seis casos positivos mostraron:

- vínculo objetivo → decisión → métrica;
- outcomes separados de drivers y resultados de negocio;
- unidades, poblaciones, denominadores o ventanas cuando cambiaban la interpretación;
- comparaciones defendibles y targets faltantes tratados como gaps;
- “So what?” asociado con decisiones o investigaciones;
- guardrails proporcionales a riesgos reales;
- North Star opcional y nunca forzada;
- actividad diferenciada de valor;
- lenguaje causal prudente;
- supuestos y validaciones pendientes explícitos;
- ausencia de listas genéricas y vanity metrics como outcomes.

Resultado: **PASS**.

## Global findings

### Principales fortalezas

- La description discrimina solicitudes analíticas de UI, implementación, SQL y tracking.
- El entrypoint resuelve inputs faltantes sin bloquear ni inventar precisión.
- La regla What / Why / How / Compared to what / So what produce definiciones accionables.
- Las referencias tienen routing útil y no necesitan cargarse como paquete completo.
- La jerarquía soporta SaaS, operaciones y productos multi-actor sin convertir frameworks en formularios.
- Los quality gates resisten North Star forzada, vanity metrics, denominadores ambiguos y causalidad inventada.

### Debilidades y riesgos abiertos

- La evidencia proviene de simulación manual no ciega; falta forward testing independiente.
- La activación automática real depende del host y no fue instrumentada.
- El handoff es semánticamente consistente, pero `dashboard-ux` todavía no tiene contrato operativo para validar el consumo downstream.
- Casos con datos reales podrían revelar problemas de calidad, significancia o inferencia que están deliberadamente fuera del alcance actual.

No se identificó ninguna debilidad que requiera cambiar `SKILL.md`, sus referencias o los success criteria en esta tarea.

## Skill changes

No se modificaron `SKILL.md` ni las referencias. No hubo resultados PARTIAL o FAIL que justificaran una corrección.

## State recommendation

Recomendación: **Candidate for Stable**.

Justificación:

- ocho escenarios ejecutados y aprobados;
- activación y no activación correctas;
- routing ambiguo resuelto sin asumir intención;
- boundaries respetados;
- progressive disclosure coherente;
- outputs accionables y resistentes a anti-patterns;
- ningún problema crítico abierto.

Esta recomendación no cambia el catálogo. La skill debe permanecer en **Experimental** hasta decidir el gate de estabilidad y, preferentemente, completar forward testing independiente en Codex y Claude Code.

## Open decisions

1. Definir si la promoción a Stable exige una evaluación ciega por otro agente o persona.
2. Ejecutar los ocho escenarios en al menos Codex y Claude Code para validar activation y compatibilidad reales.
3. Validar el handoff contra el futuro contrato de `dashboard-ux`.
4. Decidir si un runner aporta valor después de contar con más fallos observados, sin introducir tooling prematuro.
5. Acordar la rúbrica y evidencia mínima para cambiar el estado canónico a Stable.
