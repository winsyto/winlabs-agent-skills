# Migración y reconstrucción

Leer esta referencia cuando el proyecto no tiene roadmap, existen varios documentos incompatibles o debe adoptarse la estructura canónica sin perder historia.

## Principio de preservación

Antes de reemplazar, mover o consolidar fuentes, conservar los originales o asegurar su recuperación mediante el mecanismo aprobado por el proyecto. No eliminar ni sobrescribir información material sin identificar primero la fuente, el destino y los conflictos.

## Inventario

Inspeccionar de forma proporcional instrucciones, README, docs, ADRs, pendientes, roadmaps previos, issues disponibles, historial reciente y evidencia de código, pruebas, releases o despliegues. Clasificar cada dato como:

- **Confirmado:** respaldado por fuente o evidencia identificable.
- **Inferido:** interpretación plausible que debe declararse.
- **Desconocido:** no existe base suficiente.

## Reconstrucción sin roadmap

1. Explicar qué fuentes se inspeccionaron y sus límites.
2. Reconstruir objetivos, alcance y fases sin fingir cronología histórica.
3. Crear IDs nuevos y estables para los ítems recuperados.
4. Marcar `Done` solo con criterios y evidencia suficientes; si no, usar el estado defendible y registrar el gap.
5. Evaluar F00 y F01 retrospectivamente. Usar “no aplica” con motivo cuando corresponda.
6. Crear una bitácora inicial fechada en el presente; no inventar entradas pasadas.
7. Indicar qué preguntas podrían cambiar la planificación.

## Migración de documentos existentes

1. Mapear fuentes antiguas a documentos canónicos.
2. Construir correspondencias para fases, ítems, estados y alcance.
3. Preservar IDs estables y compatibles; si se reemplazan, registrar el mapeo.
4. Resolver duplicados por identidad del trabajo, no por similitud del título.
5. Preservar decisiones, pendientes, criterios de aceptación, referencias e historia útil.
6. Separar contradicciones resolubles de las que requieren decisión humana.
7. Declarar una única fuente vigente y señalar las fuentes archivadas o reemplazadas.
8. Hacer la operación idempotente: repetirla no agrega fases, ítems o bitácora duplicados.

## Conflictos

Registrar tema, fuentes en desacuerdo, hecho confirmado, resolución aplicada y pregunta pendiente. No elegir silenciosamente la fuente más reciente si no es canónica ni la más antigua solo por preservar historia.

## Idempotencia

Antes de crear una entidad, buscar por ID y por identidad semántica. Antes de agregar bitácora, comprobar si el mismo evento ya existe. Antes de crear una fase, verificar que no exista bajo otro nombre. Actualizar en lugar de duplicar cuando la entidad es la misma.

## Cierre de migración

Informar fuentes inspeccionadas y preservadas, nueva fuente vigente, mapeos, decisiones, hechos, inferencias, desconocidos, contradicciones resueltas y pendientes, estado de enlaces/IDs/avance y próxima acción.
