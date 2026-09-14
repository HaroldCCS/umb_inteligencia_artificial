# Contexto — Guía 4: Búsqueda heurística (Greedy, A*, Weighted A*)

## Qué pide el profesor
Definir las **heurísticas propias del sector** y evaluarlas en 4 retos:

1. **Comparativa de rendimiento** — grafo sectorial; implementar **Greedy, A\* y Weighted A\***
   (w sugerido 1.5 y 2, ajustable al sector); medir **nodos expandidos** y **longitud del camino**;
   tabla comparativa.
2. **Ajuste del peso (trade-off)** — Weighted A\* con `w = 1, 1.2, 1.5, 2, 3`; graficar
   *costo vs w* y *nodos expandidos vs w*; responder qué peso da el mejor balance.
3. **Escenario dinámico** — simular un cambio (bloquear un nodo, encarecer una arista); recalcular
   con cada algoritmo; analizar cuál se adapta mejor y qué pasa con los costos. Tabla + reflexión.
4. **Aplicación práctica en el sector** — implementar Weighted A\* en el contexto propio y
   **justificar el peso elegido**.

## Finalidad dentro del curso
Es la guía **técnicamente más fuerte del grupo** y la base del motor de búsqueda que el profesor
pide reutilizar en STRIPS ("usen el algoritmo de búsqueda que identificaron como más eficiente").

## Recursos (resumen)
- **`ALGOR HEURISTICA.md`** — Greedy Best-First (`f = h`), A\* (`f = g + h`), IDA\*,
  Weighted A\* (`f = g + w·h`, w > 1), RBFS; ejemplo completo S→G paso a paso; caso turístico con
  cola de prioridad visualizada; y una sección clave: **cómo diseñar buenas heurísticas**
  (admisibilidad, consistencia, relajación del problema, informatividad).
- **`HeuristicAlgm.ipynb`** — notebook de referencia del profesor con esos algoritmos.

**Ideas clave:** heurística **admisible** = `h(n) ≤ h*(n)` (nunca sobreestima) → A\* óptimo;
**consistente/monótona** = `h(n) ≤ c(n,n') + h(n')` → no hay que reexpandir nodos;
Weighted A\* con h admisible garantiza `costo ≤ w · C*` (suboptimalidad acotada).

## Qué entregamos (`entregables/`)
`Algoritmos_Busqueda_Futbol_ Actualizado.ipynb` — 34 celdas, notebook completo y ejecutable.

**Modelo definitivo del proyecto (usar SIEMPRE este):**
- 11 nodos = jugadores en 4-2-3-1: `POR, LTI, DFI, DFD, LTD, MC1, MC2, EXI, MO, EXD, DL`.
- Aristas = pases; peso = **riesgo de intercepción (1–10)** medido por análisis de video.
- `zona`: POR=0, defensas=1, pivotes=2, último tercio=3, DL=4.
- **Heurística:** `h(n) = (4 − zona(n)) × RIESGO_MIN_POR_PASE`, con `RIESGO_MIN_POR_PASE = 2`.
  Lectura futbolística: *"en el mejor caso, cada pase que falta saldría tan limpio como el mejor
  pase que este equipo sabe dar"*. Es una **relajación** → admisible y consistente (se demuestra
  en el notebook con Dijkstra invertido).
- `INICIO = 'POR'`, `OBJETIVO = 'DL'`.

**Resultados que hay que recordar (partido normal):**
| Algoritmo | Jugada | Riesgo | Nodos |
|---|---|---|---|
| A\* (w=1.0) | POR→DFI→MC1→MO→DL | **9 = C\*** | 11 |
| Weighted A\* w=1.2 | igual que A\* | 9 | 7 |
| Weighted A\* w=1.5 | (sale por el otro central) | 10 (+11 %) | 6 |
| Greedy | POR→DFD→MC2→EXD→DL | 16 | 5 |

- **Trampa de Greedy:** los extremos (`EXI`, `EXD`) tienen `h` bajísimo por estar pegados al área,
  pero su único pase al `DL` es un centro con riesgo 8–9. Greedy manda centrar; A\* no cae porque
  mira `g(n)`.
- **Reto 2:** el mejor balance es **w = 1.2** (óptimo con −36 % de cómputo). La curva **no es
  monótona** (en w=1.3 los nodos suben) → *el w se mide, no se deduce*.
- **Reto 3 (dinámico):** escenario A = marca personal sobre `MO` (+5 a todo pase hacia MO);
  escenario B = `MO` sale del campo. En ambos `C*` pasa de **9 a 14** y el óptimo cambia a
  `POR→LTI→EXI→DL`. **A\* se adapta; Greedy no reacciona en absoluto** porque el cambio ocurrió en
  `g` y Greedy solo mira `h`. Lección: *la adaptabilidad viene de g(n), no de h(n)*.
- **Reto 4:** producto = **asistente táctico de banquillo** (tablet, respuesta < 1 s). Se calibra
  `w` sobre los 10 orígenes posibles de recuperación y se elige **w = 1.5**: −27 % de cómputo,
  desvío medio 1.1 %, peor caso +11 %, con garantía formal `costo ≤ 1.5 · C*`.
- Advertencia registrada: para los últimos minutos yendo a perder **no se sube w**, se **cambia la
  función de costo**. Subir w degrada la búsqueda, no cambia el objetivo.

## Estado
✅ Desarrollada y entregada. Es el entregable de mayor calidad; sirve de plantilla de estilo
(tablas comparativas + lectura del sector después de cada resultado).
