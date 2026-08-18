# Research de `product-analytics`

Fecha de consulta: 2026-08-18
Milestone: v0.1 — Analytics & Dashboard Foundation

## Scope

El problema no es generar una lista de indicadores, sino ayudar a un agente a construir un sistema de medición que conecte objetivos, comportamiento de usuarios y decisiones. La skill debe determinar qué medir, por qué importa, cómo definir cada métrica conceptualmente, contra qué interpretarla y qué acción o diagnóstico puede habilitar.

La investigación se concentra en selección, jerarquía, definición e interpretación de métricas de producto. Quedan fuera diseño visual de dashboards, elección de gráficos o herramientas, SQL, schemas físicos, tracking, taxonomías de eventos, pipelines e implementación.

La hipótesis inicial fue:

```text
Business / Product Objective
        ↓
User / Actor
        ↓
Decisions to Support
        ↓
Metric Hierarchy
        ↓
Metric Definitions
        ↓
Diagnostic Dimensions
        ↓
Interpretation & Action
```

La investigación respalda su dirección, pero sugiere introducir explícitamente el valor u outcome antes de construir la jerarquía, incorporar comparaciones dentro de cada definición y cerrar con una validación de utilidad y riesgos.

## Sources reviewed

La trazabilidad detallada, incluidas licencias y decisiones de uso, está registrada en [sources.md](sources.md).

1. `alirezarezvani/claude-skills` — `product-analytics`.
2. `borghei/Claude-Skills` — `product-analytics`.
3. `borghei/Claude-Skills` — `metrics-dashboard`.
4. `rampstackco/claude-skills` — `analytics-strategy`.
5. `NickCrew/Claude-Cortex` — `dashboard-designer`, revisada solo para delimitar responsabilidades.
6. Amplitude — North Star Metric Resources.
7. Rodden, Hutchinson y Fu — HEART y Goals-Signals-Metrics, Google Research / CHI 2010.

No se copió texto ni estructura de estas fuentes. Se compararon sus decisiones de diseño y se sintetizó una metodología propia.

## Concepts identified

### Trabajar desde decisiones, no desde inventarios

El patrón más consistente es comenzar por las preguntas o decisiones que deben apoyarse. Esto evita dos fallas frecuentes: elegir métricas porque están disponibles y construir dashboards antes de entender para qué servirán.

Una métrica merece entrar en el sistema cuando existe una cadena defendible:

```text
objective → actor and value → decision → metric → comparison → interpretation → action
```

### Separar roles de métricas

Una jerarquía útil puede incluir, según el problema:

- **Outcome metrics**: expresan el resultado buscado para el usuario, el producto o el negocio.
- **Driver o input metrics**: representan comportamientos o condiciones que pueden influir sobre un outcome y suelen ser más cercanos a la intervención.
- **Diagnostic metrics**: ayudan a localizar dónde o para quién cambia un resultado; no necesariamente son objetivos.
- **Guardrail metrics**: detectan daños, trade-offs o conductas de gaming al optimizar outcomes o drivers.

Estos roles son más útiles que una taxonomía universal por etapa. Una misma métrica puede ser outcome en un alcance y driver en otro; debe declararse su rol dentro del problema analizado.

### North Star como opción, no requisito

Una North Star Metric puede alinear un producto cuando existe una expresión estable del valor entregado y una relación defendible con resultados sostenibles. No debe imponerse cuando:

- el producto tiene múltiples actores con intercambios de valor diferentes;
- el alcance es una feature o workflow acotado;
- el producto está demasiado temprano para identificar un comportamiento de valor estable;
- una sola métrica ocultaría calidad, riesgo o resultados de negocio relevantes.

En esos casos puede ser mejor usar un pequeño conjunto de outcomes balanceados.

### Definición antes que disponibilidad técnica

La definición conceptual debe preceder a SQL, eventos o herramientas. Como mínimo, una métrica necesita:

- fenómeno que representa;
- razón de relevancia;
- población y unidad de análisis;
- numerador, denominador o agregación conceptual cuando corresponda;
- ventana temporal y momento de observación;
- inclusiones, exclusiones y casos límite importantes;
- comparación necesaria;
- interpretación esperada y decisión habilitada.

La disponibilidad de datos se registra como factibilidad, supuesto o gap. La skill no debe convertir ese gap en un tracking plan.

### Comparación como parte de la métrica

Un valor aislado rara vez es interpretable. La comparación puede ser contra:

- período previo comparable;
- baseline previo a un cambio;
- target explícitamente acordado;
- cohorte o segmento relevante;
- benchmark externo confiable y realmente comparable.

Targets y benchmarks no deben inventarse. Cuando no existen, se los marca como pendientes y se propone establecer una baseline.

### Funnels, cohorts y lifecycle concepts bajo condición

- Usar **funnel** cuando existe una secuencia ordenada, una población de entrada y ventanas de conversión definibles. No usarlo para recorridos inherentemente no lineales sin reconocer esa limitación.
- Definir **activation** como evidencia temprana de valor, no como registro o setup por defecto.
- Distinguir **adoption** —quién comienza a usar una capacidad significativa— de **engagement** —frecuencia, profundidad o amplitud del uso valioso—.
- Definir **retention** por repetición o continuidad de un comportamiento de valor, con cohorte, ancla y período explícitos.
- Usar **cohorts** cuando el tiempo desde un evento de origen o una exposición cambia la interpretación; no segmentar por cohorte de manera ritual.

### Dimensiones diagnósticas con hipótesis

Segmentar es útil si una diferencia entre grupos puede cambiar un diagnóstico o una acción. Las dimensiones deben elegirse por hipótesis —por ejemplo rol, plan, canal, antigüedad o tipo de cuenta—, no porque el atributo esté disponible. También deben considerarse tamaño de muestra, privacidad y riesgo de sobreinterpretación.

### Interpretación sin falsa causalidad

Una variación métrica genera observaciones e hipótesis; por sí sola no demuestra causa. Una buena respuesta distingue:

- lo observado;
- la interpretación posible;
- explicaciones alternativas;
- evidencia adicional necesaria;
- acción reversible o investigación recomendada.

## Comparison

| Enfoque | Coincidencias y fortalezas | Debilidades o solapamientos | Decisión local |
| --- | --- | --- | --- |
| `alirezarezvani/product-analytics` | Distingue etapas del producto, recomienda tendencias, cohorts, comparaciones, owner y reglas de decisión. Conecta movimientos con acciones. | Incluye diseño de capas de dashboard y scripts de cálculo. Tiende a seleccionar frameworks antes de formular decisiones. | Adaptar criterios de contexto, comparación y acción. Descartar dashboard design y cálculo automatizado. |
| `borghei/product-analytics` | Pone “decisions from data” en el centro, usa value moment, árbol de métricas, guardrails y prueba de vanity. Explicita supuestos cuando falta contexto. | Mezcla contrato conceptual con instrumentación, auditoría de eventos, scripts y dashboards. Prescribe una North Star y cantidades fijas con demasiada facilidad. | Incorporar cadena valor–decisión–métrica, guardrails y prueba “So what?”. Hacer North Star y cardinalidades opcionales. Excluir instrumentación y tooling. |
| `borghei/metrics-dashboard` | Diferencia outcome, inputs, guardrails y métricas operativas. Exige comparación, owner y acción. | Su objetivo es arquitectura de dashboard, cadence y visualización, responsabilidades de `dashboard-ux` o futuras skills. | Adaptar roles semánticos y disciplina de comparación; descartar layout, chart choice y dashboard inventory. |
| `rampstackco/analytics-strategy` | Trabaja hacia atrás desde preguntas, conecta métricas con outcomes y reconoce audiencia, contexto y decisiones. | Es una mega-skill: combina KPIs, eventos, atribución, tracking, implementación, dashboards y governance. Impone AARRR y North Star como estructura general. | Incorporar enfoque questions-first. Rechazar el alcance combinado y usar frameworks solo cuando encajen. |
| `NickCrew/dashboard-designer` | Explicita audiencia, decisión, acción y comparabilidad antes del diseño. Permite trazar una frontera concreta. | Mezcla selección de KPIs con layout, color, charts y herramientas BI; su activación solapa solicitudes ambiguas de dashboard. | Usar solo para definir handoff: `product-analytics` decide el contenido semántico; `dashboard-ux`, la representación e interacción. |
| Amplitude North Star | Vincula valor del usuario, capacidad de influencia y resultado sostenible; distingue North Star de KPIs de soporte. | Marco orientado a una métrica unificadora y publicado por un proveedor de analytics. Puede simplificar productos multi-actor o etapas tempranas. | Adaptar sus tests como criterios opcionales, nunca como requisito universal. |
| Google HEART / Goals-Signals-Metrics | Mapea objetivos a señales y métricas; aporta categorías de experiencia y foco user-centered. | HEART es una taxonomía de posibles áreas, no una lista que deba completarse. No cubre por sí sola outcomes de negocio ni jerarquías causales. | Incorporar Goals-Signals-Metrics como inspiración para definitions; usar HEART solo si la calidad de experiencia es relevante. |

### Coincidencias

- Empezar por valor, preguntas o decisiones mejora la selección.
- Una jerarquía pequeña es más útil que una lista plana de KPIs.
- Outcomes necesitan drivers y, cuando existe riesgo, guardrails.
- Comparaciones, segmentación y cohorts convierten valores en información.
- La prueba de acción o “So what?” es central para detectar vanity metrics.

### Diferencias

- Algunas fuentes tratan North Star como obligatoria; otras permiten varios outcomes.
- AARRR y HEART aparecen como marcos generales, aunque resuelven problemas diferentes.
- Varias skills incluyen tracking, scripts, dashboard design y herramientas BI; el alcance local los separa deliberadamente.
- Owner y cadence se tratan como obligatorios en dashboards, pero para definición conceptual pueden quedar como contexto útil o pendiente sin invalidar toda la métrica.

### Solapamientos

La selección de métricas es el principal punto de contacto con `dashboard-ux`. La frontera propuesta es:

- `product-analytics`: qué información debe existir y qué decisión permite.
- `dashboard-ux`: cómo organizar, representar y hacer interactiva esa información para una audiencia.

Ante “Necesito un dashboard”, primero interviene `product-analytics` si objetivos, decisiones o métricas no están definidos. Si ya existe un conjunto acordado de métricas y la solicitud trata de layout, visualización, interacción o jerarquía visual, corresponde `dashboard-ux`. En una solicitud mixta, ambas pueden ejecutarse en secuencia con un handoff explícito.

## Anti-patterns detected

- **Vanity metric**: crece o impresiona sin representar valor ni habilitar una decisión.
- **KPI shopping list**: catálogo genérico por industria o framework sin vínculo con el objetivo.
- **Framework completion**: llenar AARRR, HEART u otra taxonomía aunque varias categorías no sean pertinentes.
- **Mandatory North Star**: forzar una sola métrica cuando el producto o el alcance requiere varios outcomes.
- **Metric without definition**: nombre ambiguo sin población, ventana, unidad o reglas de inclusión.
- **Metric without comparison**: número sin baseline, target, período o grupo de referencia.
- **Metric without “So what?”**: no existe interpretación ni decisión plausible asociada.
- **Outcome-only system**: métricas demasiado tardías sin drivers accionables.
- **Driver-only system**: actividad optimizable sin comprobar valor o resultado.
- **Missing guardrails**: optimización que puede degradar calidad, equidad, confianza, coste o resultados de otro actor.
- **Redundant metrics**: variantes que no cambian diagnóstico ni decisión y agregan ruido.
- **Segmentation by availability**: cortes arbitrarios sin hipótesis, acción o tamaño suficiente.
- **False causality**: atribuir un movimiento a una causa usando solo correlación temporal.
- **Invented target or benchmark**: presentar una cifra sin fuente o comparabilidad defendible.
- **Ownerless review**: métrica sin consumidor o responsable de decidir cuando el contexto organizacional lo requiere.
- **Dashboard substitution**: usar un dashboard como reemplazo del razonamiento sobre objetivos, decisiones y definiciones.
- **Implementation leakage**: resolver SQL, tracking, schemas, pipelines o visualización dentro de la definición conceptual.

## Proposed methodology

### 1. Encuadrar objetivo y alcance

Identificar el objetivo de negocio o producto, el problema, la etapa y el horizonte de decisión. Separar hechos, supuestos y preguntas abiertas.

### 2. Identificar actores, valor y unidad de análisis

Determinar quién recibe valor, quién toma decisiones y si la unidad relevante es usuario, cuenta, equipo, transacción, caso u otra. En productos multi-actor, representar los intercambios y tensiones entre actores.

### 3. Formular decisiones y preguntas

Expresar qué decisión cambiaría según el resultado: invertir, iterar, investigar, intervenir, mantener o retirar. Si no existe una decisión real, cuestionar la necesidad de la métrica.

### 4. Definir outcomes

Describir qué cambio observable indicaría progreso. Elegir una North Star solo si representa valor entregado, es influenciable y conecta con un resultado sostenible; de lo contrario, usar pocos outcomes balanceados.

### 5. Construir una jerarquía mínima

Relacionar outcomes con drivers plausibles, diagnósticos necesarios y guardrails. La jerarquía expresa una hipótesis de funcionamiento, no causalidad demostrada. No imponer cantidad fija ni cubrir categorías irrelevantes.

### 6. Definir cada métrica conceptualmente

Responder:

1. **What**: fenómeno, población, unidad y ventana.
2. **Why**: vínculo con objetivo, outcome o riesgo.
3. **How**: cálculo conceptual, denominadores e inclusiones/exclusiones.
4. **Compared to what**: baseline, período, target, cohorte, segmento o benchmark.
5. **So what**: observación, decisión, acción o investigación que habilita.

Agregar rol jerárquico, dirección esperada, owner o cadence solo cuando aporten a la decisión.

### 7. Elegir análisis diagnósticos

Incorporar funnels, cohorts, lifecycle concepts y dimensiones únicamente cuando ayuden a explicar variaciones o decidir acciones. Declarar la hipótesis que justifica cada corte.

### 8. Incorporar guardrails y tensiones

Preguntar cómo podría mejorarse artificialmente un outcome o driver y qué daño quedaría oculto. Seleccionar guardrails proporcionales a riesgos reales.

### 9. Explicar interpretación y acciones

Para movimientos relevantes, describir qué observar, qué no puede concluirse, qué explicaciones alternativas evaluar y qué acción o investigación seguiría. Evitar inferencias causales sin diseño apropiado.

### 10. Validar utilidad y factibilidad

Revisar alineación, minimalidad, no redundancia, comparabilidad, accionabilidad, riesgo de gaming, disponibilidad conceptual y supuestos. Registrar gaps de datos sin diseñar la implementación para resolverlos.

## Open decisions

1. **Owner y cadence**: decidir durante la implementación de `SKILL.md` si son campos recomendados o requeridos solo para outputs operativos recurrentes.
2. **Targets**: definir si la skill debe proponer un proceso para establecerlos cuando no existen o limitarse a marcarlos como pendientes.
3. **Madurez de evidencia**: decidir cuánto debe distinguir entre una jerarquía hipotética y relaciones validadas por análisis o experimentación.
4. **Handoff a `dashboard-ux`**: acordar el artefacto mínimo de transferencia cuando esa skill deje de ser esqueleto.
5. **Nivel de prescripción del output**: validar con evals si una tabla de definiciones recomendada mejora consistencia sin volver rígida toda respuesta.
6. **Compatibilidad**: comprobar el contrato futuro en Codex y Claude Code antes de promover a `Experimental`; otros agentes quedan en best effort.
