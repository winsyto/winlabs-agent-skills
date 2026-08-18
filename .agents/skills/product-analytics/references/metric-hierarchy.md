# Jerarquía de métricas

Usar esta referencia para diseñar o revisar la relación entre outcomes, drivers, diagnósticos y guardrails. No tratar ninguna estructura como obligatoria.

## Empezar por el outcome

Formular el cambio observable que indicaría progreso para el actor y el alcance analizados. Mantener separados cuando sea necesario:

- **Outcome de usuario:** valor o resultado que obtiene el actor.
- **Outcome de producto:** comportamiento o resultado dentro del producto asociado con ese valor.
- **Outcome de negocio:** resultado económico u organizacional sostenible.

No asumir que actividad equivale a valor ni que un resultado de negocio explica por sí mismo cómo mejorar el producto.

## Roles dentro de la jerarquía

### Outcome metric

Representar el resultado que se intenta conseguir. Puede ser lagging respecto de una intervención y aun así ser la referencia que evita optimizar actividad sin valor.

### Driver o input metric

Representar un comportamiento o condición que el equipo puede influir y que plausiblemente contribuye al outcome. Registrar esa relación como hipótesis hasta que exista evidencia suficiente.

### Diagnostic metric

Ayudar a localizar dónde, cuándo o para quién cambia un outcome o driver. No promover automáticamente cada diagnóstico a KPI permanente.

### Guardrail metric

Detectar un daño o trade-off que podría quedar oculto al optimizar otra métrica: calidad, confianza, coste, equidad, seguridad, fiabilidad o el outcome de otro actor.

El rol depende del alcance. Una métrica puede ser outcome para una feature y driver para el producto completo; declarar siempre su rol en el sistema actual.

## North Star opcional

Considerar una North Star cuando una métrica candidata:

- expresa valor entregado, no mera exposición o actividad;
- puede ser influida por decisiones de producto;
- mantiene una relación defendible con resultados sostenibles;
- es suficientemente estable para alinear equipos;
- no puede crecer fácilmente destruyendo el valor que pretende representar.

No usar una North Star cuando:

- existen varios actores con intercambios de valor que una cifra ocultaría;
- el alcance es una feature o workflow acotado;
- el producto es demasiado temprano para reconocer un comportamiento de valor estable;
- un único agregado escondería calidad, riesgo o segmentos críticos;
- el modelo de uso es episódico y la frecuencia dominaría indebidamente la lectura;
- la organización necesita primero acordar varios outcomes balanceados.

En esos casos, preferir un conjunto pequeño de outcomes explícitos. No usar revenue, usuarios activos o volumen como North Star por defecto; evaluarlos con los mismos criterios.

## Leading y lagging son relativos

Clasificar una métrica respecto de una decisión y un horizonte, no de manera universal:

- una métrica **leading** cambia antes que el outcome de interés y puede orientar intervención temprana;
- una métrica **lagging** confirma un resultado después de que los drivers ya cambiaron.

Una métrica puede ser leading para un resultado anual y lagging para una acción semanal. Mantener ambos tipos cuando ayuden a intervenir y comprobar si la intervención produjo el resultado esperado.

## Construir un metric tree

1. Escribir el objetivo y las decisiones fuera del árbol.
2. Colocar arriba uno o pocos outcomes del alcance.
3. Preguntar qué comportamientos o condiciones plausiblemente mueven cada outcome.
4. Añadir solo drivers influenciables y conceptualmente distintos.
5. Incorporar diagnósticos donde un agregado pueda ocultar el problema.
6. Añadir guardrails según riesgos concretos.
7. Marcar cada relación como hipotética, observada o respaldada por evidencia más fuerte.
8. Revisar si cada rama conduce a una decisión diferente; fusionar o eliminar lo redundante.

El árbol no es una ecuación salvo que la relación matemática esté definida. Flechas o niveles expresan una teoría de funcionamiento, no causalidad probada.

## Productos multi-actor

Para marketplaces, plataformas o workflows con varios roles:

1. Identificar el valor que recibe cada actor.
2. Definir unidades distintas si corresponde, por ejemplo usuario, cuenta, proveedor o transacción.
3. Representar los intercambios: el crecimiento de un lado puede deteriorar espera, calidad o acceso del otro.
4. Elegir outcomes por actor y guardrails que protejan el equilibrio.
5. Evitar agregados que permitan que un grupo grande o activo esconda el deterioro de otro.

No combinar poblaciones o denominadores solo para obtener una métrica única.

## Gaming y guardrails

Para cada outcome o driver prioritario, preguntar:

- ¿Cómo podría aumentar sin mejorar el valor real?
- ¿Qué coste o daño podría crecer al mismo tiempo?
- ¿Quién podría beneficiarse o perjudicarse de forma desigual?
- ¿Qué comportamiento del equipo incentivaría esta métrica?

Elegir guardrails que detecten riesgos plausibles y tengan una respuesta asociada. No agregar guardrails genéricos que nadie revisará.

## Revisión de la jerarquía

- Cada nivel tiene una responsabilidad distinguible.
- Outcomes y drivers no son sinónimos renombrados.
- Las relaciones inciertas están declaradas.
- La North Star, si existe, supera criterios explícitos.
- Las unidades no se mezclan silenciosamente.
- Los guardrails corresponden a riesgos reales.
- La jerarquía es mínima: una nueva métrica debe mejorar una decisión o diagnóstico.
