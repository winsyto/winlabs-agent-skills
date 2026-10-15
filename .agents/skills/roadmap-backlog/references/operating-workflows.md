# Flujos operativos y continuidad

Leer esta referencia al crear planificación, consultar estado, iniciar o interrumpir WIP, cerrar un bloque, incorporar trabajo no planificado o recuperar contexto.

## Crear un proyecto nuevo

1. Inspeccionar instrucciones y contexto existentes antes de crear archivos.
2. Identificar problema, usuarios, objetivos, alcance, restricciones, capacidad y evidencia disponible.
3. Definir F00, F01 y fases posteriores suficientes para mostrar dirección, sin sobredetallar trabajo lejano.
4. Crear un backlog por fase con ítems verificables.
5. Definir el alcance comprometido o declarar que todavía está abierto.
6. Inicializar WIP con un bloque solo si el trabajo realmente comienza; de lo contrario, indicar “sin trabajo activo” y el próximo candidato.
7. Inicializar bitácora y parking lot sin entradas ficticias.
8. Verificar enlaces, IDs y coherencia antes de declarar la planificación lista.

Para proyectos con interfaz, F01 usa un mockup navegable. Para proyectos sin interfaz, registrar la validación equivalente y su evidencia esperada.

## Consultar estado

La consulta es de solo lectura. Leer `roadmap.md`, `wip.md`, el backlog de la fase o IDs activos y las entradas recientes de bitácora necesarias. Ampliar a riesgos, iniciativas o parking lot solo si la pregunta lo requiere. Distinguir estado documentado de evidencia verificada durante la consulta.

### Brief rápido

- objetivo;
- fase actual;
- trabajo activo;
- último resultado;
- bloqueo principal;
- próxima acción exacta.

### Brief detallado

Agregar alcance y avance, decisiones relevantes, dependencias, riesgos, pendientes y evidencia disponible.

## Preparar el siguiente bloque

Elegir trabajo `Ready` según prioridad, dependencias, riesgo, continuidad y capacidad real. Un bloque puede abarcar varios ítems relacionados, pero no una fase completa por obligación.

Actualizar `wip.md` con objetivo, IDs, fecha local, contexto, checklist concreta, decisiones, supuestos, verificaciones, bloqueos, próxima acción y notas para retomar. Cambiar a `WIP` únicamente los ítems que realmente comienzan.

## Actualizar durante la ejecución

- Mantener el backlog como fuente de estado.
- Registrar en WIP los pasos y resultados necesarios para continuar.
- Transferir decisiones duraderas a la documentación que corresponda.
- Agregar a bitácora solo un resumen útil; agrupar sesiones del mismo día cuando evita repetición.
- Actualizar el resumen del roadmap cuando cambian fase, alcance, riesgos, avance o hitos.

No generar una entrada de bitácora idéntica ante una ejecución repetida.

## Interrumpir por bug o urgencia

1. Crear un ítem `bug` o del tipo pertinente en el backlog de la fase adecuada.
2. Definir prioridad, criterios y evidencia necesaria.
3. Registrar en WIP el punto exacto de retorno del bloque interrumpido.
4. Cambiar estados según la realidad: el trabajo anterior puede seguir `WIP`, pasar a `Blocked` o volver a `Ready`.
5. Registrar la interrupción y su impacto en bitácora.
6. Inicializar el bloque urgente y actualizar roadmap si afecta alcance o hitos.

No crear una fase exclusiva por incidente salvo que el conjunto de trabajo tenga objetivo y criterios de cierre propios.

## Cerrar o reemplazar WIP

Antes de reemplazarlo:

1. Evaluar criterios de aceptación de cada ítem involucrado.
2. Actualizar estados y evidencia en sus backlogs.
3. Transferir decisiones y resultados duraderos.
4. Registrar cierre, interrupción o remanentes en bitácora.
5. Conservar trabajo pendiente explícitamente y devolverlo a un estado coherente.
6. Actualizar resumen y avance del roadmap.
7. Inicializar el siguiente bloque o declarar “sin trabajo activo”.

Un cierre de bloque no exige que todos los ítems queden `Done`; puede cerrar por interrupción, cambio de alcance o división consciente.

## Recuperar contexto en una sesión nueva

Reconstruir:

```text
objetivo del roadmap
→ fase y alcance actuales
→ IDs del WIP
→ estado y criterios en backlog
→ último resultado en bitácora
→ próxima acción exacta
```

Si la cadena se rompe, declarar la inconsistencia y proponer reconciliación; no completar huecos como hechos.

## Cambios de alcance

Registrar qué ítems entran o salen, motivo, versión afectada y fecha local de decisión. `Cancelled` conserva historia pero se excluye del denominador. Parking lot no se cuenta como compromiso. Recalcular el avance con la nueva base y explicar la variación causada por alcance, no por ejecución.
