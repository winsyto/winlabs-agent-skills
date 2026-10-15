# Coherencia y avance

Leer esta referencia al calcular avance, responder “cuánto falta”, reconciliar documentos o auditar la planificación.

## Fórmula

Para un alcance cerrado:

```text
avance = ítems Done / ítems no Cancelled del alcance × 100
```

Mostrar numerador, denominador, alcance y fecha local. Aclarar que mide cantidad de entregables, no esfuerzo ni tiempo. Calcular por MVP o versión comprometida y por fase.

No calcular un porcentaje global de un producto de alcance abierto. Si no hay ítems, mostrar **sin base de cálculo**. No asignar avance parcial a `WIP` o `Blocked`; ambos cuentan como no terminados.

Ejemplo: `3/8 ítems Done del MVP v1 — 37,5 % al 2026-10-15.`

Si el denominador cambia por alcance, explicar el efecto. Una caída porcentual puede provenir de incorporar trabajo, no de perder entregables terminados.

## Cuánto falta

Mostrar entregables no terminados por estado, bloqueos, dependencias, próximos hitos y base de cualquier estimación. No convertir `100 % - avance` en tiempo restante. Estimar tiempo solo con tamaño, capacidad, velocidad o experiencia comparables suficientes.

## Matriz de coherencia

| Regla | Verificación |
| --- | --- |
| Fases | Cada fase enlaza un backlog y cada backlog corresponde a una fase declarada. |
| Ítems | Cada ID tiene una definición canónica; referencias repetidas apuntan a ella. |
| Estados | Solo se usan los seis estados permitidos. |
| WIP | Sus IDs existen y los ítems activos tienen estado coherente. |
| Done | Cada ítem `Done` tiene evidencia asociada. |
| Cancelled | Cada cancelación tiene motivo y queda fuera del denominador. |
| Roadmap | El resumen coincide con conteos y estados de backlogs. |
| Bitácora | Explica cambios relevantes sin gobernar el estado actual. |
| Parking lot | No entra en alcance ni avance hasta una incorporación explícita. |
| Iniciativas | Decisión y destino coinciden con backlog, parking lot o descarte. |
| Enlaces | Todos los links Markdown locales resuelven con rutas relativas. |
| Fechas | Compromisos, objetivos y estimaciones están diferenciados. |

## Auditoría semántica

El validador automático puede detectar estructura, estados, IDs y enlaces. Revisar además criterios verificables, evidencia de `Done`, dependencias actuales, duplicados semánticos, fases impropias, WIP acumulativo, fechas no respaldadas, fuentes antiguas todavía vigentes, supuestos escritos como hechos y detalle lejano excesivo frente a trabajo próximo ambiguo.

Clasificar hallazgos como **Error** —invalida estado, avance o continuidad—, **Advertencia** —evidencia incompleta o drift— u **Observación**. No declarar coherencia completa mientras exista un error.
