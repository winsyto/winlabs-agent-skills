# Análisis de lifecycle

Usar esta referencia cuando el problema involucre recorrido, adopción o comportamiento a través del tiempo. Elegir solo los conceptos que correspondan al producto y la decisión.

## Elegir el análisis apropiado

| Pregunta | Concepto útil |
| --- | --- |
| ¿Dónde se interrumpe una secuencia necesaria? | Funnel y conversion. |
| ¿Quién alcanza por primera vez una señal temprana de valor? | Activation. |
| ¿Qué parte de la población elegible comienza a usar una capacidad? | Adoption. |
| ¿Con qué frecuencia, profundidad o amplitud ocurre uso valioso? | Engagement. |
| ¿Quién continúa obteniendo valor después del inicio? | Retention. |
| ¿Cómo cambia el comportamiento según momento de entrada o exposición? | Cohorts. |

No asumir que todo producto necesita cubrir todas estas preguntas.

## Funnels y conversion

Usar un funnel cuando:

- existe una secuencia de etapas necesaria o analíticamente útil;
- puede identificarse una población de entrada;
- el orden y la ventana importan;
- la pérdida entre etapas habilita una intervención.

Definir para cada etapa:

- evento conceptual de entrada y finalización;
- unidad de análisis;
- denominador: cohorte inicial o etapa previa, según la pregunta;
- ventana permitida;
- tratamiento de saltos, repeticiones, reaperturas y abandono;
- segmentos que podrían explicar diferencias.

Distinguir:

- **conversion total:** finalizadores / población inicial elegible;
- **conversion por etapa:** quienes avanzan / quienes llegaron a esa etapa;
- **tiempo entre etapas:** duración, espera y dispersión, no solo promedio total.

No multiplicar o comparar tasas con reglas incompatibles. Si el recorrido es no lineal, usar caminos, estados o hitos en lugar de forzar un funnel único.

## Activation

Definir activation como evidencia temprana de que el actor experimentó valor, no como registro, login o configuración por defecto.

Una señal candidata debe:

- ocurrir después de una oportunidad real de uso;
- representar un cambio significativo en el workflow o resultado;
- ser suficientemente temprana para orientar intervención;
- mantener una relación plausible con valor posterior;
- poder distinguirse de actividad accidental o administrativa.

Especificar población elegible, acción o resultado, ventana desde el ancla y unidad. Validar la relación con outcomes posteriores antes de tratarla como driver establecido.

## Adoption

Adoption responde quién comienza a usar de forma significativa una capacidad. Separar:

1. **Elegibilidad:** quién tiene acceso y un caso razonable de uso.
2. **Exposición o descubrimiento:** quién tuvo oportunidad de conocerla.
3. **Primer uso significativo:** quién realizó la acción que aproxima valor.
4. **Adopción sostenida:** quién repite o integra la capacidad en su workflow, si eso importa.

Elegir nivel usuario o cuenta según dónde se materializa el valor. En productos multiusuario puede ser necesario observar ambos sin mezclarlos.

No usar toda la base como denominador si existen restricciones de plan, rol, rollout o necesidad.

## Engagement

Engagement describe la intensidad del uso valioso, no cualquier interacción. Elegir una combinación pertinente:

- **frecuencia:** cuántas veces ocurre el comportamiento dentro de un período adecuado;
- **profundidad:** cuánto valor o trabajo se completa por episodio;
- **amplitud:** cuántos usuarios, equipos o partes relevantes participan;
- **regularidad:** consistencia respecto del ritmo natural del producto.

Más actividad no siempre es mejor. Un producto eficiente puede reducir clicks, sesiones o tiempo. Relacionar engagement con el outcome y proteger calidad o esfuerzo mediante guardrails.

## Retention

Definir retention como continuidad en la obtención de valor, no retorno genérico a la aplicación.

Especificar:

- **ancla:** signup, activation, primera compra, habilitación u otro origen;
- **comportamiento retenido:** acción o resultado que representa valor recurrente;
- **cohorte:** población que comparte ancla y período;
- **intervalo:** día, semana, mes, ciclo o episodio;
- **forma:** retorno en un período exacto, retorno desde entonces o repetición dentro de una ventana;
- **unidad:** usuario, cuenta u otra entidad.

Elegir el intervalo según la frecuencia natural. No medir D1/D7/D30 por costumbre en productos mensuales, estacionales o episódicos.

Separar retención de usuario, cuenta, revenue o contrato: responden preguntas distintas. Una cuenta puede retenerse mientras cambian sus usuarios, y un usuario puede permanecer sin generar valor de negocio suficiente.

## Cohorts

Usar cohorts cuando el tiempo desde un origen o exposición cambia la interpretación. Definir:

- criterio de pertenencia;
- fecha o evento ancla;
- período de observación y maduración;
- comportamiento comparado;
- dimensión adicional solo si responde una hipótesis.

Comparar cohortes a la misma edad. No comparar una cohorte reciente incompleta con otra que tuvo más tiempo para convertir o retenerse.

Las cohortes pueden basarse en inicio, activation, feature exposure, plan o intervención. Elegir el ancla que corresponda a la pregunta, no la que resulte más fácil de obtener.

## Actividad versus valor

Antes de aceptar una métrica de lifecycle, preguntar:

- ¿La acción representa valor o solo movimiento dentro de la interfaz?
- ¿Completarla más veces es inequívocamente mejor?
- ¿Un usuario puede obtener el mismo outcome con menos actividad?
- ¿La métrica incentiva spam, fricción o trabajo innecesario?
- ¿Qué outcome posterior o evidencia cualitativa valida su significado?

Clicks, sesiones, mensajes o tiempo pueden servir como diagnósticos, pero no deben asumirse como outcomes.

## Errores habituales

- Definir activation como signup sin demostrar valor.
- Calcular adoption sobre población no elegible.
- Confundir primer uso con uso sostenido.
- Tratar volumen de actividad como engagement positivo.
- Medir retention con cualquier login.
- Usar ventanas arbitrarias o mezclar cohortes con distinta madurez.
- Forzar funnels sobre recorridos no lineales.
- Ocultar diferencias entre usuario y cuenta.
- Interpretar una mejora correlacionada como efecto causal de una feature.

## Checklist de cierre

- El concepto elegido responde una decisión concreta.
- La unidad, elegibilidad, ancla y ventana están definidas.
- Los denominadores son consistentes.
- El comportamiento representa o aproxima valor.
- El ritmo de uso refleja el producto real.
- Cohortes y segmentos se comparan de forma equivalente.
- Existen guardrails si más actividad puede producir daño.
- Las limitaciones de interpretación están explícitas.
