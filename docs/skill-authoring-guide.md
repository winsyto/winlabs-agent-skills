# Guía de autoría de skills

## 1. Definir antes de escribir

1. Formular una sola capacidad y ejemplos concretos que deban activarla.
2. Delimitar solicitudes cercanas que no debe atender.
3. Identificar inputs disponibles, supuestos permitidos y output observable.
4. Decidir si crear y revisar requieren skills separadas.
5. Confirmar que la capacidad pertenece al catálogo y milestone actuales.

## 2. Diseñar el contenido

Mantener en `SKILL.md` solo instrucciones esenciales. Crear una referencia cuando el detalle sea extenso o condicional, un script cuando una operación repetida requiera determinismo y un asset cuando deba reutilizarse en el resultado. No crear carpetas preventivamente.

Todo `SKILL.md` maduro debe cubrir:

- propósito;
- cuándo utilizar y cuándo no utilizar;
- inputs esperados y manejo de faltantes;
- workflow;
- output esperado;
- criterios de calidad;
- anti-patterns.

El frontmatter admite solo `name` y `description`. Concentrar en `description` las señales de activación porque es el nivel disponible para descubrir la skill.

## 3. Escribir para portabilidad

- Usar instrucciones accionables y agnósticas respecto del agente.
- Evitar datos, herramientas o convenciones de un consumidor particular.
- Declarar decisiones y grados de libertad; no imponer pasos rígidos sin necesidad.
- Enlazar las referencias desde `SKILL.md` e indicar bajo qué condición cargarlas.
- Preferir síntesis original; registrar fuentes externas y verificar licencias.

## 4. Diseñar evals

Crear casos en `evals/<skill>/` que especifiquen prompt o escenario, contexto mínimo, comportamiento esperado y criterios de aceptación. Cubrir al menos:

- activación y resultado esperado;
- no activación o derivación correcta;
- inputs incompletos;
- caso límite representativo;
- cumplimiento de portabilidad y formato.

Evaluar propiedades semánticas y observables en vez de exigir texto literal. Mantener fixtures fuera de la skill salvo que formen parte de su operación real.

## 5. Revisar y publicar

1. Validar nombre, frontmatter, enlaces y estructura.
2. Ejecutar las evals disponibles y registrar limitaciones.
3. Revisar concisión, duplicación, supuestos específicos y anti-patterns.
4. Solicitar una revisión separada cuando la complejidad o el impacto lo ameriten.
5. Actualizar catálogo y changelog.
6. Clasificar el cambio según Semantic Versioning antes de publicar.

## Definition of Done

Una skill deja de ser esqueleto cuando su contrato está acordado, sus recursos son necesarios y localizables, sus evals cubren éxito y límites, y la documentación de catálogo refleja su estado real.