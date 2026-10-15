# Eval 002 — Operational dashboard

## Scenario

Un equipo interno usa una vista durante toda la jornada para gestionar solicitudes. El caso prueba alta densidad razonable, lectura rápida, exceptions, acciones frecuentes y filtros con alcance comprensible.

## User request

> Organizá el dashboard operativo del equipo que recibe, asigna y resuelve solicitudes. Necesitan detectar bloqueos y actuar rápido; una vista demasiado resumida les hace perder tiempo.

## Expected activation

Sí. `dashboard-ux` debe activarse porque el pedido define una tarea operativa y solicita estructura, densidad, interacción y estados.

## Context

- Audiencia: coordinadores y agentes experimentados.
- Uso: continuo en desktop, con revisión rápida desde tablet durante guardias.
- Decisiones: qué solicitud atender, reasignar, escalar o desbloquear.
- Información acordada: estado, prioridad, antigüedad, SLA, owner, categoría, dependencia y última actualización.
- Señales agregadas: backlog válido, tiempo de espera y reaperturas.
- Excepciones: SLA en riesgo, solicitudes sin owner, bloqueos y datos stale.
- Acciones frecuentes: asignar, cambiar prioridad, escalar y abrir detalle.
- Filtros frecuentes: equipo, owner, prioridad y estado; búsqueda por código.
- Permisos: algunos casos sensibles solo muestran metadata limitada.

## Expected characteristics

- Identificar un modo operational y aceptar densidad cuando reduce navegación.
- Poner exceptions, status, próxima acción y contexto temporal al servicio de scanability.
- Distinguir overview operativo de lista de trabajo y detalle de caso.
- Justificar filtros por frecuencia y decisión; definir defaults, estado activo y reset.
- Mantener visible el efecto de filtros sobre agregados y lista.
- Elegir un detail pattern que conserve contexto y retorno.
- Contemplar loading localizado, stale, partial, error y permission-limited.
- Especificar keyboard access, focus, labels y non-color status.
- Ajustar la jerarquía para tablet sin eliminar campos críticos.

## Required concepts

- operational dashboard mode;
- appropriate high density;
- scanability;
- exception management;
- frequent actions;
- filter scope and reset;
- detail in context;
- states and freshness;
- responsive hierarchy;
- accessibility.

## Forbidden / undesirable behavior

- Convertir la vista en cuatro cards grandes y obligar a abrir cada solicitud.
- Aplicar “menos es siempre mejor” y eliminar owner, SLA o bloqueo.
- Diseñar todos los elementos como tiles equivalentes.
- Depender solo de rojo, amarillo y verde para status.
- Ocultar filtros activos o cambiar agregados sin hacerlo visible.
- Usar modals anidados para navegación profunda.
- Redefinir SLA, prioridad o throughput.
- Escribir código, SQL, eventos o componentes.

## Success criteria

1. La propuesta reduce el tiempo para detectar y resolver excepciones.
2. La densidad preserva jerarquía, legibilidad y consistencia.
3. Filtros, búsqueda, acciones y detail tienen propósito operativo explícito.
4. Estados y permisos no se confunden con cero o ausencia legítima de datos.
5. Desktop y tablet conservan información y acciones críticas.
