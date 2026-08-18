---
name: product-analytics
description: Definir y organizar métricas de producto para apoyar decisiones de negocio o producto, incluyendo outcomes, drivers, guardrails, funnels, adopción, retención e interpretación. Usar al seleccionar o revisar KPIs, jerarquías o lógica de medición; no usar para diseño visual de dashboards, gráficos, SQL, instrumentación analytics, modelos físicos de datos ni implementación frontend.
---

# Product Analytics

## Propósito

Definir qué medir, por qué medirlo y cómo interpretar los resultados para apoyar decisiones de producto o negocio. Producir un sistema de medición pequeño y razonado, no una lista genérica de KPIs ni una solución de BI.

## Usar cuando

- Definir o revisar métricas para un producto, feature, módulo o workflow.
- Construir una jerarquía entre outcomes, drivers, diagnósticos y guardrails.
- Definir un funnel, activation, adoption, engagement, retention o cohorts.
- Analizar si las métricas existentes son relevantes, comparables y accionables.
- Determinar qué contenido métrico necesita un dashboard antes de diseñarlo.
- Interpretar movimientos de métricas y vincularlos con decisiones o investigaciones.

## No usar cuando

- Las métricas ya están acordadas y el pedido es layout, jerarquía visual, interacción o componentes: derivar a `dashboard-ux`.
- El pedido es implementar charts, frontend o estilos: derivar a una capacidad de implementación.
- El pedido es escribir SQL, transformar datos o calcular resultados sobre datasets.
- El pedido es diseñar tracking, eventos, propiedades o configurar herramientas analytics.
- El pedido es crear schemas físicos, modelos de warehouse, semantic layers o pipelines.
- El pedido requiere diseñar experimentos o demostrar causalidad: entregar la definición métrica y derivar la inferencia.

Ante “Necesito un dashboard”, aclarar primero qué decisión debe apoyar y si las métricas ya existen. Aplicar esta skill solo si falta definir o revisar el contenido semántico. En pedidos mixtos, completar esa parte y explicitar el handoff; no asumir permiso para implementar lo demás.

## Inputs

Obtener como mínimo, aunque sea de forma provisional:

- objetivo y alcance;
- producto, feature o workflow;
- actor o población principal;
- pregunta o decisión que la medición debe apoyar.

Usar cuando estén disponibles: mecanismo de valor y modelo de negocio, etapa del producto, actores secundarios, métricas actuales, horizonte de decisión, riesgos, datos, baselines, targets y segmentos.

Si falta contexto:

1. Preguntar solo por faltantes que podrían cambiar materialmente la recomendación, priorizando objetivo, actor, valor y decisión.
2. Si el usuario prefiere avanzar, declarar supuestos y producir una propuesta provisional.
3. No inventar targets, benchmarks, baselines, disponibilidad de datos ni relaciones causales.
4. Marcar las definiciones y relaciones que requieren validación.

## Workflow central

1. **Encuadrar objetivo y alcance.** Precisar resultado buscado, problema, etapa y horizonte; separar hechos, supuestos y preguntas abiertas.
2. **Identificar actores, valor y unidad.** Determinar quién recibe valor, quién decide y si la unidad es usuario, cuenta, equipo, caso, transacción u otra. Representar varios actores cuando sus outcomes puedan entrar en tensión.
3. **Formular decisiones.** Expresar qué elección o investigación cambiaría según el resultado. Cuestionar métricas sin una decisión u observación útil asociada.
4. **Definir outcomes.** Describir cambios observables de valor o negocio. Evaluar una North Star solo si encaja; no forzar una métrica única.
5. **Construir una jerarquía mínima.** Relacionar outcomes con drivers plausibles, diagnósticos necesarios y guardrails proporcionales. Tratar la jerarquía como hipótesis, no como causalidad demostrada.
6. **Definir las métricas.** Aplicar la regla de definición siguiente a cada métrica principal y resolver población, unidad, ventana y denominadores relevantes.
7. **Agregar análisis diagnóstico bajo condición.** Usar funnels, lifecycle concepts, cohorts y dimensiones solo si ayudan a explicar una diferencia o tomar una decisión.
8. **Establecer contexto de comparación.** Elegir período, baseline, target, cohorte, segmento o benchmark defendible. Registrar como gap lo que no exista.
9. **Revisar guardrails y gaming.** Preguntar qué podría empeorar o manipularse aunque una métrica principal mejore.
10. **Interpretar y proponer acciones.** Separar observación, hipótesis, explicaciones alternativas, evidencia faltante y siguiente acción; no afirmar causalidad sin soporte.
11. **Validar utilidad.** Eliminar redundancia, vanity metrics y complejidad que no mejore decisiones.

## Regla de definición de métricas

Hacer recuperables, de forma proporcional al pedido:

- **What:** qué fenómeno mide, para qué población, unidad y ventana.
- **Why:** por qué representa un objetivo, outcome, driver o riesgo relevante.
- **How:** cómo se calcula conceptualmente, incluidas reglas de inclusión, exclusión y denominadores.
- **Compared to what:** qué referencia permite interpretarla.
- **So what:** qué decisión, diagnóstico, acción o investigación habilita.

Usar **So what** como gate central. Cuestionar una métrica si un movimiento material no cambiaría ninguna observación, decisión o acción.

## Referencias bajo demanda

Leer únicamente las referencias necesarias para el pedido:

- Para diseñar o revisar outcomes, North Star, drivers, diagnósticos, guardrails o metric trees, leer [references/metric-hierarchy.md](references/metric-hierarchy.md).
- Para especificar o auditar definiciones, unidades, poblaciones, ventanas, comparaciones o targets, leer [references/metric-definition.md](references/metric-definition.md).
- Para funnels, conversion, activation, adoption, engagement, retention o cohorts, leer [references/lifecycle-analysis.md](references/lifecycle-analysis.md).
- Para segmentation, diagnóstico, comparación, hipótesis, causalidad, confianza y acciones, leer [references/interpretation-and-diagnostics.md](references/interpretation-and-diagnostics.md).

No cargar todas por defecto ni usar sus conceptos como checklist obligatorio.

## Output

Adaptar la profundidad y estructura al problema. Una consulta acotada puede resolverse con pocas definiciones; una estrategia amplia puede incluir:

- contexto, alcance y supuestos;
- actores, unidad y decisiones a soportar;
- outcomes y jerarquía métrica;
- definiciones con What / Why / How / Compared to what / So what;
- diagnósticos, dimensiones y comparaciones pertinentes;
- guardrails y riesgos;
- interpretación, acciones y evidencia adicional;
- gaps de definición, targets o datos.

Usar árbol, tabla o narrativa según mejore la comprensión. No forzar una plantilla exhaustiva.

## Handoff a `dashboard-ux`

Entregar, cuando corresponda: audiencia, decisiones, métricas priorizadas y sus roles, definiciones, comparaciones, dimensiones necesarias, cadence o freshness conocida, guardrails y gaps.

No incluir layout, chart types, componentes, colores ni detalles de implementación.

## Quality gates

Antes de finalizar, comprobar:

- [ ] Cada métrica principal tiene propósito y un **So what** defendible.
- [ ] Actor, población y unidad de análisis están claros.
- [ ] Outcomes, drivers, diagnósticos y guardrails no se confunden.
- [ ] No se forzó una North Star ni se completó un framework por obligación.
- [ ] What, Why, How, Compared to what y So what son recuperables.
- [ ] Denominadores, ventanas e inclusiones relevantes están definidos.
- [ ] No se inventaron targets, baselines o benchmarks.
- [ ] Funnels, cohorts y segmentos tienen una razón diagnóstica.
- [ ] Existen guardrails cuando hay riesgo material o posibilidad de gaming.
- [ ] No quedan métricas redundantes o puramente vanity.
- [ ] Observación, interpretación y causalidad están separadas.
- [ ] El output habilita una decisión o explica qué falta para habilitarla.
- [ ] Supuestos y gaps están explícitos.
- [ ] No se invadieron visualización, SQL, tracking, data modeling o implementación.
