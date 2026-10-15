# Catálogo de skills

Este archivo es el inventario canónico de capacidades planificadas o publicadas. Incluir una skill aquí no implica que esté lista para uso.

| Skill | Estado | Milestone | Alcance actual |
| --- | --- | --- | --- |
| `product-analytics` | Experimental | v0.1 | Contrato operativo, cuatro referencias bajo demanda y evals iniciales implementados; sujeto a validación de uso y compatibilidad. |
| `dashboard-ux` | Experimental | v0.1 | Contrato operativo para diseñar y revisar dashboards, cuatro referencias bajo demanda y seis evals iniciales; pendiente de prueba en un dashboard real. |
| `roadmap-backlog` | Experimental | Sin asignar | Contrato operativo, plantillas portables, validador opcional y diez evals iniciales para planificación persistente por proyecto; pendiente de revisión independiente, forward testing y uso real. |

## Estados

- **Propuesta**: alcance en discusión, sin contrato estable.
- **Esqueleto**: estructura creada, no apta para uso operativo.
- **Experimental**: contrato implementado y evals iniciales; sujeto a cambios.
- **Estable**: criterios de calidad y compatibilidad de la versión cumplidos.
- **Deprecated**: reemplazo o retiro anunciado.

## Decisiones pendientes para v0.1

- Probar el Review mode de `dashboard-ux` sobre un dashboard real y registrar los fallos observados.
- Confirmar con fallos observados si las evals necesitan un runner, sin introducir tooling prematuro.
- Ejecutar evaluación independiente, forward testing y uso real antes de promover una skill a Stable.
- Definir matriz mínima de compatibilidad y mecanismo de distribución para agentes consumidores.
- Asignar `roadmap-backlog` a un milestone sin redefinir implícitamente el alcance de v0.1.
