# Eval 006 — Comparison-heavy dashboard

## Scenario

Una vista de desempeño necesita comparar varias anclas y segmentos. El caso prueba que `dashboard-ux` preserve contexto analítico sin mostrar todas las combinaciones al mismo tiempo.

## User request

> Diseñá la experiencia del dashboard para comparar desempeño actual contra período anterior y target, con cortes por región y tipo de cliente. Necesitamos explorar diferencias sin que la pantalla se vuelva ilegible.

## Expected activation

Sí. `dashboard-ux` debe activarse porque métricas y comparaciones están acordadas y el problema es priorizar, representar y explorar múltiples contextos.

## Context

- Audiencia: responsables regionales y dirección comercial en revisión semanal.
- Decisiones: intervenir en una región, revisar mix de clientes o mantener el plan.
- Métricas definidas: tasa de renovación, expansión neta y tiempo hasta primer valor.
- Comparación primaria: target del trimestre vigente.
- Comparación secundaria: período anterior equivalente.
- Segmentos acordados: región y tipo de cliente; pueden combinarse, pero algunas celdas tienen bajo volumen.
- Freshness: 24 horas; el período actual puede estar incompleto.
- Guardrail: descuentos concedidos para sostener renovación.
- No se pide redefinir targets ni calcular significancia.

## Expected characteristics

- Priorizar una comparison anchor por decisión y mantener otras accesibles.
- Hacer visibles medida, unidad, ventana, población, freshness y período incompleto.
- Evitar superponer todas las métricas, anchors y segmentos en una sola vista.
- Proponer una progresión overview → selección → detail preservando contexto.
- Definir cómo filtros o selection afectan comparación y guardrail.
- Tratar bajo volumen y datos parciales como límites de interpretación.
- Permitir comparación entre segmentos sin rankings engañosos.
- Definir reset, estado activo y retorno cuando la exploración sea profunda.
- Incluir acceso no dependiente de color, hover o pointer.

## Required concepts

- comparison model;
- primary and secondary anchors;
- temporal, target and segment comparison;
- overview versus detail;
- filter or selection scope;
- incomplete and partial data;
- guardrail context;
- progressive disclosure;
- accessibility.

## Forbidden / undesirable behavior

- Cambiar el target o declarar qué región rinde mejor sin datos.
- Mostrar todas las combinaciones simultáneamente por completitud.
- Ocultar período, población o anchor en un tooltip.
- Usar color como única señal de diferencia o riesgo.
- Tratar el período incompleto como equivalente al anterior.
- Elegir una receta rígida de charts o una librería frontend.
- Escribir SQL, cálculos, tracking o código.
- Afirmar causalidad por diferencias entre segmentos.

## Success criteria

1. La comparación principal es inmediata y las secundarias siguen siendo descubribles.
2. La exploración conserva filtros, anchors, ventana y contexto de guardrail.
3. Datos incompletos o de bajo volumen limitan visiblemente la interpretación.
4. La complejidad se distribuye entre overview y detail sin perder capacidad diagnóstica.
5. La solución permanece en UX conceptual y respeta el contrato analítico.
