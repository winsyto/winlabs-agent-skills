# Eval 008 — Multi-actor workflow

## Scenario

Una plataforma coordina un workflow entre dos actores cuyos objetivos pueden entrar en tensión. El caso prueba si la skill evita reducir el sistema a una métrica global de volumen.

## User request

> Nuestra plataforma conecta organizaciones que publican solicitudes con especialistas que las aceptan y resuelven. Queremos una jerarquía de métricas para mejorar el funcionamiento general sin favorecer a un lado a costa del otro.

## Expected activation

Sí. `product-analytics` debe activarse porque se requiere diseñar outcomes por actor, una jerarquía métrica y guardrails para trade-offs de un producto multi-actor.

## Context

- Actores principales: organizaciones solicitantes y especialistas.
- Un especialista puede rechazar solicitudes poco atractivas o fuera de su capacidad.
- Las organizaciones valoran velocidad, calidad y previsibilidad.
- Los especialistas valoran demanda pertinente, compensación y carga sostenible.
- La plataforma obtiene ingresos cuando una solicitud se resuelve.
- Aumentar el volumen publicado no garantiza matching ni resolución.

## Expected characteristics

- Identificar unidades distintas: organización, especialista, solicitud y resolución.
- Definir outcomes específicos para cada actor y un outcome de salud del intercambio.
- Evitar una North Star única si oculta desequilibrios.
- Relacionar drivers como matching, aceptación, tiempo y resolución con hipótesis explícitas.
- Incorporar guardrails para calidad, concentración, carga, rechazos o inequidad de acceso.
- Proponer dimensiones diagnósticas solo cuando cambian una decisión.
- Explicar trade-offs y acciones sin presentar correlaciones como causalidad.
- Vincular el outcome de negocio con valor bilateral sin convertir revenue o volumen en objetivo único.

## Required concepts

- multi-actor outcomes;
- unit of analysis;
- metric hierarchy;
- drivers;
- trade-offs;
- guardrails;
- diagnostic dimensions;
- business outcome;
- gaming risk.

## Forbidden / undesirable behavior

- Elegir solicitudes publicadas, transacciones o revenue como única métrica global.
- Mezclar organizaciones, especialistas y solicitudes en un denominador ambiguo.
- Optimizar velocidad ignorando calidad o carga del especialista.
- Asumir que más aceptación siempre es mejor.
- Proponer segmentos sin hipótesis o acción.
- Recomendar layout, charts, SQL, tracking, schemas o implementación.

## Success criteria

1. Cada actor tiene outcomes y unidades explícitas.
2. La jerarquía representa intercambio, drivers y resultados de negocio sin simplificación engañosa.
3. Los guardrails hacen visibles los principales trade-offs.
4. Ninguna métrica de volumen sustituye el valor bilateral.
5. El output habilita decisiones diferenciadas para matching, calidad, capacidad o equilibrio.
