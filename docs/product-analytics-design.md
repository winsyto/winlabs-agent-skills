# Diseño conceptual de `product-analytics`

Estado del documento: especificación previa a `SKILL.md`

Estado de la skill: Esqueleto
Milestone: v0.1 — Analytics & Dashboard Foundation

Base conceptual: [research de `product-analytics`](../research/product-analytics-research.md).

## Purpose

Ayudar a un agente a definir qué medir, por qué medirlo y cómo interpretar los resultados para apoyar decisiones de producto o negocio.

La responsabilidad primaria comprende selección, jerarquía, definición conceptual e interpretación de métricas. La skill debe producir un sistema de medición pequeño y razonado, no una lista genérica de KPIs ni una solución de BI.

## Boundaries

### Resuelve

- traducir objetivos y preguntas en métricas pertinentes;
- identificar outcomes, drivers, diagnósticos y guardrails;
- definir conceptualmente métricas, funnels, conversiones, adopción, engagement, retención o eficiencia cuando aporten valor;
- elegir comparaciones y dimensiones diagnósticas;
- explicar interpretación, límites y decisiones habilitadas;
- identificar gaps de información o datos sin diseñar su implementación.

### No resuelve

- layout, componentes, interacción, jerarquía visual o accesibilidad de dashboards;
- selección o implementación de gráficos;
- SQL, transformación de datos o cálculo sobre datasets;
- tracking plans, taxonomías de eventos o instrumentación;
- configuración de herramientas analytics o BI;
- schemas físicos, modelos de warehouse o semantic layers;
- pipelines de datos, librerías frontend o código de aplicación;
- diseño de experimentos o inferencia causal completa.

Puede señalar que una definición requiere nuevos datos o evidencia causal, pero debe derivar la ejecución a la capacidad correspondiente.

### Frontera con `dashboard-ux`

| Situación | Skill responsable |
| --- | --- |
| Objetivo, decisiones o métricas todavía indefinidos | `product-analytics` primero |
| Métricas acordadas; falta layout, visual hierarchy, interacción o componentes | `dashboard-ux` |
| Solicitud mixta de dashboard desde cero | `product-analytics` y luego handoff a `dashboard-ux` |
| Implementación de gráficos o frontend | Ninguna de estas dos; derivar a implementación |

`product-analytics` puede describir la necesidad analítica —por ejemplo, comparar etapas o observar evolución por cohorte—, pero no elegir la representación visual.

## Activation cases

- “Define KPIs para saber si esta nueva feature mejora la colaboración.”
- “¿Cómo deberíamos medir el funnel de onboarding de este módulo?”
- “Necesito analizar adopción y uso recurrente de una funcionalidad.”
- “Propón las métricas esenciales para este SaaS y explica para qué sirven.”
- “¿Cómo mediríamos retención en un producto que se usa mensualmente?”
- “Construye una jerarquía entre nuestro outcome, drivers y guardrails.”
- “Tenemos estas métricas, pero no sabemos cuáles ayudan a decidir.”
- “Antes de diseñar un dashboard, define qué debería medir para responder estas preguntas.”

## Non-activation cases

- “Implementa estos gráficos en React.”
- “Diseña visualmente un dashboard con sidebar y cards.”
- “Escribe la query SQL para calcular retención.”
- “Corrige el CSS de este chart.”
- “Elige entre Recharts y Chart.js.”
- “Instrumenta estos eventos en Segment.”
- “Diseña el schema físico para analytics.”
- “Configura Mixpanel y crea el tracking plan.”

Si una solicitud contiene una parte conceptual y otra de implementación, aplicar esta skill solo a la primera y explicitar el handoff.

## Inputs

### Required

- objetivo de negocio o producto, aunque sea provisional;
- producto, feature, módulo o workflow bajo análisis;
- actor o población principal;
- al menos una pregunta o decisión que las métricas deben apoyar.

### Useful

- modelo de negocio y mecanismo de valor;
- etapa del producto;
- actores secundarios y posibles tensiones;
- workflow o journey relevante;
- definiciones y métricas existentes;
- cadence de decisión y horizonte temporal;
- riesgos o resultados que no deben degradarse;
- owner o audiencia responsable de revisar y actuar.

### Optional

- eventos, fuentes o datos disponibles;
- baselines históricos;
- targets acordados;
- cohorts o segmentos conocidos;
- benchmarks externos con fuente y población comparable;
- restricciones regulatorias, de privacidad o de coste.

### Cuando falta información

1. Preguntar solo por los datos faltantes que cambiarían materialmente la selección o definición.
2. Priorizar objetivo, actor, valor y decisión sobre detalles técnicos.
3. Si el usuario pide avanzar, formular supuestos explícitos y producir una propuesta provisional.
4. No inventar targets, benchmarks, baselines, causalidad ni disponibilidad de datos.
5. Marcar qué definiciones necesitan validación con stakeholders o evidencia.

## Workflow

### 1. Understand objective and scope

Definir resultado buscado, problema, alcance y horizonte. Distinguir hechos, supuestos y preguntas abiertas.

### 2. Identify actors, value and unit

Identificar receptor de valor, decisor y unidad de análisis. Modelar más de un actor cuando el producto dependa de un intercambio o marketplace.

### 3. Identify decisions

Formular las decisiones o preguntas que cambiarían con evidencia: invertir, iterar, investigar, intervenir, mantener o retirar.

### 4. Define outcomes

Describir cambios observables de valor o resultado. Evaluar si una North Star es apropiada; no forzarla. Mantener separados outcomes de usuario, producto y negocio cuando confundirlos oculte trade-offs.

### 5. Build a minimal metric hierarchy

Relacionar outcomes con:

- drivers o inputs plausibles;
- métricas diagnósticas necesarias;
- guardrails proporcionales a los riesgos.

Tratar el árbol como modelo de hipótesis. No asumir causalidad ni imponer números fijos de métricas.

### 6. Define metrics

Para cada métrica candidata responder:

| Campo | Pregunta |
| --- | --- |
| Nombre y rol | ¿Cómo se llama y qué función cumple en la jerarquía? |
| What | ¿Qué fenómeno mide, para qué población, unidad y ventana? |
| Why | ¿Qué objetivo, outcome o riesgo representa? |
| How | ¿Cómo se calcula conceptualmente? ¿Qué se incluye o excluye? |
| Compared to what | ¿Qué baseline, período, target, cohorte, segmento o benchmark la hace interpretable? |
| So what | ¿Qué observación, decisión, acción o investigación habilita? |

Agregar dirección deseada, cadence, owner y limitaciones solo cuando sean pertinentes.

### 7. Add diagnostic analysis selectively

Elegir dimensiones, funnels, cohorts o lifecycle concepts solo si ayudan a decidir o diagnosticar:

- usar funnels para secuencias ordenadas con población y ventana definidas;
- definir activation por primer valor observable;
- distinguir adoption de engagement;
- definir retention alrededor de comportamiento valioso repetido;
- usar cohorts cuando el tiempo desde un ancla cambie la lectura;
- seleccionar segmentos por hipótesis, no por disponibilidad.

### 8. Add comparisons and targets

Verificar una comparación defendible por métrica. Si no existe target o baseline, registrarlo como gap y proponer establecer uno; no inventarlo. Tratar benchmarks externos con cautela por diferencias de población, definición y producto.

### 9. Identify guardrails and gaming risks

Preguntar qué podría empeorar aunque la métrica principal mejore y cómo podría manipularse. Cubrir calidad, confianza, coste, equidad, seguridad o outcomes de otros actores solo cuando el riesgo sea real.

### 10. Explain interpretation and actions

Distinguir observación, interpretación, explicaciones alternativas, evidencia adicional y siguiente acción. No atribuir causalidad a una tendencia o correlación sin diseño apropiado.

### 11. Validate usefulness

Cuestionar o eliminar métricas que no estén alineadas, sean redundantes, carezcan de comparación, no permitan actuar o agreguen complejidad sin mejorar decisiones. Registrar supuestos, gaps y confianza.

## Output contract

El output debe adaptarse al problema. No todos los casos necesitan todas las secciones ni una tabla extensa.

Una respuesta completa debería poder representar:

1. **Context and assumptions**: objetivo, alcance, actor, unidad de análisis y faltantes relevantes.
2. **Decisions to support**: preguntas o decisiones concretas.
3. **Outcome and hierarchy**: outcomes y relación con drivers, diagnósticos y guardrails.
4. **Metric definitions**: What, Why, How, Compared to what y So what.
5. **Diagnostic approach**: dimensiones, funnel, cohorts u otros análisis pertinentes.
6. **Interpretation and actions**: señales, límites, hipótesis y respuestas posibles.
7. **Open gaps**: definiciones, targets, datos o validaciones pendientes.

La jerarquía puede expresarse como árbol, tabla o narrativa. La tabla de definiciones es recomendable cuando hay varias métricas, pero no obligatoria para una consulta acotada.

### Handoff semántico a `dashboard-ux`

Cuando corresponda continuar con diseño de dashboard, entregar:

- audiencia y decisiones;
- métricas priorizadas y roles;
- definiciones y comparaciones;
- dimensiones o cortes necesarios;
- cadence o freshness requerida si se conoce;
- alertas, guardrails y estados relevantes;
- supuestos y gaps.

No incluir layout, componentes, colores, chart types ni herramientas.

## Quality criteria

Una respuesta de calidad cumple de forma observable:

- cada métrica se vincula con un objetivo, outcome, decisión o riesgo;
- el actor y la unidad de análisis están claros;
- outcomes, drivers, diagnósticos y guardrails no se confunden;
- una North Star se utiliza solo cuando supera criterios explícitos;
- What, Why, How, Compared to what y So what son recuperables para cada métrica principal;
- poblaciones, ventanas y denominadores relevantes están definidos;
- no se inventan targets, benchmarks ni baselines;
- funnels, cohorts y segmentos tienen una razón diagnóstica;
- existen guardrails cuando optimizar podría causar daño o gaming;
- las métricas redundantes o no accionables se eliminan o cuestionan;
- observación, interpretación y causalidad se distinguen;
- el resultado permite decidir o define qué falta para poder hacerlo;
- supuestos, gaps y nivel de confianza están explícitos;
- no invade dashboard UX, SQL, tracking, schemas, tooling ni implementación.

## Anti-patterns

- devolver listas genéricas por industria;
- completar frameworks por obligación;
- forzar una North Star;
- usar registro, login o click como activation sin demostrar valor;
- definir porcentajes sin denominador o ventana;
- mezclar usuarios, cuentas y eventos como si fueran la misma unidad;
- presentar cifras sin comparación;
- elegir dimensiones sin hipótesis ni acción posible;
- confundir actividad con valor;
- optimizar drivers sin outcomes o guardrails;
- atribuir causalidad a correlaciones;
- inventar targets o benchmarks;
- recomendar charts, layouts, SQL, eventos o herramientas;
- convertir un gap de datos en un tracking plan no solicitado;
- producir un dashboard como sustituto del razonamiento analítico.

## Progressive disclosure

### Debe permanecer en `SKILL.md`

- propósito y frontera de responsabilidad;
- señales principales de activación y no activación;
- inputs mínimos y manejo de faltantes;
- workflow esencial;
- principio What / Why / How / Compared to what / So what;
- output flexible y criterios de calidad principales;
- routing directo a referencias condicionales.

### Arquitectura propuesta de referencias

No crear referencias hasta implementar el contrato operativo de `SKILL.md`. Cuando se haga, se propone comenzar con cuatro archivos, cada uno con una responsabilidad concreta:

| Archivo propuesto | Responsabilidad | Leer cuando |
| --- | --- | --- |
| `metric-hierarchy.md` | Elegir entre outcomes, North Star opcional, drivers, diagnósticos y guardrails; construir árboles sin asumir causalidad. | Se deba diseñar o revisar una jerarquía. |
| `metric-definition.md` | Especificar población, unidad, ventana, cálculo conceptual, comparación, targets y criterio “So what?”. | Se deban definir o auditar métricas. |
| `lifecycle-analysis.md` | Delimitar activation, adoption, engagement, retention, funnels y cohorts, con casos donde no aplican. | El problema involucre recorrido o comportamiento a través del tiempo. |
| `interpretation-and-diagnostics.md` | Elegir dimensiones, interpretar movimientos, formular hipótesis, guardrails y acciones sin falsa causalidad. | Se deban diagnosticar resultados o proponer acciones. |

### Archivos descartados de la hipótesis inicial

- `funnels-and-conversion.md` y `retention-and-cohorts.md` se combinan en `lifecycle-analysis.md`: ambos dependen de anclas, poblaciones, ventanas y comportamiento temporal, y por separado serían demasiado pequeños o repetitivos.
- `guardrails-and-diagnostics.md` se integra en `interpretation-and-diagnostics.md`: los guardrails son parte de la lectura de tensiones y riesgos, no un modo aislado.
- `anti-patterns.md` no se crea inicialmente: los anti-patterns esenciales deben estar en `SKILL.md` o en la referencia donde se aplica la corrección, evitando un catálogo duplicado.

No se justifican scripts ni assets para esta skill conceptual. Los evals permanecen fuera de la skill.

## Compatibility target

| Entorno | Objetivo |
| --- | --- |
| Codex | Primary |
| Claude Code | Compatible target |
| Otros agentes con Agent Skills | Best effort |

El contrato debe usar Markdown, frontmatter mínimo con `name` y `description`, enlaces relativos y lenguaje agnóstico. No debe depender de tools, metadata ni mecanismos propietarios.

## Open decisions before implementation

1. Definir si owner y cadence son recomendados o condicionalmente requeridos.
2. Validar con evals si la tabla de definición mejora claridad sin rigidizar respuestas breves.
3. Acordar cómo expresar confianza o madurez de las relaciones outcome–driver.
4. Definir el proceso recomendado para establecer targets cuando solo existe una baseline.
5. Confirmar el handoff con el futuro contrato de `dashboard-ux`.
6. Probar activación y comportamiento en Codex y Claude Code antes de cambiar el estado a `Experimental`.
