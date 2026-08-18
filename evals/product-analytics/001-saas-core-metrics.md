# Eval 001 — SaaS core metrics

## Scenario

Una empresa B2B SaaS joven quiere acordar sus métricas centrales. El objetivo es suficientemente abierto como para tentar al agente a devolver una lista estándar de SaaS KPIs.

## User request

> Tenemos un SaaS de gestión de proyectos para estudios profesionales. Queremos crecer sin perder calidad, pero hoy cada equipo mira números distintos. Definí las métricas principales que deberíamos seguir.

## Expected activation

Sí. `product-analytics` debe activarse porque la solicitud requiere traducir un objetivo abierto en una jerarquía y definiciones de métricas.

## Context

- Clientes: estudios profesionales con cuentas multiusuario.
- Valor esperado: coordinar trabajo y completar proyectos con menos retrasos.
- Modelo de negocio: suscripción por cuenta con planes por tamaño.
- Etapa: crecimiento temprano; no existe una North Star acordada.
- Datos conocidos: cuentas, usuarios, proyectos y estados de tareas.
- Datos desconocidos: baseline de retención, target de activación y benchmarks comparables.

## Expected characteristics

- Reformular el objetivo y distinguir usuario, cuenta y proyecto como posibles unidades.
- Identificar decisiones que las métricas deben apoyar.
- Proponer pocos outcomes de usuario/producto y conectar, sin confundir, resultados de negocio.
- Evaluar una North Star como opción; no imponerla.
- Construir una jerarquía de outcomes, drivers, diagnósticos y guardrails.
- Definir cada métrica principal con What, Why, How, Compared to what y So what.
- Explicitar que targets y benchmarks están pendientes.
- Incluir supuestos y gaps de datos sin diseñar tracking.

## Required concepts

- outcome y business outcome;
- drivers o inputs;
- activation basada en valor;
- retention por cuenta o cohorte cuando corresponda;
- engagement significativo, no actividad genérica;
- quality o guardrails;
- comparaciones y baseline;
- unidad de análisis.

## Forbidden / undesirable behavior

- Lista genérica de MRR, ARR, DAU, CAC, LTV y churn sin cadena de decisión.
- Declarar una North Star definitiva sin validar el valor entregado.
- Inventar targets o benchmarks de industria.
- Confundir usuarios activos con cuentas retenidas.
- Recomendar herramientas, eventos, SQL, charts o layout.
- Afirmar relaciones causales entre drivers y outcomes.

## Success criteria

1. La respuesta permite entender qué decisiones habilita cada métrica principal.
2. Las unidades y ventanas críticas están conceptualmente definidas.
3. Outcomes, drivers y guardrails son distinguibles y no redundantes.
4. Los supuestos y datos faltantes quedan visibles.
5. El sistema propuesto es más pequeño y específico que una lista estándar de SaaS KPIs.
