# Evaluation report — `roadmap-backlog`

Fecha: 2026-10-15.

## Alcance y método

Se evaluaron los diez escenarios solicitados contra comportamiento observable, límites de autorización, coherencia documental y capacidad de recuperación. La revisión consistió en:

1. recorrido manual de cada prompt desde la descripción de activación hasta las referencias y assets que debería cargar;
2. comprobación del resultado esperado contra reglas explícitas del contrato;
3. materialización sintética de las plantillas en un directorio temporal;
4. tests del validador sobre un roadmap válido y otro con errores;
5. controles estructurales de frontmatter, links, rutas, archivos y diff.

No se modificaron proyectos reales. La evaluación fue realizada en la misma sesión de autoría; no es revisión independiente ni forward testing en otro agente.

## Resumen

| Eval | Capacidad principal | Resultado |
| --- | --- | --- |
| 001 | Proyecto nuevo con interfaz | PASS |
| 002 | Proyecto nuevo sin interfaz | PASS |
| 003 | Reconstrucción sin roadmap | PASS |
| 004 | Migración contradictoria | PASS |
| 005 | Consulta rápida read-only | PASS |
| 006 | Interrupción por bug | PASS |
| 007 | Cierre y siguiente bloque | PASS |
| 008 | Cambio de alcance y avance | PASS |
| 009 | Reejecución idempotente | PASS |
| 010 | Recuperación en sesión nueva | PASS |

Resultado global: **10 PASS, 0 PARTIAL, 0 FAIL** dentro del alcance de evaluación interna.

## Hallazgos por escenario

### 001 — Proyecto nuevo con interfaz

El routing activa creación, exige estructura por proyecto y aplica F00/F01. `planning-model.md` define mockup navegable, seguridad proporcional y capacidad OPC; `operating-workflows.md` evita iniciar WIP si solo se pidió planificar. Las plantillas no contienen fechas ficticias. **PASS**.

### 002 — Proyecto nuevo sin interfaz

F01 admite contratos, ejemplos o flujo de prueba equivalente. El contrato no fuerza UI y conserva autenticación, autorización, inputs, secrets, auditoría y operación como decisiones contextuales. La planificación no amplía permisos de implementación. **PASS**.

### 003 — Proyecto existente sin roadmap

`migration-and-reconstruction.md` separa confirmado, inferido y desconocido; trata código y tests como evidencia, no conclusión; prohíbe historia inventada y exige evaluar F00/F01 retrospectivamente. **PASS**.

### 004 — Migración contradictoria

El flujo preserva fuentes, mapea entidades, resuelve identidad semántica, mantiene conflictos visibles y declara una fuente vigente. La regla de idempotencia evita duplicados en una segunda ejecución. **PASS**.

### 005 — Consulta rápida sin cambios

El contrato identifica consultas como read-only, prescribe lectura roadmap → WIP → backlog relevante → bitácora reciente y define un brief rápido sin reconciliación implícita. **PASS**.

### 006 — Interrupción por bug

`operating-workflows.md` incorpora el bug a una fase adecuada, conserva punto de retorno, sincroniza estados, WIP, bitácora e impacto y prohíbe crear una fase por incidente. No autoriza corregir código. **PASS**.

### 007 — Cierre y preparación del siguiente bloque

La secuencia obliga a evaluar criterios y evidencia, actualizar backlog, transferir decisiones, registrar cierre y conservar pendientes antes de reemplazar WIP. Permite cerrar el bloque sin fingir que todos los ítems terminaron. **PASS**.

### 008 — Cambio de alcance

`consistency-and-progress.md` usa `Done / no Cancelled`, excluye parking lot e iniciativas y exige explicar cambios del denominador. Para el escenario, el resultado correcto es `3/7 = 42,9 %`, no una pérdida de trabajo ni una estimación temporal. **PASS**.

### 009 — Reejecución sin duplicados

La migración busca por ID e identidad semántica, actualiza entidades existentes y evita repetir fases, ítems y eventos. La evidencia nueva puede incorporarse sin recrear el evento original. **PASS**.

### 010 — Recuperación de contexto

El flujo reconstruye objetivo → fase/alcance → IDs activos → estado/criterios → último resultado → próxima acción y exige declarar cualquier ruptura como inconsistencia. La consulta permanece read-only. **PASS**.

## Validación del validador y plantillas

`test_validator.py` ejecutó cuatro pruebas con `unittest`:

- materialización de las plantillas con F00 y F01: sin hallazgos;
- fixture sintético válido: sin hallazgos;
- fixture inválido: detectó archivo obligatorio faltante, link roto y estados inválidos.
- fixture inconsistente: detectó divergencia de estado y referencias inexistentes a iniciativa y parking lot.

Resultado: **4 tests OK**.

El validador comprueba estructura, backlogs, IDs, estados, evidencia mínima de `Done`, links locales relativos, referencias WIP y duplicados básicos. La revisión semántica sigue siendo obligatoria.

## Validación estructural

- Frontmatter: solo `name` y `description`.
- Links de instrucciones y referencias: resolubles.
- Rutas absolutas específicas de máquina: ninguna.
- Evals: diez archivos con request, comportamiento esperado y criterios de éxito.
- Planificación activa en la raíz de este repositorio: no existe.
- `git diff --check`: sin errores.
- Validador genérico `quick_validate.py`: no ejecutado por ausencia de PyYAML; no se instalaron dependencias. Se reprodujeron manualmente sus controles aplicables.

## Limitaciones

- No hubo evaluación ciega ni subagente independiente.
- No se probó selección automática real de la skill en distintos hosts.
- No hubo uso en un proyecto real.
- El validador no determina si la evidencia es suficiente, si la prioridad es correcta o si dos ítems son duplicados semánticos.

## Recomendación de estado

Mantener **Experimental**. La implementación y la evaluación interna permiten probarla, pero no justifican Stable sin revisión independiente, forward testing y uso real.
