# Diseño conceptual de `dashboard-ux`

Estado del documento: base conceptual del contrato operativo.

Estado de la skill: Experimental.

Milestone: v0.1 — Analytics & Dashboard Foundation.

Base conceptual: [research de `dashboard-ux`](../research/dashboard-ux-research.md).

## Purpose

Determinar cómo presentar, organizar y permitir explorar información analítica para que una audiencia pueda comprender una situación y tomar decisiones.

La responsabilidad primaria comprende arquitectura de información, jerarquía, prioridad, densidad, navegación, comparación, interacción, estados, responsive behavior y requisitos preventivos de accesibilidad. El resultado debe ser una especificación de experiencia, no una estrategia métrica, un catálogo de gráficos ni una implementación.

## Principles

1. Diseñar para una audiencia, una tarea y un contexto de uso concretos.
2. Hacer que la prominencia refleje prioridad de decisión, urgencia o riesgo.
3. Preservar significado, comparación y freshness del contrato analítico.
4. Separar overview, contexto y detail sin ocultar información crítica.
5. Usar interacción solo cuando reduce trabajo o complejidad neta.
6. Ajustar densidad al modo de trabajo; no asumir que menos siempre es mejor.
7. Tratar estados, responsive behavior y accesibilidad como parte del significado.
8. Evitar invadir analytics, visualization especializada o implementación.

## Activation cases

- “Diseña la estructura de un dashboard de métricas ya definidas.”
- “¿Qué debería ir arriba y qué debería quedar en detalle?”
- “Tenemos demasiados KPIs y la pantalla es difícil de leer.”
- “Necesito organizar un dashboard operativo.”
- “¿Cómo debería funcionar el drill-down?”
- “Diseña la experiencia para comparar períodos y segmentos.”
- “Este dashboard se ve lleno y cuesta entenderlo.”
- “Organiza estados, alertas y excepciones para que el equipo actúe rápido.”
- “Adapta esta jerarquía analítica a desktop y mobile sin perder contexto.”

## Non-activation cases

- “Define los KPIs para este producto.” → `product-analytics`.
- “Diseña el funnel y la estrategia de retención.” → `product-analytics`.
- “Escribe el SQL.” → análisis o ingeniería de datos.
- “Implementa estos charts en React.” → implementación frontend.
- “Crea el tracking plan.” → instrumentación analytics.
- “Diseña la base de datos.” → data modeling.
- “Elige una librería de gráficos.” → implementación o data visualization.
- “Haz un landing page de marketing.” → diseño/frontend de marketing.
- “Crea el branding, la paleta y la tipografía del producto.” → brand o design system.
- “Audita formalmente WCAG sobre esta aplicación.” → accessibility review.

En pedidos mixtos, resolver solo la parte de dashboard UX que tenga inputs suficientes y explicitar los handoffs. No interpretar “dashboard” como autorización para definir métricas, escribir código o crear visual assets.

## Inputs

### Required

Obtener, aunque sea de forma provisional:

- **audience:** quién usará la experiencia y su nivel de conocimiento;
- **decisions/tasks:** qué debe detectar, comprender, decidir o ejecutar;
- **metrics/information:** contrato o inventario de información a presentar;
- **context of use:** frecuencia, presión temporal, dispositivo o entorno relevante.

Audience y decisions/tasks son indispensables para una jerarquía defendible. Metrics/information puede estar incompleto si el pedido es una exploración preliminar, pero no puede inventarse una estrategia métrica completa.

### Useful

- frecuencia y cadence de revisión;
- prioridad y materialidad conocida;
- roles de las métricas —outcome, driver, diagnostic o guardrail—;
- dimensiones y segmentos;
- comparisons y targets acordados;
- freshness y tolerancia a stale data;
- thresholds o reglas de alerting ya aprobadas;
- acciones habilitadas;
- device, viewport y contexto físico;
- experiencia y vocabulario de la audiencia;
- restricciones de espacio, performance, privacidad o permisos;
- estados de datos esperables.

### Optional

- design system existente;
- screenshots o layout actual;
- component library;
- patrones de navegación del producto;
- requisitos de accesibilidad adicionales;
- hallazgos de research o pruebas de usabilidad;
- restricciones técnicas que afecten el handoff.

### Cuando falta información

1. Preguntar primero por audiencia, decisión y existencia del contrato analítico.
2. Preguntar solo por faltantes capaces de cambiar materialmente jerarquía, modo o interacción.
3. Avanzar con supuestos mínimos cuando sean explícitos, reversibles y no alteren qué se mide.
4. Entregar alternativas condicionadas cuando dos supuestos plausibles producen estructuras distintas.
5. Derivar a `product-analytics` cuando falten métricas, definiciones o comparaciones necesarias para decidir el contenido.
6. Registrar como gap freshness, permisos, thresholds, estados o constraints desconocidos; no inventarlos.

No bloquear por detalles cosméticos o técnicos que pertenecen a implementación.

## Metric contract gate

Antes de diseñar, clasificar la situación:

| Estado | Respuesta de `dashboard-ux` |
| --- | --- |
| Contrato suficiente | Diseñar jerarquía, estructura, exploración, estados y handoff. |
| Contrato parcial pero estable | Avanzar sobre lo confirmado, declarar supuestos y aislar gaps. |
| Falta menor de contexto UX | Hacer una o pocas preguntas discriminantes o proponer opciones condicionadas. |
| Faltan decisiones o contenido métrico | Solicitar definición analítica o activar `product-analytics`. |
| Pedido mixto desde cero | Secuenciar `product-analytics` → handoff semántico → `dashboard-ux`. |

No exigir una North Star, un metric tree ni una tabla formal si el contenido semántico ya es suficiente.

## Dashboard mode

Clasificar solo cuando ayude a decidir jerarquía, densidad o interacción:

### Monitoring

Priorizar awareness, estado, cambios materiales, thresholds, alertas y freshness. Permitir llegar a diagnóstico sin convertir la vista en una consola operativa si no hay acción frecuente.

### Operational

Priorizar excepciones, status, cola de trabajo, próximas acciones y filtros frecuentes. Admitir alta densidad razonable cuando reduzca navegación y acelere lectura.

### Diagnostic

Priorizar comparación, drivers, segmentos, composición y explicaciones alternativas. Mantener la hipótesis o pregunta visible durante el drill-down.

### Exploratory

Priorizar flexibilidad, selection, filtros, múltiples perspectivas, historial y reset. Aportar defaults y orientación suficientes para evitar una superficie sin punto de partida.

### Executive

Priorizar outcomes, variaciones materiales, contexto, riesgos y decisiones. Limitar detalle inicial y hacer que la profundización sea intencional.

### Hybrid

Usar cuando existen tareas compatibles que necesitan convivir. Definir un modo dominante y separar las demás responsabilidades por zona o vista. No usar “hybrid” para justificar que todo aparezca junto.

## Workflow

### 1. Clarify audience and decisions

Definir persona o rol, tareas, decisiones, acciones, cadence y contexto. Distinguir hechos, supuestos y gaps.

### 2. Confirm the metric contract

Revisar información, roles, definiciones, comparaciones, dimensiones, guardrails y freshness. Aplicar el gate anterior sin reabrir decisiones analíticas acordadas.

### 3. Identify the dashboard mode

Elegir un modo dominante cuando cambie decisiones de diseño. Si existen modos incompatibles, proponer separación antes de ordenar contenido.

### 4. Prioritize information

Asignar prioridad según:

- decisión o acción habilitada;
- urgencia y coste de omisión;
- materialidad del cambio;
- rol como outcome o guardrail;
- frecuencia de consulta;
- necesidad de comparación inmediata;
- confianza y disponibilidad.

No priorizar por popularidad, disponibilidad, tamaño del dato o conveniencia visual.

### 5. Build the information hierarchy

Definir grupos, secuencia y relaciones. Distinguir:

- **primary:** necesario para orientarse o tomar la decisión principal;
- **secondary:** explica, compara o confirma lo primario;
- **detail:** diagnóstico o evidencia bajo demanda;
- **metadata:** definición, freshness, scope, calidad o limitaciones.

La jerarquía puede usar tamaño, posición, orden, agrupación, contraste o espacio en implementación, pero el diseño conceptual debe justificar la prioridad antes de prescribir recursos visuales.

### 6. Define overview versus detail

Hacer que el overview responda “qué ocurre y dónde mirar”. El detail debe responder una pregunta planteada por el overview y preservar filtros, comparación, entidad y retorno.

No imponer una sola página. Separar vistas cuando distintas audiencias, cadences o tareas competirían por prominencia.

### 7. Define the comparison model

Para cada comparación relevante, conservar medida, unidad, población, ventana, ancla y dirección. Priorizar una comparación principal y hacer secundarias las demás cuando su simultaneidad produzca ruido.

No redefinir si target, benchmark, período, cohorte, segmento o actor son analíticamente válidos.

### 8. Define interactions and navigation

Elegir el patrón mínimo que sostenga la tarea:

- filters para acotar población o contexto;
- drill-down para relaciones jerárquicas;
- cross-filtering para coordinar vistas relacionadas;
- tabs para perspectivas pares o modos separados;
- drawers para detalle medio sin perder contexto;
- modal para foco temporal, no navegación analítica profunda;
- inline expansion para detalle local;
- hover solo como complemento;
- selection para comparación o acción explícita;
- search para localizar entidades.

Definir cuando corresponda alcance, defaults, persistencia, estado activo, reset, deep-linking, retorno y alternativa por teclado/touch.

### 9. Define states and feedback

Cubrir únicamente los estados posibles pero no omitir diferencias semánticas:

- loading;
- empty o primera configuración;
- no-data legítimo;
- no-results por filtros;
- error;
- stale data;
- partial data;
- permission-limited data;
- anomalous state.

Para cada estado, describir qué ocurre, qué alcance afecta, qué contenido sigue siendo confiable y qué puede hacer la persona.

### 10. Validate density and scanability

Evaluar densidad por experiencia, frecuencia, decisiones simultáneas, dispositivo, coste de interacción y riesgo de omisión. Comprobar agrupación, alineación, consistencia, legibilidad y señal de excepción.

No convertir espacio en blanco, card count o “above the fold” en reglas absolutas.

### 11. Validate responsive hierarchy and accessibility

Preservar prioridad, contexto, lectura y acciones a través de tamaños y modalidades. Exigir keyboard access, focus visible, orden significativo, labels, non-color encoding, contraste y alternativas para información visual compleja.

### 12. Validate decision support

Comprobar que la audiencia puede:

1. orientarse;
2. identificar lo importante;
3. entender la comparación y freshness;
4. distinguir estado válido de ausencia o error;
5. llegar al detalle sin perder contexto;
6. decidir o actuar, o reconocer qué gap lo impide.

Eliminar contenido e interacción que no mejore alguna de estas capacidades.

El workflow es adaptable. Una consulta puntual puede requerir solo encuadre, prioridad y recomendación; una especificación completa puede cubrir todos los pasos.

## Handoff from `product-analytics`

```text
product-analytics
    ↓
audience
decisions
prioritized metrics
metric roles
definitions
comparisons
dimensions
cadence/freshness
guardrails
gaps
    ↓
dashboard-ux
```

### Directly consumable

| Campo | Uso en dashboard UX |
| --- | --- |
| Audience | Vocabulario, profundidad, densidad y contexto de uso. |
| Decisions | Orden, prominencia, navegación y acción. |
| Prioritized metrics | Inventario inicial, sin asumir igualdad visual. |
| Metric roles | Relación entre outcomes, drivers, diagnostics y guardrails. |
| Definitions | Labels, units, scope y detalle explicativo. |
| Gaps | Límites, preguntas y estados de confianza visibles. |

### Requires UX adaptation

| Campo | Adaptación |
| --- | --- |
| Comparisons | Contexto visible, prioridad y patrón de exploración. |
| Dimensions | Filtro, segmentación fija, drill-down o detail según tarea. |
| Cadence/freshness | Indicador de actualización, stale behavior y expectativa de respuesta. |
| Guardrails | Prominencia, proximidad al outcome y escalamiento de riesgo. |

### Generates questions

- ¿Qué decisión tiene mayor prioridad cuando varias compiten?
- ¿Qué comparación debe comprenderse sin interacción?
- ¿Qué dimensiones son frecuentes y cuáles diagnósticas?
- ¿Qué freshness vuelve insegura una decisión?
- ¿Qué thresholds o anomalías ya están acordados?
- ¿Qué permisos cambian el alcance visible?

Si la respuesta exige redefinir la métrica o su valor estratégico, devolver la pregunta a `product-analytics`.

## Information hierarchy contract

Una recomendación debe poder expresar, sin imponer un wireframe:

1. **Orientation:** alcance, período, filtros activos, freshness y propósito.
2. **Primary signals:** outcomes, excepciones, alertas o decisiones centrales.
3. **Context:** comparación, drivers, composición o explicación necesaria.
4. **Action and navigation:** qué puede hacerse y cómo se llega al detalle.
5. **Details:** tablas, entidades, definiciones o análisis bajo demanda.
6. **Trust metadata:** data quality, partial/stale state, permisos, assumptions y gaps.

El orden no implica necesariamente una columna vertical ni una posición universal.

## Comparison model

`dashboard-ux` debe describir:

- comparison anchor principal;
- comparaciones secundarias disponibles;
- contexto mínimo siempre visible;
- interacción necesaria para cambiar comparación;
- efecto de filtros sobre ambas partes;
- tratamiento de ventanas incompletas o freshness desigual;
- modo de evitar que demasiadas series o segmentos compitan.

Puede sugerir una familia de representación —tendencia, ranking, distribución, relación, composición o tabla— cuando eso define la experiencia. La selección fina de encoding o una visualización especializada puede requerir otro handoff.

## States contract

| Estado | Significado que debe preservarse | Respuesta UX conceptual |
| --- | --- | --- |
| Loading | El dato todavía no está disponible | Mantener orientación, indicar alcance y evitar falsa precisión. |
| Empty | Todavía no existe contenido o configuración | Explicar qué aparecerá y el siguiente paso, si existe. |
| No-data | No hubo observaciones válidas | Diferenciar de cero, error y ausencia de permiso. |
| No-results | Filtros o búsqueda no encontraron coincidencias | Mostrar filtros activos y ofrecer reset o ajuste. |
| Error | No pudo obtenerse o procesarse información | Explicar alcance, conservar contenido válido y ofrecer recuperación posible. |
| Stale | La última actualización supera la tolerancia | Mostrar timestamp, impacto y acción; no presentar como actual. |
| Partial | Solo parte de la cobertura está disponible | Indicar cobertura, limitar interpretación y evitar agregados engañosos. |
| Permission-limited | La persona no puede ver parte del contenido | Explicar alcance sin filtrar datos sensibles y orientar sobre acceso. |
| Anomalous | Una condición acordada requiere atención | Mostrar magnitud, contexto, prioridad y camino a diagnóstico o acción. |

## Density and scanability

### Favorecer mayor densidad cuando

- la audiencia es experta y usa la vista con frecuencia;
- varias excepciones deben compararse o atenderse rápidamente;
- abrir detalle repetidamente sería costoso;
- tablas y status soportan una tarea operativa concreta;
- el entorno permite lectura sostenida y precisión.

### Favorecer menor densidad cuando

- la audiencia revisa ocasionalmente;
- existen pocas decisiones de alto impacto;
- el objetivo es síntesis y alineación;
- el detalle operativo distrae del outcome;
- el dispositivo o contexto reduce atención disponible.

En ambos casos, densidad no equivale a cantidad total. Agrupación, redundancia, labels, decoración e interacción cambian la carga cognitiva.

## Responsive behavior

Definir reglas semánticas, no breakpoints ni CSS:

- conservar primary signals y contexto de comparación;
- reordenar antes de reducir ilegiblemente;
- transformar detail persistente en acceso explícito cuando el espacio lo exija;
- hacer visibles filtros activos aunque los controles se compacten;
- evitar scroll horizontal para lectura general; permitirlo solo cuando una estructura tabular lo justifique y exista alternativa usable;
- mantener acciones frecuentes accesibles;
- no eliminar freshness, estado o unidad para ahorrar espacio.

## Accessibility notes

Toda especificación completa debe contemplar:

- navegación y operación por teclado;
- foco visible, ordenado y no atrapado;
- reading order coherente con la jerarquía;
- labels significativos para métricas, controles e iconos;
- estado, selección, tendencia y alerta comunicados además de color;
- contraste suficiente de texto, controles y objetos gráficos necesarios;
- valores, tendencias o relaciones esenciales disponibles en texto o tabla cuando corresponda;
- hover, drag o gestos con alternativa equivalente;
- anuncios de loading, error y cambios dinámicos cuando sean relevantes;
- zoom/reflow y jerarquía responsive sin pérdida de información crítica.

`dashboard-ux` define estos requisitos; una auditoría WCAG formal y su implementación pertenecen a capacidades especializadas.

## Output contract

Adaptar la profundidad al pedido. Una respuesta completa debería poder incluir:

1. **Context and assumptions:** alcance, inputs confirmados y gaps.
2. **Audience:** rol, experiencia y contexto de uso.
3. **Primary decisions/tasks:** qué debe detectar, decidir o ejecutar.
4. **Dashboard mode:** clasificación y efecto sobre el diseño, si aporta valor.
5. **Information hierarchy:** primary, secondary, detail y metadata.
6. **Sections:** propósito, contenido y relación de cada zona o vista.
7. **Comparison model:** anchors, contexto y prioridades.
8. **Interaction model:** filtros, selection, navegación y detail pattern.
9. **States:** significado, alcance y recuperación.
10. **Responsive behavior:** qué se conserva, reordena o cambia de patrón.
11. **Accessibility notes:** requisitos observables.
12. **Rationale:** por qué la estructura soporta decisiones.
13. **Open gaps:** analytics, datos, thresholds, permisos o constraints pendientes.

No forzar todas las secciones ni wireframes ASCII. Usar tabla, flujo, árbol, narrativa o wireframe solo si aclara relaciones materiales.

## Handoff to implementation

Entregar cuando corresponda:

- estructura de vistas y secciones;
- orden y prioridad del contenido;
- relaciones overview/detail;
- comportamiento de filtros, selección, navegación y reset;
- comparison model;
- estados y feedback;
- reglas responsive semánticas;
- requisitos de accesibilidad;
- supuestos, gaps y decisiones todavía abiertas.

No entregar React, CSS, tokens, APIs de componentes, librerías, queries, eventos ni pipelines. Si existe un design system, referenciar restricciones y componentes disponibles sin rediseñarlo.

## Quality criteria

Una respuesta de calidad cumple de forma observable:

- cada elemento visible tiene propósito asociado a orientación, decisión, acción o explicación;
- audiencia, decisiones y contexto de uso están explícitos;
- la jerarquía refleja prioridad y no simetría estética;
- las decisiones principales pueden abordarse sin exploración excesiva;
- overview y detail tienen responsabilidades distintas y conectadas;
- cada comparación conserva ancla, unidad, población y período necesarios;
- la densidad corresponde al modo, frecuencia y experiencia;
- filtros e interacción no dominan la interfaz ni esconden estado;
- los patrones de detalle preservan contexto y retorno;
- loading, empty, no-data, error, stale, partial, permissions y anomaly se consideran cuando aplican;
- freshness y calidad limitan la interpretación de forma visible;
- responsive behavior preserva prioridad y contexto;
- no se depende solo de color, hover o pointer;
- keyboard, focus, labels y alternativas de información compleja son verificables;
- no se agrega contenido por simetría o por llenar espacio;
- assumptions y gaps están explícitos;
- no se redefine arbitrariamente la estrategia métrica;
- no se invade SQL, tracking, data modeling, design system o implementación.

## Anti-patterns

- KPI wall;
- card soup;
- chart zoo;
- decorative visualization;
- excessive color;
- excessive filters;
- hidden comparison context;
- ambiguous units;
- dashboard without audience;
- dashboard without decisions;
- excessive drill-down;
- overuse of modals;
- everything above the fold;
- forced symmetry;
- visual hierarchy unrelated to importance;
- real-time by default;
- zero used for no-data or error;
- hover-only meaning;
- responsive disappearance of critical context;
- redefining KPIs to make a layout possible;
- prescribing code or libraries in a conceptual handoff.

## Progressive disclosure

### Must remain in `SKILL.md`

- purpose and discriminating description;
- activation and non-activation boundaries;
- required inputs and metric contract gate;
- adaptable workflow;
- dashboard modes as a short routing aid;
- output contract;
- main quality gates and anti-patterns;
- direct links explaining when to read each reference.

### Implemented reference architecture

El contrato operativo materializa las cuatro referencias cuyo detalle cambia decisiones reales y las carga solo bajo condición.

| Archivo | Responsabilidad | Leer cuando |
| --- | --- | --- |
| `modes-and-information-hierarchy.md` | Modos, prioridad, agrupación, density, overview/detail y separación de vistas. | Se deba diseñar o corregir estructura, prominencia o densidad. |
| `exploration-and-comparison.md` | Comparison model, filtros, drill-down, cross-filtering, navigation, detail patterns y reversibilidad. | El pedido incluya comparación, exploración o interacción analítica. |
| `states-and-feedback.md` | Loading, empty, no-data, no-results, error, stale, partial, permissions y anomaly. | La disponibilidad, calidad o feedback de datos cambie la experiencia. |
| `accessibility-and-responsive.md` | Keyboard, focus, non-color, chart alternatives, labels y preservación responsive de jerarquía. | Se produzca una especificación completa o exista riesgo de acceso/dispositivo. |

### Alternatives rejected

- `information-hierarchy.md` y `dashboard-modes.md` separados: modo, prioridad y densidad se necesitan juntos y producirían duplicación.
- `interaction-patterns.md` como catálogo aislado: alentaría seleccionar componentes sin relación con comparación o tarea.
- `density.md` independiente: la densidad es consecuencia de modo, audiencia y coste de interacción.
- `chart-selection.md`: invadiría data visualization y convertiría la skill en una librería de recetas.
- `anti-patterns.md`: los anti-patterns esenciales deben quedar cerca del workflow o de la referencia que contiene la corrección.

No se justifican scripts ni assets. Los evals permanecen fuera de la skill.

## Eval coverage

La suite inicial debe verificar:

| Eval | Capacidad principal |
| --- | --- |
| 001 — Executive dashboard | Síntesis, prioridad, comparación y detail limitado. |
| 002 — Operational dashboard | Densidad, status, exceptions, acciones y filtros. |
| 003 — Overloaded dashboard | Reducción y reorganización sin pérdida crítica. |
| 004 — Negative KPI definition | No activación y handoff a `product-analytics`. |
| 005 — Ambiguous dashboard request | Clarificación mínima y routing conjunto. |
| 006 — Comparison-heavy dashboard | Múltiples anchors y segmentos sin sobrecarga. |

Los evals describen comportamiento observable y no una redacción o wireframe exactos.

## State recommendation

Clasificar `dashboard-ux` como **Experimental**: `SKILL.md` contiene un contrato operativo para Design y Review, las cuatro referencias tienen routing bajo demanda y la suite independiente cubre activación, límites y casos representativos.

La promoción indica que la skill ya puede probarse en proyectos reales, no que su comportamiento esté validado. Esta implementación no incluye una evaluación conductual completa. El siguiente gate es revisar un dashboard real, documentar resultados y corregir únicamente fallos observados.

No considerar Stable hasta completar la evaluación conductual, revisión independiente, forward testing, uso real y demás criterios de la guía de autoría.

## Open decisions

1. Validar con uso real si las cuatro referencias implementadas son el mínimo correcto.
2. Decidir el límite exacto entre sugerir una familia de representación y activar una futura capacidad de data visualization.
3. Probar dashboard híbrido con un caso real para definir criterios de separación de vistas.
4. Acordar si freshness/data quality requiere un bloque canónico en todo output completo.
5. Ejecutar el handoff desde `product-analytics` con métricas reales y observar gaps.
6. Evaluar el contrato en al menos Codex y Claude Code antes de considerar Stable.
7. Definir si una evaluación de accesibilidad especializada debe ser obligatoria para Stable o proporcional al riesgo y superficie.
