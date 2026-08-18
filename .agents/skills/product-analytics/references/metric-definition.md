# Definición de métricas

Usar esta referencia para convertir nombres ambiguos en definiciones conceptuales comparables y accionables. No diseñar eventos, SQL ni modelos físicos de datos.

## Registro mínimo

Para cada métrica principal, hacer explícitos los elementos necesarios de este contrato:

| Elemento | Contenido |
| --- | --- |
| Nombre y rol | Término no ambiguo y función como outcome, driver, diagnóstico o guardrail. |
| What | Fenómeno, población, unidad de análisis y ventana. |
| Why | Vínculo con objetivo, valor, decisión o riesgo. |
| How | Cálculo conceptual, agregación y reglas de inclusión o exclusión. |
| Compared to what | Período, baseline, target, cohorte, segmento o benchmark. |
| So what | Interpretación posible y decisión, acción o investigación habilitada. |

Agregar owner, cadence, dirección deseada, fuente o limitaciones cuando cambien el uso de la métrica. Una respuesta breve puede expresar el contrato en prosa; no exigir siempre una tabla.

## What: fenómeno y alcance

Precisar:

- **Población elegible:** quién podría razonablemente producir el resultado.
- **Unidad de análisis:** usuario, cuenta, equipo, sesión, caso, pedido, transacción u otra.
- **Comportamiento o resultado:** qué debe ocurrir para contar.
- **Ventana:** período de observación y, cuando corresponda, tiempo permitido desde un evento de origen.
- **Grano:** diario, semanal, mensual, por ciclo o por episodio según el comportamiento real.

No usar “usuarios”, “clientes”, “activos” o “conversión” sin definirlos. En B2B, decidir explícitamente si la lectura es por usuario o cuenta.

## Why: cadena de relevancia

Vincular la métrica con al menos uno de estos elementos:

- outcome que representa;
- driver cuya evolución se intenta gestionar;
- riesgo que funciona como guardrail;
- pregunta diagnóstica;
- decisión que cambiaría con la observación.

Si el vínculo depende de una hipótesis no validada, declararlo. Disponibilidad o popularidad no son razones suficientes.

## How: cálculo conceptual

### Conteos

Definir qué entidad se cuenta, si se deduplica y durante qué intervalo. Los acumulados históricos suelen requerir contexto de actividad o valor para evitar vanity metrics.

### Tasas y conversiones

Especificar:

- numerador;
- denominador elegible;
- relación temporal entre ambos;
- tratamiento de observaciones incompletas;
- unidad sobre la que se calcula la tasa.

No comparar tasas con denominadores o ventanas diferentes como si fueran equivalentes.

### Promedios y distribuciones

Declarar si se usa media, mediana, percentil o proporción bajo un umbral. Preferir una medida robusta o mostrar distribución cuando los extremos cambian la decisión.

### Ratios

Explicar por qué la relación entre magnitudes representa el fenómeno y qué ocurre cuando el denominador es pequeño o cero.

### Inclusión y exclusión

Definir casos como cuentas internas, pruebas, duplicados, cancelaciones, reintentos, reaperturas, datos tardíos o entidades todavía no maduras para la ventana. Registrar reglas relevantes aunque su implementación quede fuera de alcance.

## Compared to what

Elegir la comparación según la decisión:

- **Período previo comparable:** útil para seguimiento, respetando estacionalidad y ventanas equivalentes.
- **Baseline:** estado de referencia anterior a una intervención o al inicio de la medición.
- **Target:** nivel acordado que representa un resultado deseado dentro de un horizonte.
- **Cohorte o segmento:** comparación entre poblaciones cuya diferencia puede orientar una acción.
- **Benchmark externo:** usar solo con definición, población, producto y período suficientemente comparables.

Una comparación puede requerir más de un ancla, pero no agregarlas por rutina.

## Targets y benchmarks

No inventar cifras. Si falta un target:

1. Marcarlo como pendiente.
2. Proponer establecer una baseline con una ventana representativa.
3. Relacionar el futuro target con el outcome, capacidad de intervención, horizonte y guardrails.
4. Distinguir target aspiracional, compromiso operativo y threshold de alerta.

Tratar benchmarks externos como contexto, no como verdad normativa. Documentar fuente y diferencias que limiten la comparación.

## So what: gate de utilidad

Completar una o más frases operativas:

- “Si sube o baja materialmente, revisaremos…”
- “La diferencia entre estos segmentos indicaría investigar…”
- “Antes de actuar necesitamos descartar…”
- “Esta métrica permite decidir si…”

Si no existe respuesta, redefinir, convertir en diagnóstico exploratorio o eliminar la métrica. Evitar reglas automáticas cuando no hay suficiente evidencia.

## Owner y cadence

Incluirlos cuando la métrica forme parte de una revisión recurrente o un handoff operativo:

- **Owner:** rol o equipo responsable de revisar y decidir, no necesariamente quien produce los datos.
- **Cadence:** frecuencia coherente con la velocidad de cambio, maduración de la ventana y capacidad de respuesta.

No exigirlos para una exploración conceptual acotada. No proponer tiempo real si la decisión o el fenómeno cambian semanal o mensualmente.

## Ejemplo abstracto

“Adopción de capacidad” es ambiguo. Una definición más útil podría expresar:

- **What:** proporción de cuentas elegibles que completan una acción de valor dentro de los 14 días posteriores a la habilitación.
- **Why:** aproxima si la capacidad llega a integrarse en el workflow inicial.
- **How:** cuentas elegibles con acción de valor / cuentas elegibles con ventana madura; excluir cuentas internas.
- **Compared to what:** cohortes de habilitación y baseline del flujo anterior, si existe.
- **So what:** identificar si se debe revisar descubrimiento, onboarding o propuesta de valor antes de ampliar el rollout.

La acción de valor, la elegibilidad y la ventana deben validarse en el contexto real; el ejemplo no prescribe un KPI universal.

## Validar ambigüedad

Antes de cerrar una definición, comprobar:

- ¿Dos personas podrían calcular resultados diferentes usando el mismo nombre?
- ¿Se mezclan usuarios, cuentas, eventos o períodos?
- ¿La ventana deja observaciones inmaduras?
- ¿El denominador representa realmente quién tuvo oportunidad?
- ¿Cambiar una exclusión alteraría materialmente la interpretación?
- ¿La comparación utiliza la misma definición?
- ¿El “So what” conduce a una decisión defendible?

Registrar cualquier respuesta pendiente como gap de definición, no resolverla inventando precisión.
