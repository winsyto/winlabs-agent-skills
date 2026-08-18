# Instrucciones del repositorio

Estas reglas aplican a todo el árbol del repositorio.

## Propósito y alcance

- Tratar este repositorio como una biblioteca versionada de capacidades especializadas, no como una colección de prompts sueltos.
- Crear skills pequeñas, especializadas y composables; evitar mega-skills y separar creación de revisión cuando sean responsabilidades distintas.
- Mantener el contenido agnóstico respecto del agente y separar conocimiento reutilizable de configuración específica de proyectos consumidores.
- No copiar skills de terceros. Registrar en `research/sources.md` las fuentes externas consultadas y sintetizar el conocimiento respetando sus licencias.
- No introducir nuevas categorías fuera del catálogo o milestone acordado sin una decisión explícita.

## Estructura de una skill

- Usar `.agents/skills/<nombre>/SKILL.md` como entrypoint obligatorio.
- Usar nombres en minúsculas y kebab-case.
- Mantener `SKILL.md` compacto mediante progressive disclosure. Mover detalle durable a `references/`, automatización determinista a `scripts/` y materiales para outputs a `assets/` solamente cuando sean necesarios.
- No crear archivos auxiliares dentro de una skill que no contribuyan directamente a ejecutarla.
- Incluir únicamente `name` y `description` en el frontmatter de `SKILL.md`; la descripción debe indicar propósito y condiciones de activación.
- Definir, al desarrollar una skill, propósito, cuándo usarla, cuándo no usarla, inputs, workflow, output, criterios de calidad y anti-patterns.
- Evitar duplicar información entre `SKILL.md` y `references/`; enlazar cada referencia directamente desde el entrypoint e indicar cuándo leerla.

## Autoría y cambios

- Leer `docs/architecture.md` y `docs/skill-authoring-guide.md` antes de crear o ampliar skills.
- Empezar por ejemplos de uso y límites; diseñar recursos reutilizables después, no antes.
- No agregar dependencias npm, Python ni tooling por conveniencia. Justificar scripts por repetición, fragilidad o necesidad de resultados deterministas.
- Mantener actualizado `docs/skill-catalog.md` cuando cambie el estado, alcance o versión de una skill.
- Registrar cambios orientados al usuario en `CHANGELOG.md` bajo una sección de versión o `Unreleased`.
- Aplicar versionado semántico a releases de la biblioteca. Documentar explícitamente cambios incompatibles en contratos o comportamiento.

## Evals y revisión

- Mantener evals en `evals/<nombre-de-skill>/`, separadas de la implementación.
- Incluir casos positivos, negativos/no activación y escenarios límite antes de declarar estable una skill.
- Evaluar comportamiento observable, calidad del output y cumplimiento de límites; evitar pruebas acopladas a una redacción exacta.
- Ejecutar las validaciones aplicables y revisar enlaces, estructura, frontmatter y ausencia de contenido específico de un proyecto antes de finalizar.
- Considerar autoría y revisión como responsabilidades distintas cuando el riesgo o complejidad lo justifique.

## Calidad documental

- Escribir instrucciones operativas claras, preferentemente en infinitivo o imperativo.
- Distinguir hechos respaldados, decisiones del proyecto y asuntos pendientes.
- Mantener enlaces relativos válidos y no añadir placeholders que parezcan contenido definitivo.