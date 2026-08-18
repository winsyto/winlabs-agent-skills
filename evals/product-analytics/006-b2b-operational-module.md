# Eval 006 — B2B operational module

## Scenario

Una empresa utiliza un módulo interno para gestionar solicitudes operativas. Quiere mejorar velocidad y capacidad sin incentivar cierres apresurados ni confundir actividad con valor.

## User request

> Tenemos un módulo que usan empleados para recibir, asignar y resolver solicitudes internas. Queremos medir si el módulo hace más eficiente la operación, si fue adoptado y si estamos resolviendo más trabajo sin bajar la calidad. Definí las métricas principales.

## Expected activation

Sí. `product-analytics` debe activarse porque se solicita definir outcomes, drivers, adopción, eficiencia, throughput y guardrails para un workflow operativo.

## Context

- Actores: empleados solicitantes, agentes resolutores y responsables operativos.
- Unidad potencial: solicitud, agente, empleado o área.
- Las solicitudes tienen categorías y complejidades diferentes.
- Una solicitud cerrada puede reabrirse si la resolución fue incorrecta.
- Parte del trabajo todavía llega por canales externos al módulo.
- No existen baseline ni targets acordados.

## Expected characteristics

- Aclarar qué significa “resuelta” y distinguir cierre administrativo de resolución útil.
- Elegir explícitamente unidades para throughput, eficiencia, adopción y calidad.
- Relacionar outcomes con drivers sin afirmar causalidad.
- Definir throughput con período y población, evitando premiar volumen sin contexto.
- Medir tiempos con ventanas y distribuciones apropiadas, no solo un promedio global.
- Separar elegibilidad, primer uso y adopción sostenida del módulo.
- Incorporar guardrails como reaperturas, retrabajo, satisfacción o backlog envejecido cuando aporten valor.
- Proponer comparaciones por baseline, período y categorías de complejidad, sin inventar targets.

## Required concepts

- operational outcome;
- efficiency;
- throughput;
- adoption;
- quality;
- drivers;
- guardrails;
- unit of analysis;
- comparison context.

## Forbidden / undesirable behavior

- Tratar cantidad de cierres como outcome suficiente.
- Usar logins o clicks como adopción significativa.
- Optimizar tiempo de resolución sin calidad o backlog.
- Comparar agentes o áreas sin considerar mix de complejidad.
- Inventar SLA, baseline o target.
- Recomendar dashboard layout, charts, SQL, tracking o implementación.

## Success criteria

1. Eficiencia, throughput, adopción y calidad tienen definiciones y decisiones diferenciadas.
2. Las unidades, poblaciones y ventanas críticas están claras.
3. Los guardrails evitan incentivar cierres rápidos o selectivos sin valor.
4. Las comparaciones reconocen complejidad y canales externos.
5. El output permite decidir dónde intervenir o qué falta validar.
