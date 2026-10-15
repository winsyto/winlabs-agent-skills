# Modelo de planificación

Leer esta referencia al crear una planificación, definir fases, materializar plantillas o resolver dudas sobre la responsabilidad de cada documento.

## Fuentes de verdad

| Documento | Responsabilidad | No debe convertirse en |
| --- | --- | --- |
| `roadmap.md` | Dirección, alcance, fases, estado ejecutivo, riesgos e hitos. | Backlog detallado o diario de sesiones. |
| `backlog/backlog-fase-XX.md` | Estado y contrato verificable de entregables. | Checklist de implementación minuto a minuto. |
| `wip.md` | Bloque activo, contexto operativo y próxima acción. | Historial acumulativo o copia del backlog. |
| `bitacora.md` | Historia breve de trabajo, decisiones e interrupciones. | Transcripción o segunda fuente del estado actual. |
| `parking-lot.md` | Posibilidades diferidas no comprometidas. | Backlog encubierto o alcance contabilizado. |
| `iniciativas/*.md` | Análisis previo de oportunidades. | Aprobación automática para incorporar trabajo. |

Si dos documentos discrepan, el backlog gobierna el estado de los entregables. Reconciliar el resumen del roadmap y el WIP contra esa fuente, preservando en bitácora la historia necesaria.

## Estados

Usar solo:

- **Pending:** registrado, todavía no preparado para ejecutar.
- **Ready:** suficientemente definido y sin impedimentos conocidos para comenzar.
- **WIP:** en ejecución dentro del bloque activo.
- **Blocked:** no puede continuar por un impedimento explícito.
- **Done:** cumple criterios de aceptación y posee evidencia.
- **Cancelled:** retirado del alcance, conservando el motivo.

Un ítem no pasa a `Done` por existir código, documentación o una declaración de avance. Registrar qué criterio se verificó, cómo y dónde está la evidencia. Si falta evidencia, mantener el estado anterior o declarar la incertidumbre.

## IDs y movimiento

- Fases: `F00`, `F01`, `F02`.
- Ítems: `F02-001`.
- Iniciativas: `INI-001`.
- Parking lot: `PL-001`.

Asignar el siguiente ID libre dentro de su secuencia. No reutilizar IDs cancelados ni renumerar al reordenar. Si `F02-003` cambia de fase, conservar el ID, ubicar su definición canónica en el backlog destino y registrar el movimiento; el prefijo señala origen, no ubicación eterna.

## Contenido de un ítem

Incluir ID, título, descripción, tipo, prioridad, estado, alcance o versión, criterios de aceptación observables, dependencias, evidencia al quedar `Done` y referencias relevantes. Usar `feature`, `bug`, `technical`, `research` u otro tipo justificado. La prioridad ordena; no exigir scoring cuando una secuencia razonada es suficiente.

## Roadmap y alcance

Registrar contexto, problema, usuarios, objetivos, factores de éxito, modelo de negocio si aplica, alcance actual, must have, nice to have y fuera de alcance. Resumir fases sin duplicar ítems. Identificar forma de trabajo y capacidad disponible, especialmente restricciones de una OPC.

Separar:

- **fecha comprometida:** acuerdo externo que crea una obligación;
- **fecha objetivo:** intención revisable;
- **estimación:** cálculo sujeto a supuestos.

Si no existe fecha, escribir “sin fecha acordada”; no completar una plantilla con fechas inventadas.

## F00 y F01

### F00 — Definición y preparación

Seleccionar solo lo pertinente: brief, usuarios y objetivos; alcance y éxito; arquitectura y stack; hosting, entornos y CI/CD; datos; CRUDs e integraciones; estrategia API/server actions; convenciones; UX y accesibilidad; errores; autenticación, autorización, roles y permisos; auditoría; validación y secrets; librerías; pruebas; observabilidad, backups y operación; skills disponibles; preparación técnica; y plan de validación.

No bloquear por toda incertidumbre. Marcar cada pregunta como bloqueante, diferible o descartada.

### F01 — Validación de la solución

Para aplicaciones con interfaz, planificar pantallas, flujos, layout, navegación, roles, estados y un mockup navegable. Para proyectos sin interfaz, usar contratos, ejemplos o un flujo de prueba equivalente. No tratar un mockup como prueba de seguridad implementada.

## Iniciativas

Crear un documento solo cuando la oportunidad merece análisis separado. Incluir problema, beneficiario, valor, evidencia, supuestos, alternativas, impacto, esfuerzo aproximado, riesgos, dependencias, recomendación, decisión, motivo y destino. El destino puede ser backlog, nueva fase, parking lot o descarte.

El parking lot no se limita a trabajo post-MVP: puede conservar cualquier posibilidad diferida que todavía no esté comprometida, siempre con motivo y condición de reconsideración cuando se conozca.

## Portabilidad

Mantener Markdown como contrato central. Detectar otras skills útiles —por ejemplo arquitectura, seguridad o UX— y declarar si están disponibles, pero no inventarlas ni bloquear el trabajo si son opcionales. La documentación técnica extensa vive fuera de `roadmap/` y se enlaza sin duplicación.
