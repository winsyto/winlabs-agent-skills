---
name: roadmap-backlog
description: Crear, reconstruir, migrar, consultar y mantener roadmaps, backlogs por fase, WIP y bitácoras persistentes para proyectos de desarrollo con capacidad limitada u OPC. Usar cuando se necesite planificar, retomar, reordenar, registrar avance o verificar coherencia documental; no usar para ejecutar cambios funcionales ni gestionar un portafolio global entre proyectos.
---

# Roadmap Backlog

## Propósito

Mantener un sistema Markdown persistente para que una persona y distintos agentes entiendan qué se busca, qué está comprometido, qué está activo, qué ocurrió y cuál es la próxima acción exacta.

## Usar cuando

- Crear la planificación de un proyecto nuevo.
- Reconstruir planificación desde código, documentación o evidencia existente.
- Migrar roadmaps o backlogs a una estructura común.
- Consultar estado, avance, pendientes o punto de reanudación.
- Preparar, actualizar, interrumpir o cerrar un bloque de trabajo.
- Incorporar bugs, urgencias o cambios de alcance.
- Analizar una iniciativa antes de comprometerla.
- Auditar coherencia entre roadmap, backlogs, WIP y bitácora.

## No usar cuando

- El pedido es ejecutar código, instalar dependencias, hacer commit, desplegar o modificar sistemas externos sin autorización específica.
- Se busca administrar un portafolio global entre repositorios.
- Solo se necesita una lista transitoria sin continuidad documental.
- El pedido principal es gestión operativa en una herramienta propietaria.

## Contrato de autonomía

Cuando el usuario solicita crear, actualizar, migrar o reconciliar la planificación, administrar autónomamente los documentos de `roadmap/`: desglosar, ordenar, priorizar, registrar decisiones, actualizar estados y sincronizar vistas sin pedir aprobación por cada edición. Respetar decisiones y restricciones explícitas; preguntar únicamente cuando falte información que cambie materialmente el resultado y registrar inferencias relevantes como supuestos.

Una consulta de estado es de solo lectura salvo pedido adicional de actualización o reconciliación. La autonomía documental no autoriza cambios funcionales, instalaciones, commits, despliegues ni acciones externas.

## Estructura canónica

Mantener dentro de cada proyecto consumidor:

```text
roadmap/
├── roadmap.md
├── wip.md
├── bitacora.md
├── parking-lot.md
├── backlog/
│   └── backlog-fase-XX.md
└── iniciativas/
    └── iniciativa-XXX-nombre.md
```

Crear un backlog por cada fase definida. Crear `iniciativas/` y sus documentos solo cuando exista una iniciativa. No crear un roadmap global entre proyectos. Usar nombres en minúsculas, enlaces relativos y siempre el término **fase**.

Para materializar la estructura, adaptar las plantillas de [assets/templates/](assets/templates/) y eliminar todas las ayudas entre corchetes. No copiar plantillas sin resolverlas con evidencia y contexto reales.

## Modelo esencial

- `roadmap.md`: contexto, alcance, fases, estado ejecutivo, riesgos e hitos; no duplica detalle.
- `backlog/backlog-fase-XX.md`: fuente del estado de los entregables y sus criterios de aceptación.
- `wip.md`: único bloque activo, contexto de ejecución y próxima acción; no es un historial.
- `bitacora.md`: historial breve de resultados, decisiones, cierres e interrupciones.
- `parking-lot.md`: posibilidades no comprometidas, fuera del porcentaje de avance.
- `iniciativas/`: análisis previo; una idea no se incorpora automáticamente al alcance.

Usar exactamente `Pending`, `Ready`, `WIP`, `Blocked`, `Done` y `Cancelled`. Leer [references/planning-model.md](references/planning-model.md) al crear estructura, definir fases, estados, IDs o alcance.

## Modos y workflow

1. **Detectar intención y permisos.** Distinguir consulta de solo lectura de creación, migración o actualización autorizada.
2. **Leer en orden.** Empezar por `roadmap.md` y `wip.md`; continuar con el backlog relevante y las últimas entradas de bitácora. Ampliar solo según la consulta.
3. **Separar evidencia.** Distinguir confirmado, inferido y desconocido. Código presente no equivale a entregable `Done`.
4. **Elegir modo.** Crear, reconstruir, migrar, consultar, actualizar/replanificar, analizar iniciativa o verificar coherencia.
5. **Operar desde la fuente correcta.** Cambiar estados en backlog, ejecución en WIP, historia en bitácora y resumen en roadmap.
6. **Sincronizar.** Actualizar todos los documentos afectados; no declarar la operación completa si quedan contradicciones.
7. **Validar y resumir.** Informar archivos afectados, estado resultante, supuestos, evidencia, bloqueos y próxima acción.

Para crear, consultar, interrumpir, cerrar o reanudar trabajo, leer [references/operating-workflows.md](references/operating-workflows.md). Para reconstruir o migrar documentación existente, leer [references/migration-and-reconstruction.md](references/migration-and-reconstruction.md). Para porcentajes, referencias cruzadas y auditorías, leer [references/consistency-and-progress.md](references/consistency-and-progress.md).

## Fases iniciales

- **F00 — Definición y preparación:** dejar contexto y decisiones suficientes para construir; distinguir incertidumbres bloqueantes de las diferibles.
- **F01 — Validación de la solución:** para interfaces, mockup navegable; para APIs, automatizaciones u otros proyectos, contratos, ejemplos o flujo de prueba equivalente.
- **F02 en adelante:** definir según el producto, con objetivo, entregables, criterios de cierre y dependencias.

En proyectos existentes, evaluar F00 y F01 retrospectivamente. No exigir rehacerlas ni marcarlas `Done` sin evidencia; admitir “no aplica” con justificación. Planificar seguridad durante definición, implementación y entrega de forma proporcional al sistema.

## Reglas no negociables

- Usar IDs estables: `F00`, `F02-001`, `INI-001`, `PL-001`. Si un ítem cambia de fase, conservar su ID y registrar la nueva ubicación.
- Mantener un bloque principal activo por defecto. Si no existe trabajo activo, indicarlo y señalar el próximo candidato sin marcarlo `WIP`.
- Antes de reemplazar WIP, actualizar backlog, transferir conocimiento durable, registrar cierre o interrupción y preservar pendientes.
- Incorporar bugs y urgencias al backlog de una fase apropiada; no crear una fase por incidente.
- No inventar fechas, targets, evidencia histórica, estados `Done` ni estimaciones temporales.
- Distinguir fechas comprometidas, fechas objetivo y estimaciones.
- Conservar o hacer recuperables los documentos originales antes de una migración destructiva y declarar la fuente vigente.
- Repetir una operación no debe duplicar fases, ítems ni entradas de bitácora.

## Output

Para consultas, ofrecer:

- **Brief rápido:** objetivo, fase actual, trabajo activo, último resultado, bloqueo principal y próxima acción.
- **Brief detallado:** lo anterior más alcance, avance, decisiones, dependencias, riesgos, pendientes y evidencia.

Para mutaciones, entregar documentos creados o actualizados, cambios de estado o alcance, evidencia registrada, supuestos, inconsistencias pendientes y próxima acción.

## Quality gates

- [ ] Existe un backlog por fase y cada ítem tiene ID estable, tipo, prioridad, estado, alcance, criterios verificables y referencias pertinentes.
- [ ] `Done` tiene evidencia y `Cancelled` conserva motivo.
- [ ] Roadmap resume el backlog; WIP referencia IDs válidos; bitácora registra historia sin duplicarla.
- [ ] Parking lot e iniciativas no comprometidas quedan fuera del avance.
- [ ] Fechas y estimaciones tienen naturaleza explícita y base suficiente.
- [ ] Estado documentado y estado verificado están diferenciados.
- [ ] No quedan links locales rotos, IDs ambiguos, estados inválidos ni fuentes vigentes contradictorias.
- [ ] El detalle es preciso para lo próximo y más general para lo lejano.
- [ ] El resultado es portable y no depende de un agente, plugin o ruta absoluta.

Cuando esté disponible, ejecutar opcionalmente `scripts/validate_roadmap.py <ruta-al-roadmap>` para controles deterministas. El script complementa, pero no sustituye, la revisión semántica.

## Anti-patterns

- Copiar el backlog completo al roadmap o al WIP.
- Usar subtareas del WIP para inflar el porcentaje.
- Inferir tiempo restante desde el porcentaje de entregables.
- Convertir toda idea en compromiso o toda urgencia en fase.
- Reescribir IDs al reordenar trabajo.
- Crear documentos vacíos “por si acaso”.
- Sobrescribir historia sin conservar decisiones, pendientes y evidencia.
- Mezclar planificación documental con autorización de ejecución.
