# Contexto — Parcial Práctico 1: Agente Integrador de IA Clásica

## Qué pide el profesor (resumen exacto de `actividad.md`)

Aplicar **Min-Max, STRIPS y Redes Bayesianas** en el sector y entregar **un agente sencillo en
Python que integre los tres métodos**.

### Entregables obligatorios
1. **Presentación** (parte conceptual).
2. **Código Python ejecutable** (script o notebook) comentado + **README** con instrucciones de ejecución.
3. **Visualizaciones PNG con nombres EXACTOS**:
   - `minmax_tree.png`
   - `strips_graph.png`
   - `bayes_bars.png`
   - `agent_summary.png`
4. **Registro de ejecución** impreso en consola **y** en `agent_log.txt`.
5. **Demo en clase de 5 minutos** (≈15 min por grupo en total).

### Requerimientos de visualización (no negociables)
- **Min-Max:** árbol con **todos los nodos y hojas mostrando su valor evaluado**; **rama escogida
  resaltada** (color/anchura distinta); **etiquetas** que dejen claro qué movimiento es cada rama.
- **STRIPS:** grafo de estados (nodo = estado o proposición compuesta); **ruta del plan resaltada**;
  **leyenda** con estado inicial, metas y plan.
- **Bayes:** gráfico de **barras** con las probabilidades calculadas (`P(H1|evidencia)`, …);
  ejes y etiquetas claras; **la evidencia usada debe aparecer** en el gráfico o en el README.
- **Agente integrador:**
  - Salida textual completa del flujo `observe → posterior → plan → decision → acción`
    en consola y en `agent_log.txt`.
  - `agent_summary.png` debe combinar **en una sola figura**: (1) el plan de STRIPS como mini-grafo
    o lista visual, (2) la probabilidad de éxito bayesiana como mini-barras o número destacado,
    y (3) la decisión final de Min-Max de forma **muy visible**, con la rama seleccionada
    superpuesta al plan si procede.
  - *"A primera vista debe verse: qué plan propuso, qué probabilidad asignó al éxito y qué decisión
    tomó."*

### Bloque extra 1 — Comparación de heurísticas y poda en Min-Max
Comparar **(i) Min-Max naive** (búsqueda completa hasta cierta profundidad),
**(ii) Min-Max + poda α-β**, **(iii) Min-Max + heurística de evaluación propia** (y opcionalmente
heurística + α-β).
- Ejecutar en **3 escenarios representativos** del sector y profundidades **{2, 3, 4}**.
- Registrar **tiempo, nodos expandidos y decisión escogida**.
- Si la decisión varía entre versiones, analizar si la heurística mejora o empeora el resultado.

### Bloque extra 2 — Análisis de sensibilidad bayesiano
- Elegir **4–6 valores** para el/los prior(s) relevante(s) (ej. `P(Severe) = [0.01, 0.05, 0.1, 0.2, 0.4]`).
- Para cada prior: recalcular posteriores con la **misma evidencia**, ejecutar el flujo completo
  del agente (`observe → plan → decide`) y registrar resultados.
- Comparar y discutir **estabilidad vs fragilidad** de las decisiones, incluyendo si el cambio de
  posterior altera el **objetivo de STRIPS** o la **decisión de Min-Max**.

## Finalidad dentro del curso
Es el **cierre del corte 1**: obliga a unir todo lo visto (grafo del sector, heurística A\*,
Min-Max, STRIPS, Bayes) en un solo agente que percibe, razona, planifica, decide y actúa.

## Recursos
Carpeta `recursos/` inexistente. **Todo el material conceptual sale de guías anteriores:**
- Min-Max + α-β + función de utilidad → `../guia 5/recursos/PLANIFICACION-MAX MIN.md`
- STRIPS + forward/backward + Sussman → `../guia 5/recursos/Planificación STRIPS.md`
- Redes bayesianas + CPTs + tipos de razonamiento → `../guia 6/recursos/PLANIFIC BAYESIANO.md`
- Motor de búsqueda A\* / Weighted A\* → `../guia 4/` (entregable y recursos)

## 📅 Fecha de entrega
**Jueves 17 de septiembre de 2026.**

## Estado
✅ **DESARROLLADO** (14-sep-2026). Código completo, verificado y ejecutable.

### Qué entregamos (`entregables/`)

**Código** — 7 módulos, sin librerías nuevas (`matplotlib`, `networkx`, `pandas`):
| Archivo | Qué hace |
|---|---|
| `dominio.py` | Métricas, función de utilidad, escenarios, constantes ajustables |
| `bayes.py` | Red bayesiana C→F→E (la misma de la guía 6) |
| `strips.py` | Acciones STRIPS, forward, backward, **A\***, detección de bloqueos |
| `minmax.py` | Árbol procedural, poda α-β, heurística de evaluación |
| `agente.py` | **Punto de entrada.** Flujo integrador completo |
| `experimentos.py` | Los dos bloques extra |
| `test_regresion.py` | 31 comprobaciones — todas pasan |

**Documentos:** `README.md` (cómo ejecutar) · `explicacion_algoritmo.md` (alto y bajo nivel).

**Salidas:** los 4 PNG con nombres exactos + `agent_log.txt` + `sensibilidad.png` +
`experimentos_log.txt` + los dos CSV.

`python agente.py` genera todo lo obligatorio de una sola ejecución.

### Resultados
| | |
|---|---|
| Min-Max | `Carga Moderada → Fatiga Alta → Descansar`, valor **+19**, nodos 28→20 (−29 %) |
| STRIPS | plan estándar 5 acciones / CO₂ 9 · conservador 6 / CO₂ 10 |
| Bayes | `P(E=Éxito)` 57.8 % → **32.5 %** con evidencia `F=Alta` |
| Contraste | Min-Max garantiza **+19**, Bayes espera **+35.1**. Coinciden en la decisión |

### Hallazgos de los bloques extra
1. **α-β da idéntica decisión y valor que la versión básica en los 12 casos** — su garantía
   teórica, verificada. Ahorro: −33 % de nodos.
2. **La decisión se estabiliza en profundidad 3.** Con profundidad 2 el agente elige *Carga Baja*
   porque no alcanza a ver que todavía puede **descansar** al jugador; sin esa mitigación, la
   única forma de protegerlo es entrenarlo menos. Con profundidad 4 la decisión no cambia y el
   coste sube de 28 a 64 nodos. → **profundidad 3 es la configuración correcta**.
3. **La heurística solo cambia la decisión a profundidad 2.** La lección no es que una evaluación
   sea superior, sino que ninguna heurística compensa cortar la búsqueda demasiado pronto.
4. **Sensibilidad:** el plan cambia solo entre prior 0.10 y 0.25; de ahí en adelante es estable.
   **La decisión de Min-Max no se mueve nunca** — no es defecto: Min-Max razona sobre el peor
   caso, no sobre probabilidades.
5. **A\* mejora al encadenamiento forward:** CO₂ 9 vs 10 en la meta estándar.
6. **Anomalía de Sussman demostrada, no afirmada:** el planificador lineal se bloquea si resuelve
   `atleta(recuperado)` antes que `reserva_energetica(alta)`, porque `Ajustar_Plan_Nutricional`
   borra `atleta(en_recuperacion)` y esa precondición ya no se puede recuperar.

### Pendiente
- [ ] Presentación conceptual (Gamma) — ver `planeacion.md` §8 para el guion de 5 min.
- [ ] Ensayar la demo cronometrada.
- [ ] `pip install matplotlib networkx pandas` en el equipo donde se haga la demo.
