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

#### Dashboard Designer — `NickCrew/Claude-Cortex`

- **Repositorio / autor:** Nicholas Ferguson / comunidad, `NickCrew/Claude-Cortex`.
- **URL:** <https://github.com/NickCrew/Claude-Cortex/blob/main/skills/dashboard-designer/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `dashboard-designer`.
- **Conceptos útiles:** comenzar por audiencia, decisión, frecuencia y acción; separar headline, contexto y detalle; adaptar densidad y profundidad al tipo de dashboard; exigir comparación y definición comprensible.
- **Limitaciones detectadas:** mezcla selección de KPIs, arquitectura de información, color, chart selection, tooling BI y reglas numéricas rígidas; presupone patrones de lectura y posiciones universales.
- **Decisión:** **adaptar** el encuadre audience–decision–action y la separación overview/detail; **descartar** cardinalidades, posiciones, colores y cadencias universales.
- **Licencia / restricciones:** MIT según el repositorio y el frontmatter. Se sintetizan principios; no se copia contenido.

#### UI/UX Pro Max — `nextlevelbuilder/ui-ux-pro-max-skill`

- **Repositorio / autor:** Next Level Builder, `nextlevelbuilder/ui-ux-pro-max-skill`.
- **URL:** <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `ui-ux-pro-max` y su routing hacia guías de UX, charts y stacks.
- **Conceptos útiles:** progressive disclosure por dominio; accesibilidad prioritaria; densidad como variable contextual; estados y feedback; responsive behavior; búsqueda focalizada de guidance en lugar de cargar un catálogo completo.
- **Limitaciones detectadas:** mega-skill orientada también a estilos, tipografía, animación, design systems, chart catalogs y código específico por stack; depende de scripts y datasets propios.
- **Decisión:** **incorporar** el patrón de routing bajo demanda y **adaptar** densidad, accesibilidad y feedback; **descartar** tooling, branding, catálogo visual y recomendaciones de implementación.
- **Licencia / restricciones:** MIT. No se reutilizan datasets, scripts ni redacción.

#### Interface Design — `Dammyjay93/interface-design`

- **Repositorio / autor:** Dammy Jay, `Dammyjay93/interface-design`.
- **URL:** <https://github.com/Dammyjay93/interface-design/blob/main/.claude/skills/interface-design/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `interface-design`.
- **Conceptos útiles:** diseñar desde persona y tarea concreta; hacer visible una jerarquía deliberada; tratar navegación, densidad y estructura como decisiones; reutilizar patrones existentes; verificar estados y accesibilidad.
- **Limitaciones detectadas:** combina dirección estética, design-system architecture, implementación, tokens, motion y QA visual; su ideal de una sola focalización puede ser insuficiente para consolas operativas con varias excepciones simultáneas.
- **Decisión:** **adaptar** el enfoque task-first, la jerarquía intencional y el rechazo de defaults; **descartar** estética, persistencia de design systems y disciplina de código.
- **Licencia / restricciones:** MIT. Uso comparativo sin copiar instrucciones ni ejemplos.

#### Frontend Design — Anthropic

- **Repositorio / organización:** Anthropic, `anthropics/skills`.
- **URL:** <https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `frontend-design` oficial.
- **Conceptos útiles:** vincular decisiones visuales con propósito y audiencia; evitar layouts genéricos; usar estructura solo cuando codifica relaciones reales; tratar responsive behavior y estados como parte del diseño.
- **Limitaciones detectadas:** está orientada a dirección estética e implementación de interfaces completas; no ofrece una metodología analítica específica para dashboards y su foco expresivo no es adecuado como default operativo.
- **Decisión:** **adaptar** intencionalidad y contextualización; **descartar** dirección estética, branding, implementación y búsqueda deliberada de singularidad visual como responsabilidad de `dashboard-ux`.
- **Licencia / restricciones:** Apache License 2.0 en `skills/frontend-design/LICENSE.txt`. Síntesis original sin reproducción.

#### Data Visualization — `NTCoding/claude-skillz`

- **Repositorio / autor:** NTCoding, `NTCoding/claude-skillz`.
- **URL:** <https://github.com/NTCoding/claude-skillz/blob/main/data-visualization/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `data-visualization`.
- **Conceptos útiles:** overview, filter y details-on-demand; elección de encodings según la tarea; interacción coordinada; evitar depender solo del color; separar contexto general de detalle.
- **Limitaciones detectadas:** combina percepción, chart selection, algoritmos de layout, librerías y umbrales de renderizado; la amplitud atrae pedidos de implementación ajenos a dashboard UX.
- **Decisión:** **adaptar** la progresión overview→focus→detail y los criterios de accesibilidad; **derivar** selección exhaustiva de gráficos y **descartar** librerías, algoritmos y código.
- **Licencia / restricciones:** no se identificó un archivo de licencia en la ruta consultada. Se usa únicamente como fuente pública comparativa, sin reutilización textual o de código.

#### KPI Dashboard Design — `alexander-kastil/skills-collection`

- **Repositorio / autor:** Alexander Kastil, `alexander-kastil/skills-collection`; la colección atribuye la implementación disponible a `wshobson/agents`.
- **URL:** <https://github.com/alexander-kastil/skills-collection/blob/master/CATALOG.md> y <https://github.com/wshobson/agents/blob/main/plugins/business-analytics/skills/kpi-dashboard-design/SKILL.md>.
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `kpi-dashboard-design`.
- **Conceptos útiles:** distinguir niveles estratégico, táctico y operativo; mostrar comparación, tendencia, target o alerta; permitir drill-down; relacionar freshness con ritmo de decisión; mantener visible la metodología de una métrica.
- **Limitaciones detectadas:** combina metric selection, SQL, troubleshooting de datos, infraestructura, thresholds y visualización; prescribe cantidades, colores y patrones por defecto que no son universales.
- **Decisión:** **adaptar** niveles, contexto y drill-down; **descartar** definición de KPI, SQL, pipelines, thresholds automáticos y reglas visuales rígidas.
- **Licencia / restricciones:** la colección declara MIT y el upstream `wshobson/agents` también declara MIT. Se conserva la atribución de procedencia y no se copia contenido.

#### Metrics Dashboard — `borghei/Claude-Skills`

- **Repositorio / autor:** Amin Borghei, `borghei/Claude-Skills`.
- **URL:** <https://github.com/borghei/Claude-Skills/blob/main/project-management/discovery/metrics-dashboard/SKILL.md>
- **Fecha de consulta:** 2026-09-09.
- **Skill o componente:** `metrics-dashboard`, revisada para delimitar solapamientos.
- **Conceptos útiles:** audiencia, owner y cadence; jerarquía; comparison anchor; poda de contenido no usado; distinción entre vistas ejecutivas y operativas.
- **Limitaciones detectadas:** fuerza North Star y cardinalidades, incorpora instrumentación, define KPIs y charts, ejecuta scripts y mezcla gobierno métrico con UX.
- **Decisión:** **adaptar** poda, audience fit y comparison context; **descartar** arquitectura métrica prescriptiva, tooling, selección de KPIs y chart recipes.
- **Licencia / restricciones:** MIT con Commons Clause. Uso limitado a comparación y delimitación; no se reproduce estructura ni texto.

#### The Eyes Have It — Ben Shneiderman

- **Autor / publicación:** Ben Shneiderman, IEEE Symposium on Visual Languages, 1996.
- **URL:** <https://hci.stanford.edu/courses/cs448b/papers/shneiderman96eyes.pdf>
- **Fecha de consulta:** 2026-09-09.
- **Componente estudiado:** taxonomía de tareas de visual information seeking.
- **Conceptos útiles:** overview, zoom, filter, details-on-demand, relate, history y extract como repertorio de tareas, no como secuencia obligatoria para todo dashboard.
- **Limitaciones detectadas:** marco general de information visualization anterior a patrones web actuales; no resuelve priorización, estados, accesibilidad ni diferencias entre dashboards ejecutivos y operativos.
- **Decisión:** **adaptar** overview→focus→detail y conservar history/reset cuando la exploración lo requiera.
- **Licencia / restricciones:** publicación académica bajo derechos de IEEE; se cita y parafrasea sin reproducción extensa.

#### Web Content Accessibility Guidelines 2.2 y tutoriales — W3C WAI

- **Organización:** World Wide Web Consortium, Web Accessibility Initiative.
- **URL:** <https://www.w3.org/TR/WCAG22/>, <https://www.w3.org/WAI/tutorials/images/complex/> y <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color>.
- **Fecha de consulta:** 2026-09-09.
- **Componente estudiado:** keyboard access, focus, contrast, non-color encoding y alternativas para gráficos complejos.
- **Conceptos útiles:** funcionalidad operable por teclado; orden y foco significativos; color acompañado por texto, forma o patrón; contraste; labels y descripciones textuales equivalentes para información visual compleja.
- **Limitaciones detectadas:** define requisitos de accesibilidad, no una metodología completa de dashboard UX ni reglas de prominencia o densidad.
- **Decisión:** **incorporar** como quality gates y requisitos del handoff a implementación.
- **Licencia / restricciones:** estándares y material W3C sujetos a sus políticas de documentos y licencias. Referencia normativa; no se copia contenido extenso.

#### Loading y Empty States — Carbon Design System

- **Organización:** IBM, Carbon Design System.
- **URL:** <https://carbondesignsystem.com/components/loading/usage/> y <https://preview.carbondesignsystem.com/building-blocks/core/patterns/empty-states>.
- **Fecha de consulta:** 2026-09-09.
- **Componente estudiado:** feedback de carga, progressive loading y variantes de empty/error state.
- **Conceptos útiles:** diferenciar carga global y localizada; conservar estructura durante la carga; distinguir ausencia real, falta de resultados, permisos, configuración y error; ofrecer explicación y siguiente acción contextual.
- **Limitaciones detectadas:** guidance ligada a un design system y componentes concretos; no cubre freshness, datos parciales o anomalías como sistema completo.
- **Decisión:** **adaptar** la taxonomía de estados y el principio explicación→impacto→acción; **descartar** prescripciones de componentes.
- **Licencia / restricciones:** documentación pública de IBM Carbon; uso como referencia con atribución, sin copiar componentes o redacción.

#### Progressive Disclosure — Nielsen Norman Group

- **Organización / autor:** Nielsen Norman Group, Jakob Nielsen.
- **URL:** <https://www.nngroup.com/articles/progressive-disclosure/>
- **Fecha de consulta:** 2026-09-09.
- **Componente estudiado:** deferir opciones y contenido secundarios sin volverlos indescubribles.
- **Conceptos útiles:** mantener lo esencial en la vista primaria y trasladar complejidad secundaria a niveles accesibles; verificar que el acceso al detalle sea comprensible y reversible.
- **Limitaciones detectadas:** principio general de interaction design, no específico de dashboards ni suficiente para decidir qué información es analíticamente importante.
- **Decisión:** **incorporar** como criterio de overview/detail y discoverability, subordinado a audiencia y tarea.
- **Licencia / restricciones:** contenido público sujeto a derechos del sitio; solo se cita y sintetiza.
