# Arquitectura

## Objetivo

Organizar una biblioteca portable de Agent Skills cuyo contenido pueda evolucionar, evaluarse y consumirse de forma selectiva sin arrastrar configuración propia de un proyecto o agente concreto.

## Capas

1. **Biblioteca (`.agents/skills/`)**: una carpeta autocontenida por capacidad y un `SKILL.md` como entrypoint.
2. **Recursos de skill**: `references/` para conocimiento cargado bajo demanda; `scripts/` para operaciones repetibles y deterministas; `assets/` para materiales incorporados al output. Crear únicamente los recursos necesarios.
3. **Evals (`evals/`)**: especificaciones y fixtures externos a la skill para probar activación, límites y calidad sin contaminar sus instrucciones.
4. **Gobierno (`docs/`, `AGENTS.md`, `CHANGELOG.md`)**: convenciones, inventario, decisiones y evolución de la biblioteca.
5. **Investigación (`research/`)**: trazabilidad de fuentes; no es contenido operativo cargado automáticamente por una skill.

## Progressive disclosure

El frontmatter permite descubrir una skill. Su cuerpo contiene el contrato y workflow esencial. El detalle extenso se consulta mediante enlaces directos a referencias. No duplicar contenido entre niveles ni encadenar referencias innecesariamente.

## Límites de portabilidad

- Evitar rutas, schemas, marcas, credenciales o convenciones de un proyecto consumidor.
- Expresar inputs y outputs en términos neutrales cuando no exista un estándar obligatorio.
- Aislar integraciones específicas en recursos opcionales solo después de acordar su alcance.
- No asumir que todos los agentes soportan metadatos propietarios adicionales a `SKILL.md`.

## Versionado

La biblioteca usa Semantic Versioning. Un cambio en el contrato observable, condiciones de activación o formato requerido puede ser incompatible aunque solo modifique Markdown. Cada release debe actualizar el changelog y el estado del catálogo.

## Flujo de evolución

Propuesta → alcance y ejemplos → contrato → implementación mínima → evals → revisión independiente cuando corresponda → publicación → observación e iteración.

Las decisiones todavía abiertas para `v0.1` se conservan en el [catálogo](skill-catalog.md) y no deben resolverse implícitamente dentro de los esqueletos.