# Research de `dashboard-ux`

Fecha de consulta: 2026-09-09.

Estado: investigación y síntesis conceptual previa al contrato operativo.

## Scope

`dashboard-ux` debe determinar cómo presentar, organizar y permitir explorar información analítica para que una audiencia comprenda una situación y tome decisiones. Su unidad de diseño no es el gráfico aislado ni la lista de KPIs, sino la experiencia completa de orientación, lectura, comparación, acción y profundización.

La skill debe poder:

- convertir un contrato analítico existente en una arquitectura de información;
- distinguir qué debe verse de inmediato, qué aporta contexto y qué queda bajo demanda;
- adaptar jerarquía, densidad, navegación e interacción al propósito del dashboard;
- preservar comparaciones, unidades, freshness, guardrails y gaps sin redefinirlos arbitrariamente;
- especificar estados de datos y requisitos de accesibilidad;
- producir un handoff conceptual implementable sin escribir código.

No debe resolver por conveniencia la estrategia métrica, el cálculo, la instrumentación, el modelo físico de datos, la implementación frontend ni el branding visual completo.

## Método de investigación

Se revisaron implementaciones públicas como evidencia comparativa, no como plantillas. Para cada fuente se separaron:

1. el problema que intenta resolver;
2. el workflow o modelo conceptual que propone;
3. los límites que declara o deja implícitos;
4. las prescripciones contextuales que no son portables;
5. los solapamientos con analytics, visualization, frontend y design systems.

Después se contrastaron esos patrones con fuentes primarias o institucionales para interaction design, accessibility y dashboard states. La trazabilidad detallada, licencias y decisiones de incorporación se registran en [sources.md](sources.md).

## Sources reviewed

| Fuente | Foco observado | Aporte principal | Riesgo de solapamiento |
| --- | --- | --- | --- |
| `NickCrew/Claude-Cortex` — `dashboard-designer` | Dashboard end-to-end | Audience, decision, action, overview/detail | KPI selection, chart rules y BI tooling |
| `nextlevelbuilder/ui-ux-pro-max-skill` | UI/UX y búsqueda de guidance | Routing bajo demanda, a11y, density, responsive | Mega-skill, branding, stacks y código |
| `Dammyjay93/interface-design` | Product interface craft | Persona/tarea, jerarquía deliberada, navegación | Estética, design system e implementación |
| Anthropic — `frontend-design` | Dirección visual de frontend | Intencionalidad y estructura con propósito | Diseño expresivo y código productivo |
| `NTCoding/claude-skillz` — `data-visualization` | Visualization y encodings | Overview/focus/detail, interacción, non-color | Chart selection, algoritmos y librerías |
| `alexander-kastil/skills-collection` / upstream `wshobson/agents` | KPI dashboards | Niveles, comparaciones, freshness y drill-down | Métricas, SQL, thresholds e infraestructura |
| `borghei/Claude-Skills` — `metrics-dashboard` | Metric/dashboard architecture | Audience fit, cadence, comparación y poda | North Star, KPIs, scripts y charts |
| Shneiderman — *The Eyes Have It* | Information seeking | Overview, filter, detail, history | No cubre dashboard purpose ni estados modernos |
| W3C WAI — WCAG 2.2 y tutoriales | Accessibility | Keyboard, focus, contrast, alternativas textuales | No define arquitectura de dashboard |
| IBM Carbon — loading y empty states | System feedback | Taxonomía de estados y acciones de recuperación | Componentes de un design system concreto |
| Nielsen Norman Group — progressive disclosure | Interaction design | Deferir complejidad sin ocultarla | Principio general, no priorización analítica |

## Concepts identified

### 1. El propósito antecede al layout

La coincidencia más fuerte entre fuentes es comenzar por audiencia y tarea. “Dashboard” describe un artefacto, no una necesidad homogénea. Dos vistas con las mismas métricas pueden necesitar jerarquías opuestas si una sirve para revisión mensual ejecutiva y otra para intervención operativa continua.

El propósito puede expresarse como una combinación de:

- quién observa;
- qué debe detectar, comprender o decidir;
- qué acción puede realizar;
- con qué frecuencia y presión temporal;
- en qué contexto o dispositivo;
- qué daño produce pasar algo por alto.

Una vista sin audiencia ni decisión defendible no está lista para diseño detallado.

### 2. Los dashboard modes son perfiles, no templates

Los modos útiles encontrados son:

| Modo | Trabajo principal | Qué tiende a ganar prominencia | Riesgo frecuente |
| --- | --- | --- | --- |
| Monitoring | Detectar cambios, riesgos o salud | Estado, tendencia, umbral, freshness | Mostrar estado sin explicar relevancia |
| Operational | Priorizar y ejecutar trabajo repetido | Excepciones, cola, status, acción próxima | Baja densidad que obliga a navegar demasiado |
| Diagnostic | Explicar por qué cambió algo | Comparaciones, drivers, segmentos, contexto | Drill-down infinito sin hipótesis |
| Exploratory | Formular y contrastar preguntas | Controles flexibles, historial, múltiples vistas | Filtros y posibilidades sin orientación |
| Executive | Comprender situación y decidir dirección | Outcomes, cambios materiales, riesgos, decisión | “KPI wall” o detalle operativo excesivo |
| Hybrid | Combinar tareas reales compatibles | Zonas o vistas con responsabilidades claras | Mezclar todos los modos en una sola superficie |

Clasificar ayuda cuando cambia jerarquía, densidad o interacción. No debe forzarse una etiqueta si el caso es simple o si varios modos pueden separarse claramente por vista.

### 3. El contrato analítico es un input, no una excusa para inventar KPIs

`dashboard-ux` puede recibir de `product-analytics` audiencia, decisiones, métricas priorizadas, roles, definiciones, comparaciones, dimensiones, cadence/freshness, guardrails y gaps.

Esos campos cumplen funciones distintas:

- **directamente consumibles:** audiencia, decisiones, métricas, roles, definiciones y gaps;
- **requieren adaptación UX:** prioridad, comparación, dimensiones, cadence/freshness y guardrails;
- **generan preguntas si faltan:** audiencia decisora, acción, significado de la métrica, comparison anchor, tolerancia a stale data y permisos.

La skill puede aclarar el significado necesario para representar una métrica, pero no debe reconstruir una estrategia completa de medición. Si la ausencia cambia qué se mostraría, debe solicitar definición analítica o activar `product-analytics` primero.

### 4. Prominencia significa prioridad de decisión

Las fuentes suelen reducir prominencia a tamaño o posición. La síntesis más portable es separar **por qué** algo merece atención de **cómo** se materializará visualmente.

Un elemento puede ganar prominencia por:

- proximidad a una decisión principal;
- urgencia o coste de no actuar;
- magnitud o materialidad del cambio;
- rol como outcome o guardrail crítico;
- necesidad de comparación inmediata;
- frecuencia de consulta;
- confianza y calidad suficiente para actuar.

Popularidad, disponibilidad o simetría visual no justifican prominencia. Tampoco toda métrica priorizada debe convertirse en una card idéntica.

### 5. Overview y detail son responsabilidades distintas

Overview no significa “todos los datos comprimidos”. Debe permitir orientación rápida: alcance, estado, cambios materiales, contexto de comparación y puntos de entrada al diagnóstico o la acción.

Detail debe responder preguntas que el overview plantea, preservando:

- contexto de filtros y comparación;
- identidad de la métrica o entidad;
- camino de regreso y posibilidad de reset;
- distinción entre detalle complementario y otra tarea completa.

Drill-down, panel lateral, expansión inline, pestaña o navegación a otra vista son alternativas con costes diferentes. El patrón debe elegirse por continuidad de contexto, profundidad, espacio necesario, frecuencia y riesgo de desorientación.

### 6. Comparar es una necesidad semántica y una decisión de UX

`product-analytics` decide qué comparación es válida; `dashboard-ux` decide cómo conservarla y hacerla legible.

Cada comparación visible debe hacer recuperables:

- medida y unidad;
- población o segmento;
- período o ventana;
- ancla —target, período previo, baseline, benchmark, cohorte o actor—;
- dirección y magnitud;
- limitaciones o freshness relevantes.

Cuando hay múltiples anclas, la interfaz debe priorizar la que responde la decisión principal y relegar las demás a contexto o exploración. Mostrar todas simultáneamente puede destruir la comparación que se quería facilitar.

### 7. La densidad depende del ritmo y del coste de interacción

“Menos es mejor” falla en operación: ocultar status, excepciones o acciones frecuentes puede aumentar tiempo y errores. “Más datos es mejor” falla en vistas ejecutivas: reduce jerarquía y obliga a interpretar ruido.

La densidad adecuada depende de:

- experiencia de la audiencia;
- frecuencia y duración de uso;
- número de decisiones simultáneas;
- necesidad de scanability versus lectura profunda;
- coste de abrir detalle repetidamente;
- tamaño y distancia del dispositivo;
- consecuencias de omitir información.

Una vista puede ser densa y clara si mantiene agrupación, alineación, consistencia y señal de excepción. Puede ser escasa y confusa si desperdicia espacio en elementos decorativos o fuerza navegación para tareas frecuentes.

### 8. Toda interacción debe pagar su coste cognitivo

Los patrones estudiados forman un repertorio, no un checklist:

- **filters:** limitar población o contexto; deben tener alcance, defaults, persistencia y reset claros;
- **drill-down:** profundizar una relación jerárquica;
- **cross-filtering:** coordinar vistas, con estado visible y reversible;
- **tabs:** separar modos o perspectivas pares, no ocultar contenido crítico;
- **drawers:** conservar contexto mientras se consulta detalle medio;
- **modals:** reservar para decisiones o foco temporal, no navegación analítica profunda;
- **inline expansion:** revelar detalle local sin perder posición;
- **hover:** aportar complemento, nunca ser el único acceso a información esencial;
- **selection:** sostener comparación o acción, con estado perceptible;
- **search:** localizar entidades cuando navegar o filtrar sería costoso.

Una interacción se justifica cuando reduce complejidad o acerca una decisión más de lo que añade memoria, pasos o riesgo de estado oculto.

### 9. Los estados son parte del significado del dashboard

“No hay un número” puede significar situaciones materialmente distintas:

- loading;
- empty por primera configuración;
- no-data legítimo para el período;
- no-results después de filtros o búsqueda;
- error;
- stale data;
- partial data;
- permission-limited data;
- anomalía o cambio material.

Cada estado debe comunicar, según corresponda: qué ocurre, qué alcance afecta, qué tan confiable es lo visible, qué acción existe y qué contenido previo puede conservarse. No se debe presentar cero, vacío y error como equivalentes.

### 10. Accesibilidad y responsive behavior preservan la jerarquía

La accesibilidad no se resuelve solo con una paleta. El contrato UX debe exigir:

- todas las funciones disponibles por teclado;
- orden de foco y lectura significativo;
- foco visible y no oculto;
- labels y nombres comprensibles;
- información no dependiente solo de color;
- contraste suficiente para texto, controles y objetos gráficos relevantes;
- equivalentes textuales o tabulares cuando un gráfico porta información compleja;
- hover y gestos con alternativas;
- announcements apropiados para loading, error y actualización;
- jerarquía responsive que preserve decisión y contexto, no mero reflow mecánico.

En pantallas pequeñas puede cambiar el orden, la forma de acceso y el nivel inicial de detalle. Lo primario debe seguir siendo primario; contenido crítico no debe desaparecer por falta de espacio.

## Comparison

### Coincidencias

- Empezar por audiencia, propósito o tarea antes de elegir layout.
- Separar síntesis de detalle y ofrecer exploración bajo demanda.
- Mantener comparación, freshness y contexto junto a la información.
- Reducir contenido sin decisión o acción asociada.
- Tratar accesibilidad y responsive behavior como calidad, no adorno.
- Evitar dashboards genéricos formados por cards equivalentes.

### Diferencias

- Algunas fuentes fuerzan una North Star y cantidades fijas; otras parten de una persona y una tarea sin arquitectura métrica.
- Las implementaciones data-viz privilegian encodings y chart selection; las de UI privilegian estética, tokens y código.
- Los enfoques ejecutivos premian síntesis; los operativos requieren densidad, status y acciones frecuentes.
- Algunas fuentes usan progressive disclosure como organización de conocimiento; otras como patrón de interfaz. `dashboard-ux` necesita ambos conceptos separados.

### Fortalezas por enfoque

- **Dashboard-specific:** ofrece vocabulario de audience, cadence, hierarchy y drill-down.
- **Interface-design:** aporta intencionalidad, task fit y rechazo de patrones arbitrarios.
- **Data visualization:** aporta comparación perceptiva, overview/detail y límites del color.
- **Standards y design systems:** aportan accessibility y estados verificables.

### Debilidades recurrentes

- Mezclar qué medir con cómo presentarlo.
- Convertir heurísticas en números universales de KPIs, charts o colores.
- Suponer que top-left, cards o grillas simétricas son siempre correctos.
- Tratar “real-time” como superior sin relación con cadence de decisión.
- Usar chart recipes en lugar de necesidades de comparación.
- Omitir estados parciales, stale y permission-limited.
- Reducir accessibility a contraste o color blindness.
- Incluir implementación y tooling dentro del contrato conceptual.

### Solapamientos

| Área | Solapamiento observado | Límite propuesto |
| --- | --- | --- |
| `product-analytics` | KPIs, targets, funnels, guardrails | Recibir contrato; preguntar o derivar si falta. No definir estrategia métrica completa. |
| Data visualization | Encodings, chart types, legends | Expresar necesidad de representación y comparación; derivar selección especializada cuando requiera expertise de visualización. |
| Frontend implementation | Responsive, controls, loading, focus | Especificar comportamiento y requisitos; no escribir React/CSS ni elegir librerías. |
| Design system | Tokens, componentes, patrones existentes | Consumir restricciones; no crear branding ni un sistema visual completo. |
| Accessibility review | Requisitos y checks especializados | Incluir requisitos base; derivar auditoría formal o remediación técnica. |

## Boundaries

### Con `product-analytics`

`product-analytics` define qué medir, por qué, con qué unidad, comparación y decisión. `dashboard-ux` decide orden, prominencia, agrupación, exploración, estados e interacción para ese contenido.

Puede avanzar con supuestos mínimos cuando el inventario está claro y solo faltan detalles que no cambian la estructura. Debe detener o derivar cuando falten decisiones, métricas o definiciones que produzcan layouts materialmente distintos.

### Con data visualization

Puede recomendar familias de representación a nivel de necesidad —tendencia, ranking, distribución, relación, composición o detalle tabular— cuando eso aclara la UX. No debe convertirse en un catálogo de charts, reglas de encoding exhaustivas ni implementación gráfica.

### Con frontend implementation

Debe producir especificaciones de estructura, comportamiento, estados, responsive y accesibilidad. No debe elegir frameworks, componentes concretos, librerías, CSS, rendering technology ni código.

### Con design systems

Puede consumir componentes, tokens y restricciones existentes y señalar gaps. No debe definir identidad de marca, tipografía, paleta completa o component API como problema principal.

### Con accessibility review

Debe incluir requisitos preventivos observables. Una auditoría de conformidad, test con assistive technology o reparación de código pertenece a una capacidad especializada.

## Anti-patterns detected

- **KPI wall:** todos los números compiten con igual peso.
- **Card soup:** el contenedor card sustituye agrupación y jerarquía.
- **Chart zoo:** variedad de gráficos sin gramática ni necesidad distinta.
- **Decorative visualization:** complejidad visual que no mejora comprensión.
- **Excessive color:** demasiados significados o color usado como decoración.
- **Excessive filters:** controles dominan la vista y exponen el modelo de datos.
- **Hidden comparison context:** valor o tendencia sin ancla, período o población visible.
- **Ambiguous units:** número sin unidad, denominador, alcance o freshness recuperable.
- **Dashboard without audience:** una vista intenta servir a todos.
- **Dashboard without decisions:** contenido disponible pero no accionable.
- **Excessive drill-down:** profundidad que fragmenta el diagnóstico y pierde contexto.
- **Modal navigation:** análisis profundo dentro de overlays difíciles de orientar o enlazar.
- **Everything above the fold:** comprimir por dogma en lugar de priorizar y permitir recorrido.
- **Forced symmetry:** igualar tamaños o cantidades aunque la importancia sea desigual.
- **Hierarchy unrelated to importance:** tamaño, color o posición responden a estética y no a decisión.
- **Real-time by default:** freshness más rápida que la capacidad o necesidad de actuar.
- **Zero equals no data:** representar ausencia, error o permiso como valor válido.
- **Hover-only meaning:** ocultar definición o valores esenciales a teclado, touch o assistive tech.
- **Responsive disappearance:** eliminar contexto crítico para hacer caber la vista.

## Proposed methodology

### 1. Encauzar el pedido y confirmar el contrato

Identificar si el problema es UX, analytics, visualization especializada o implementación. Confirmar audiencia, decisiones y métricas existentes. Avanzar con supuestos explícitos solo si son reversibles y no obligan a inventar estrategia métrica.

### 2. Encuadrar audiencia, tareas y contexto de uso

Describir quién usa el dashboard, qué necesita detectar o decidir, qué acciones puede tomar, con qué frecuencia, bajo qué presión temporal y en qué dispositivos o entorno.

### 3. Identificar el modo dominante

Clasificar como monitoring, operational, diagnostic, exploratory, executive o hybrid solo cuando la clasificación cambie el diseño. Separar vistas o zonas si un híbrido mezcla ritmos y tareas incompatibles.

### 4. Traducir el contrato analítico a prioridades UX

Relacionar cada elemento con una decisión, acción, riesgo o explicación. Asignar prioridad primaria, secundaria o bajo demanda. No usar el rol métrico como único criterio: urgencia, materialidad y coste de omisión también importan.

### 5. Construir la arquitectura de información

Definir secciones, orden y relaciones. Hacer que el overview oriente; que el contexto explique; y que el detail permita actuar o diagnosticar. Evitar llenar espacios por simetría.

### 6. Diseñar el modelo de comparación

Preservar ancla, ventana, unidad, población y dirección. Resolver qué comparación debe verse de inmediato y cuáles quedan bajo interacción. Señalar gaps sin inventarlos.

### 7. Diseñar navegación y exploración

Elegir filtros, selección, drill-down, cross-filtering, tabs, drawers, expansión, hover o búsqueda solo cuando reducen trabajo. Definir alcance, persistencia, reset, deep-linking y camino de regreso cuando sean relevantes.

### 8. Definir estados y feedback

Especificar loading, empty, no-data, no-results, error, stale, partial, permission-limited y anomalous según el caso. Para cada estado, aclarar significado, alcance, confianza y acción disponible.

### 9. Ajustar densidad y responsive hierarchy

Calibrar densidad por experiencia, frecuencia, decisiones simultáneas, dispositivo y coste de navegación. En responsive, preservar prioridad y contexto; cambiar composición o patrón de detalle cuando sea necesario.

### 10. Aplicar accessibility requirements

Comprobar keyboard access, focus, reading order, labels, non-color encoding, contrast, alternativas textuales/tabulares y acceso equivalente a interacciones.

### 11. Validar soporte a decisiones

Revisar si una persona puede orientarse, detectar lo importante, comprender la comparación, llegar al detalle y decidir o actuar sin ambigüedad innecesaria. Eliminar todo elemento o interacción sin propósito.

El workflow debe comprimirse en pedidos acotados; no es obligatorio producir doce secciones ni completar un template exhaustivo.

## Proposed progressive disclosure

La investigación justifica cuatro referencias conceptuales futuras, no cinco:

| Referencia propuesta | Responsabilidad | Motivo de agrupación |
| --- | --- | --- |
| `modes-and-information-hierarchy.md` | Modos, prioridad, agrupación, densidad y overview/detail | Modo, jerarquía y densidad se deciden juntos; separarlos duplicaría criterios. |
| `exploration-and-comparison.md` | Comparaciones, filtros, navegación, drill-down y details-on-demand | La interacción existe para explorar relaciones y comparaciones; un catálogo aislado sería mecánico. |
| `states-and-feedback.md` | Loading, empty, no-data, no-results, error, stale, partial, permissions y anomaly | Tiene taxonomía y decisiones propias, consultables cuando el dashboard depende de datos dinámicos. |
| `accessibility-and-responsive.md` | Keyboard, focus, contrast, non-color, labels, chart alternatives y jerarquía responsive | Son constraints transversales que deben coordinarse para preservar acceso y prioridad. |

En `SKILL.md` deben permanecer propósito, activación, boundaries, input gate, workflow resumido, output, quality gates y routing directo. La implementación posterior materializa estas referencias sin convertirlas en catálogos ni duplicar el entrypoint.

## Open decisions

1. Definir si la recomendación de familias de representación queda dentro de `dashboard-ux` o requiere una futura skill `data-visualization` para cualquier elección de chart.
2. Validar con casos reales cuándo un hybrid dashboard debe separarse en vistas y cuándo puede convivir por zonas.
3. Determinar el mínimo de información de freshness y data quality que debe estar siempre visible.
4. Probar si el output contract necesita una tabla canónica o si una estructura flexible produce mejores respuestas.
5. Validar el handoff completo desde `product-analytics` sin acoplar ambas skills en tiempo de ejecución.
6. Realizar evaluación conductual independiente y forward testing antes de considerar la skill para Stable.
