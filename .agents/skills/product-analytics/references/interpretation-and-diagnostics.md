# Interpretación y diagnóstico

Usar esta referencia para explicar movimientos de métricas, elegir dimensiones diagnósticas y proponer acciones sin convertir correlación en causalidad ni diseñar visualizaciones.

## Cadena de interpretación

Mantener separados estos niveles:

1. **Observación:** qué cambió, en qué magnitud, período, población y definición.
2. **Comparación:** contra qué baseline, target, período, cohorte o segmento se evalúa.
3. **Interpretación:** qué podría significar el patrón dentro del modelo métrico.
4. **Explicaciones alternativas:** qué otros cambios, sesgos o problemas podrían producirlo.
5. **Evidencia adicional:** qué análisis, dato o diseño permitiría discriminar hipótesis.
6. **Acción:** qué decisión reversible, intervención o investigación es razonable ahora.

No saltar de observación a acción irreversible cuando existen explicaciones plausibles no examinadas.

## Dimensiones diagnósticas

Elegir una dimensión solo si una diferencia entre grupos puede cambiar el diagnóstico o la acción. Candidatas frecuentes —no obligatorias— incluyen:

- antigüedad o cohorte;
- plan, rol o tipo de cuenta;
- canal o fuente;
- región, dispositivo o workflow;
- exposición a una feature o intervención;
- categoría de caso, complejidad o volumen.

Para cada dimensión, declarar:

- hipótesis que ayuda a evaluar;
- decisión que podría cambiar;
- población y tamaño suficientes;
- riesgos de privacidad, equidad o proxies sensibles;
- posibilidad de diferencias de composición.

Evitar segmentar por todo atributo disponible. Demasiados cortes producen hallazgos accidentales y dificultan priorizar.

## Segmentation y unidades

Comprobar que los segmentos sean mutuamente interpretables y que la unidad sea consistente. No mezclar, por ejemplo, usuarios con cuentas ni atribuir a individuos un atributo definido a nivel organización.

Cuando un agregado cambia, distinguir:

- cambio real dentro de los segmentos;
- cambio en la proporción de segmentos;
- entrada o salida de poblaciones;
- cambio de definición o cobertura.

Un promedio global puede mejorar aunque un segmento crítico empeore, o viceversa.

## Comparaciones y baselines

Seleccionar el ancla según la pregunta:

- período anterior equivalente para tendencia operativa;
- mismo período estacional para patrones cíclicos;
- baseline previo a una intervención;
- target acordado para seguimiento de intención;
- cohorte a la misma edad para lifecycle;
- segmento comparable para diagnóstico.

Verificar que definición, ventana, población y madurez sean equivalentes. Anotar lanzamientos, cambios de mix, políticas, incidentes o calidad de datos que limiten la comparación, sin diseñar su representación visual.

Si no existe baseline, declararlo y recomendar crear uno antes de fijar conclusiones o targets. No reconstruir precisión ficticia.

## Análisis guiado por hipótesis

1. Formular el patrón observado sin explicar todavía su causa.
2. Enumerar pocas hipótesis que produzcan predicciones distintas.
3. Elegir dimensiones o métricas diagnósticas capaces de diferenciarlas.
4. Buscar evidencia que podría refutar, no solo confirmar, la explicación favorita.
5. Actualizar el nivel de confianza y decidir siguiente acción.

No crear una jerarquía de diagnósticos infinita. Priorizar por impacto potencial, plausibilidad, riesgo y coste de obtener evidencia.

## Explicaciones alternativas

Considerar cuando correspondan:

- estacionalidad o calendario;
- cambio de mix de usuarios, cuentas o canales;
- maduración incompleta de cohortes;
- lanzamiento, campaña, pricing o política concurrente;
- incidentes de fiabilidad o soporte;
- cambios de definición, cobertura o calidad de datos;
- selección, supervivencia o exposición desigual;
- regresión a la media y variación aleatoria;
- comportamiento estratégico o gaming.

No presentar esta lista completa en cada respuesta; elegir alternativas plausibles para el contexto.

## Guardrails en la interpretación

Leer outcomes y drivers junto con los guardrails relevantes. Si la métrica principal mejora:

- comprobar si calidad, coste, confianza o equidad empeoraron;
- revisar si el cambio se concentra en un actor o segmento;
- determinar si el resultado proviene de una redefinición o incentivo no deseado;
- evitar celebrar una mejora hasta entender trade-offs materiales.

Si un guardrail empeora, la respuesta depende del riesgo: detener, limitar, investigar o aceptar conscientemente el trade-off. Explicitar quién debe decidir.

## Observación, interpretación y causalidad

Usar lenguaje proporcional a la evidencia:

- **Observado:** describe el dato y la comparación.
- **Compatible con / sugiere:** expresa una interpretación aún abierta.
- **Asociado con:** reconoce correlación sin dirección causal.
- **Causó / produjo:** reservar para evidencia cuyo diseño soporte esa conclusión.

Una coincidencia temporal, diferencia entre segmentos o mejora de cohortes no demuestra por sí sola que una feature causó el resultado.

## Confianza y gaps

Declarar qué sostiene o limita la interpretación:

- definición acordada o todavía ambigua;
- cobertura y maduración de la población;
- comparabilidad del baseline;
- consistencia entre métricas o fuentes;
- alternativas no descartadas;
- evidencia observacional o causal disponible.

Puede usarse una etiqueta simple —baja, media o alta— solo si se explican sus razones. No convertirla en una puntuación falsa.

Registrar gaps como preguntas accionables: definición pendiente, target inexistente, segmento demasiado pequeño, ventana inmadura o dato no disponible. No resolverlos diseñando tracking, SQL o pipelines dentro de esta skill.

## Proponer acciones

Relacionar la acción con el nivel de evidencia:

- **Definición insuficiente:** alinear concepto, unidad o reglas antes de medir.
- **Señal temprana:** observar otra ventana o segmento y evitar una intervención irreversible.
- **Diagnóstico localizado:** probar una mejora acotada en el punto o población afectados.
- **Riesgo de guardrail:** limitar o detener optimización mientras se investiga.
- **Patrón consistente:** priorizar una intervención y definir cómo se evaluará.
- **Evidencia causal necesaria:** derivar a diseño experimental o análisis apropiado.

Toda acción debe indicar qué decisión habilita, qué supuesto conserva y qué resultado o guardrail se revisará después.

## Checklist de cierre

- La observación incluye población, ventana y comparación.
- Las dimensiones responden hipótesis y decisiones.
- Se consideraron cambios de composición y maduración.
- Las explicaciones alternativas relevantes están visibles.
- Los guardrails acompañan la lectura del outcome.
- El lenguaje causal coincide con la evidencia.
- La confianza y los gaps están explícitos.
- La acción es proporcional y tiene una métrica de seguimiento.
- No se recomendaron charts, layout, SQL, tracking ni implementación.
