# Contexto — Guía 3: Espacio de búsqueda y algoritmos ciegos (BFS, DFS, UCS)

## Qué pide el profesor
**Parte 1 — modelar el problema como espacio de búsqueda:**
1. Describir el contexto del problema del sector.
2. Definir los elementos del espacio de búsqueda (estados, acciones, costos, meta).
3. Representar **al menos 5 estados y transiciones** (diagrama o tabla).
4. Decidir **búsqueda en árbol o en grafo** y justificarlo.

**Parte 2 — modelar como grafo y comparar:**
1. Modelar el problema como grafo.
2. Aplicar **BFS, DFS y UCS**.
3. Comparar caminos (eficiencia, costo).
4. Justificar cuál algoritmo sirve más en el caso propio.

Fecha de presentación indicada: jueves 20.

## Finalidad dentro del curso
Es la guía que **convierte el sector en un grafo**. Aquí nace el modelo que se reutiliza en todas
las guías siguientes: la **red de pases** del equipo.

## Recursos (resumen para no releerlos)
- **`IA ALGORIT BUSQUEDA.md`** — qué es un agente de IA (percibir → decidir → actuar), tipos de
  agente, tipos de búsqueda (**no informada/ciega** vs **informada/heurística**), conceptos de grafos,
  criterios de comparación de algoritmos (completitud, optimalidad, complejidad temporal y espacial),
  y BFS / DFS / UCS paso a paso. Incluye un ejemplo completo en turismo (itinerarios con
  restricciones de satisfacción, tiempo y presupuesto) con órdenes de expansión de cada algoritmo.
- **`algoritmosbusqueda(1).ipynb`** — notebook base del profesor con las implementaciones de
  referencia de BFS, DFS y UCS.

**Ideas clave que hay que poder citar:**
- BFS: óptimo solo si todos los costos son iguales (mínimo número de saltos).
- DFS: ni completo ni óptimo en grafos con ciclos; se lanza por la primera rama.
- UCS: óptimo con costos no negativos (es Dijkstra), pero expande a ciegas en todas direcciones.
- Búsqueda en **grafo** (con lista de visitados) evita reexpandir estados repetidos; en **árbol** no.

## Qué entregamos (`entregables/`)
`Algoritmos_Busqueda_Futbol.ipynb`

- **Problema modelado:** jugada de construcción ofensiva desde la defensa (`DF`) hasta el
  delantero (`DL`).
- **Nodos = jugadores** (DF, LT, MCD, MC1, MC2, EX, DL), **aristas = pases**,
  **peso = riesgo de intercepción (escala 1–10)**.
- Se implementan BFS, DFS y UCS y se dibujan las tres rutas con `networkx` + `matplotlib`.
- Nota metodológica del notebook: los pesos son dinámicos; cambiar un peso y re-ejecutar recalcula
  todo.

⚠️ El notebook entregado está **incompleto en disco**: faltan las celdas con la definición de
`grafo`, `bfs`, `dfs`, `ucs` (se ejecutaron en clase pero no quedaron guardadas). La versión
completa y corregida de ese mismo modelo está en el entregable de la **guía 4**.

## Estado
✅ Presentada. El modelo definitivo (11 jugadores, formación 4-2-3-1) vive en la guía 4.

## Para recordar
Decisión de modelado del grupo: **búsqueda en grafo**, porque la red de pases tiene ciclos
(el balón puede volver atrás) y reexpandir estados repetidos sería absurdo en tiempo real.
