# Diseño conceptual de `roadmap-backlog`

Estado del documento: contrato operativo inicial.

Estado de la skill: Experimental.

Milestone: sin asignar; la incorporación de esta capacidad fue solicitada explícitamente fuera del alcance original de Analytics & Dashboard Foundation.

## Propósito

Definir un sistema Markdown portable para crear, reconstruir, migrar, consultar y mantener la planificación de un proyecto de desarrollo con capacidad limitada u OPC. El sistema debe conservar continuidad entre sesiones y agentes sin convertirse en una aplicación de project management ni autorizar ejecución funcional.

## Casos de activación

- Crear roadmap y backlog para un proyecto nuevo.
- Reconstruir el estado de un proyecto existente sin planificación canónica.
- Migrar documentos contradictorios o incompletos.
- Consultar estado, avance, pendientes o punto de reanudación.
- Preparar, interrumpir o cerrar un bloque de trabajo.
- Registrar bugs, urgencias, decisiones y cambios de alcance.
- Analizar iniciativas o auditar coherencia documental.

## Límites

- No ejecutar código, instalaciones, commits, despliegues ni acciones externas por el solo hecho de administrar planificación.
- No crear un roadmap global entre repositorios.
- No depender de plugins, servicios propietarios, rutas absolutas o funciones de un agente concreto.
- No sustituir documentación técnica extensa; enlazarla desde `roadmap/`.
- No convertir consultas de estado en mutaciones implícitas.

## Modelo documental

| Nivel | Documento | Responsabilidad |
| --- | --- | --- |
| Alto | `roadmap.md` | Contexto, alcance, fases, resumen ejecutivo, riesgos e hitos. |
| Medio | `backlog/backlog-fase-XX.md` | Fuente de estado, criterios y evidencia de entregables. |
| Detallado | `wip.md` | Único bloque activo, ejecución y próxima acción. |
| Historia | `bitacora.md` | Resultados, decisiones, cierres e interrupciones por fecha local. |
| Diferido | `parking-lot.md` | Posibilidades no comprometidas y fuera del avance. |
| Análisis | `iniciativas/*.md` | Evaluación previa a incorporar, postergar o descartar trabajo. |

La skill vive exclusivamente en `.agents/skills/roadmap-backlog/`. Este repositorio no recibe una planificación activa en `roadmap/`; las plantillas se materializan únicamente en proyectos consumidores cuando el usuario lo solicita.

## Fuentes de verdad

El backlog gobierna el estado de los entregables. El roadmap resume, el WIP referencia y profundiza la ejecución, y la bitácora conserva historia. Una operación está incompleta si deja contradicciones entre esas vistas.

## Autonomía y autorización

Una solicitud explícita de crear, actualizar, migrar o reconciliar planificación autoriza administrar autónomamente `roadmap/` dentro del proyecto consumidor. No se requiere aprobación por cada edición documental. Deben respetarse restricciones explícitas y pedirse datos solo cuando su ausencia impida decidir con criterio.

Una consulta es read-only. La autonomía documental no se extiende a implementación, instalaciones, commits, despliegues ni sistemas externos.

## Fases e IDs

- Usar `F00` para definición y preparación.
- Usar `F01` para mockup navegable o validación equivalente.
- Definir F02 en adelante por objetivos y criterios de cierre del producto.
- Usar IDs estables `F02-001`, `INI-001` y `PL-001`.
- Conservar el ID de un ítem aunque cambie de fase; registrar el movimiento.

En proyectos existentes, F00 y F01 se evalúan retrospectivamente y pueden ser “no aplica” con motivo. No se marcan completas sin evidencia.

## Estados

El conjunto cerrado es `Pending`, `Ready`, `WIP`, `Blocked`, `Done` y `Cancelled`. `Done` exige criterios cumplidos y evidencia. `Cancelled` conserva motivo e historia.

## Avance

Para alcance cerrado:

```text
Done / ítems no Cancelled del alcance × 100
```

El resultado siempre incluye numerador, denominador, alcance y fecha, y se presenta por versión comprometida y por fase. No representa esfuerzo ni tiempo. Parking lot e iniciativas no incorporadas quedan fuera. Un producto de alcance abierto no recibe porcentaje global.

## Progressive disclosure

`SKILL.md` contiene activación, límites, autonomía, modelo esencial, routing y gates. Las referencias separan:

| Referencia | Leer cuando |
| --- | --- |
| `planning-model.md` | Crear estructura, fases, estados, IDs o alcance. |
| `operating-workflows.md` | Consultar, iniciar, interrumpir, cerrar o retomar trabajo. |
| `migration-and-reconstruction.md` | Reconstruir o migrar fuentes existentes. |
| `consistency-and-progress.md` | Calcular avance, reconciliar o auditar coherencia. |

Las plantillas son assets copiables, no instrucciones cargadas por defecto. El script es opcional y complementa la revisión semántica.

## Validador

`scripts/validate_roadmap.py` usa solo la biblioteca estándar de Python y comprueba estructura requerida, backlogs, IDs canónicos, estados, evidencia mínima de `Done`, enlaces relativos, referencias del WIP y duplicados básicos. No pretende evaluar calidad de producto, suficiencia real de evidencia, prioridad ni semántica de criterios.

## Evals

La suite inicial cubre los diez escenarios solicitados: proyectos nuevos con y sin interfaz, reconstrucción, migración conflictiva, consulta read-only, interrupción por bug, cierre y próximo bloque, cambio de alcance, idempotencia y recuperación de contexto.

Las evals observan comportamiento y límites; no exigen redacción literal. La evaluación de esta tarea es interna a la sesión de autoría y no cuenta como revisión independiente ni forward testing en otros agentes.

## Estado recomendado

Mantener `roadmap-backlog` como **Experimental**. Puede probarse en proyectos sintéticos y luego reales, pero no cumple el gate de Stable hasta contar con evaluación independiente, forward testing en agentes compatibles y evidencia de uso real.

## Decisiones pendientes

1. Asignar la skill a un milestone de la biblioteca.
2. Observar en proyectos reales si las cuatro referencias son el mínimo correcto.
3. Verificar compatibilidad del validador en los entornos consumidores donde se decida usarlo.
4. Evaluar si aparecen conflictos reales que justifiquen reglas adicionales sin ampliar el contrato preventivamente.
