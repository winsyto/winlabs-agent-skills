# Fuentes de investigación

Registro de trazabilidad para material externo consultado al diseñar las skills. No copiar contenido de terceros: documentar la fuente, sintetizar solo lo necesario y revisar su licencia o condiciones de uso.

## Cómo registrar una fuente

Para cada fuente futura, anotar:

- título, autor u organización y URL;
- fecha de consulta;
- skill o decisión a la que informa;
- síntesis de los hallazgos relevantes;
- licencia o restricciones conocidas;
- estado de revisión (pendiente, aceptada o descartada).

## Fuentes

### `product-analytics`

#### Product Analytics — `alirezarezvani/claude-skills`

- **Repositorio / autor:** Alireza Rezvani, `alirezarezvani/claude-skills`.
- **URL:** <https://github.com/alirezarezvani/claude-skills/blob/main/product-team/skills/product-analytics/SKILL.md>
- **Fecha de consulta:** 2026-08-18.
- **Skill o componente:** `product-analytics`.
- **Conceptos útiles:** métricas adecuadas a la etapa del producto; cohorts y curvas de retención; comparación temporal; owner, target y regla de decisión; acción asociada a cada riesgo u oportunidad.
- **Limitaciones detectadas:** combina definición de métricas con dashboard design y scripts de cálculo; comienza por elegir un framework; contiene recomendaciones numéricas rígidas que no se generalizan a todos los casos.
- **Decisión:** **adaptar** la disciplina de contexto, comparación e interpretación; descartar tooling y diseño de dashboards.
- **Licencia / restricciones:** repositorio bajo MIT. Se utiliza como fuente comparativa; no se copia contenido.

#### Product Analytics — `borghei/Claude-Skills`

- **Repositorio / autor:** Amin Borghei, `borghei/Claude-Skills`.
- **URL:** <https://github.com/borghei/Claude-Skills/blob/main/product-team/product-analytics/SKILL.md>
- **Fecha de consulta:** 2026-08-18.
- **Skill o componente:** `product-analytics`.
- **Conceptos útiles:** decisiones desde datos; value moment; North Star, inputs y guardrails; activación como evidencia de valor; jerarquía de métricas; prueba de actionability; manejo explícito de supuestos.
- **Limitaciones detectadas:** mezcla instrumentación, eventos, scripts, dashboards y análisis de datos con definición conceptual; prescribe una North Star y cardinalidades fijas; algunas interpretaciones de retención son demasiado concluyentes sin contexto.
- **Decisión:** **adaptar** value-to-decision, roles jerárquicos, guardrails y “So what?”; excluir instrumentación y tooling.
- **Licencia / restricciones:** MIT con Commons Clause, que restringe la venta de software cuyo valor derive sustancialmente de la obra. Se sintetizan patrones sin copiar estructura o texto.

#### Metrics Dashboard — `borghei/Claude-Skills`

- **Repositorio / autor:** Amin Borghei, `borghei/Claude-Skills`.
- **URL:** <https://github.com/borghei/Claude-Skills/blob/main/project-management/discovery/metrics-dashboard/SKILL.md>
- **Fecha de consulta:** 2026-08-18.
- **Skill o componente:** `metrics-dashboard`.
- **Conceptos útiles:** separación entre North Star, inputs, guardrails y métricas operativas; comparación, ownership y prueba de acción; rechazo de vanity metrics.
- **Limitaciones detectadas:** su responsabilidad principal incluye arquitectura de dashboard, visualización y cadence; fija cantidades máximas y prescribe representaciones.
- **Decisión:** **adaptar** roles semánticos y disciplina de comparación; **descartar** layout, chart selection y dashboard inventory para `product-analytics`.
- **Licencia / restricciones:** MIT con Commons Clause. Se utiliza solo para comparación conceptual y delimitación.

#### Analytics Strategy — `rampstackco/claude-skills`

- **Repositorio / autor:** RampStack Co., `rampstackco/claude-skills`.
- **URL:** <https://github.com/rampstackco/claude-skills/blob/main/skills/analytics-strategy/SKILL.md>
- **Fecha de consulta:** 2026-08-18.
- **Skill o componente:** `analytics-strategy`.
- **Conceptos útiles:** comenzar por preguntas; conectar medición con decisiones y outcomes; comparaciones y segmentación con propósito; reconocer audiencia y contexto.
- **Limitaciones detectadas:** alcance excesivamente amplio que combina KPIs, tracking, taxonomías de eventos, atribución, dashboards, implementación y governance; presenta North Star y AARRR como estructura general.
- **Decisión:** **incorporar** el enfoque questions-first y **adaptar** la conexión outcome–decision; **descartar** el alcance combinado y la implementación.
- **Licencia / restricciones:** repositorio bajo MIT. Síntesis original sin reproducción textual.

#### Dashboard Designer — `NickCrew/Claude-Cortex`

- **Repositorio / autor:** Nicholas Ferguson / comunidad, `NickCrew/Claude-Cortex`.
- **URL:** <https://github.com/NickCrew/Claude-Cortex/blob/main/skills/dashboard-designer/SKILL.md>
- **Fecha de consulta:** 2026-08-18.
- **Skill o componente:** `dashboard-designer`, revisada únicamente para detectar límites y solapamientos.
- **Conceptos útiles:** audiencia, decisión y acción como prerequisitos; comparabilidad de KPIs; distinción entre contenido y representación.
- **Limitaciones detectadas:** combina selección de métricas con layout, visual hierarchy, color, herramientas BI y chart choice; su activación ante solicitudes genéricas de dashboard invade analytics.
- **Decisión:** **adaptar** solo la frontera de responsabilidades y el criterio de handoff a `dashboard-ux`; descartar recomendaciones visuales y de tooling.
- **Licencia / restricciones:** la skill declara MIT en su frontmatter y el paquete público declara MIT. Uso limitado a análisis de fronteras; no se copia contenido.

#### North Star Metric Resources — Amplitude

- **Organización:** Amplitude.
- **URL:** <https://amplitude.com/north-star-hub>
- **Fecha de consulta:** 2026-08-18.
- **Componente estudiado:** definición y cualidades de una North Star Metric.
- **Conceptos útiles:** relación entre valor percibido por usuarios, capacidad de influencia del equipo y resultados sostenibles; distinción entre una métrica primaria y KPIs de soporte.
- **Limitaciones detectadas:** material de un proveedor de plataforma analytics y marco centrado en una métrica unificadora; no siempre representa bien productos multi-actor o etapas tempranas.
- **Decisión:** **adaptar** sus criterios para evaluar una North Star; descartar su obligatoriedad.
- **Licencia / restricciones:** contenido público sujeto a derechos del sitio; consultado y citado, sin reproducirlo.

#### Measuring the User Experience on a Large Scale — HEART

- **Autores / publicación:** Kerry Rodden, Hilary Hutchinson y Xin Fu; Google Research, Proceedings of CHI 2010, ACM Press.
- **URL:** <https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/>
- **Fecha de consulta:** 2026-08-18.
- **Componente estudiado:** HEART y proceso Goals-Signals-Metrics.
- **Conceptos útiles:** mapear objetivos a señales observables y luego a métricas; categorías de experiencia —happiness, engagement, adoption, retention y task success— como menú contextual; triangulación de medición con otras evidencias.
- **Limitaciones detectadas:** HEART no sustituye objetivos, jerarquía ni outcomes de negocio; completar todas sus categorías produciría métricas innecesarias.
- **Decisión:** **incorporar** Goals-Signals-Metrics como inspiración para la cadena conceptual y **adaptar** HEART solo cuando la calidad de experiencia sea relevante.
- **Licencia / restricciones:** publicación académica de ACM enlazada desde Google Research; usar como referencia con atribución, sin reproducción extensa.

### `dashboard-ux`

No se han incorporado todavía fuentes para diseñar el contrato de `dashboard-ux`. La revisión de `dashboard-designer` anterior solo informa el límite con `product-analytics`.
