# winlabs-agent-skills

Biblioteca versionada y reutilizable de Agent Skills para agentes de desarrollo de software compatibles con el estándar Agent Skills.

> **Estado:** fundación inicial de `v0.1 — Analytics & Dashboard Foundation`. Las skills incluidas son esqueletos y todavía no contienen orientación conceptual definitiva.

## Objetivos

- Construir capacidades pequeñas, especializadas y composables.
- Mantener el conocimiento reutilizable separado de la configuración de cada proyecto consumidor.
- Favorecer compatibilidad entre agentes mediante `SKILL.md` como punto de entrada.
- Validar el comportamiento mediante evals versionadas junto a cada skill.

## Estructura

```text
.agents/skills/   Skills publicadas y sus recursos bajo demanda
docs/             Arquitectura, guía de autoría y catálogo
evals/            Casos de evaluación organizados por skill
research/         Registro de fuentes externas evaluadas
```

Consultar [la arquitectura](docs/architecture.md) antes de modificar la organización y [la guía de autoría](docs/skill-authoring-guide.md) antes de crear o ampliar una skill.

## Milestone actual

`v0.1` prepara la metodología y reserva la estructura de:

- `product-analytics`
- `dashboard-ux`

Su alcance conceptual, contrato de inputs/outputs y casos de evaluación se definirán en iteraciones posteriores.

## Uso provisional

Los consumidores podrán instalar o enlazar de forma selectiva el directorio de una skill desde `.agents/skills/`. No se declara aún una estrategia oficial de distribución ni compatibilidad por agente.

## Contribuir

Leer `AGENTS.md` y `docs/skill-authoring-guide.md`. No agregar dependencias o automatización hasta que exista una necesidad repetible y verificable.