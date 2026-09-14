# Parcial Práctico 1 — Agente Integrador de IA Clásica

**Curso:** Inteligencia Artificial
**Integrantes:** Keiry Lucía Olaya Noguera · Harold Stiven Camargo Castellanos · Juan Felipe Coronel Montes
**Sector:** Rendimiento deportivo y analítica avanzada — gestión de carga del atleta

Un agente en Python que integra **Min-Max con poda α-β**, **planificación STRIPS** y una
**Red Bayesiana** para decidir cómo preparar a un futbolista en los 5 días previos a un partido.

---

## 1. Cómo ejecutar

### Requisitos

```bash
pip install matplotlib networkx pandas
```

Python 3.8 o superior. No hace falta nada más: el cálculo bayesiano, el Min-Max y el planificador
STRIPS están implementados a mano, sin librerías especializadas.

### Ejecución completa (lo normal)

```bash
python agente.py
```

Un solo comando genera **todo lo obligatorio**:

| Archivo | Qué contiene |
|---|---|
| `agent_log.txt` | Registro completo del flujo `observe → posterior → plan → decision → acción` (también se imprime en consola) |
| `minmax_tree.png` | Árbol de decisiones con el valor de cada nodo y la rama escogida resaltada |
| `strips_graph.png` | Grafo de estados con la ruta del plan resaltada y su leyenda |
| `bayes_bars.png` | Probabilidades calculadas y la evidencia utilizada |
| `agent_summary.png` | Síntesis: plan + probabilidad de éxito + decisión final |

### Los bloques extra del enunciado

```bash
python experimentos.py
```

| Archivo | Qué contiene |
|---|---|
| `resultados_bloque1.csv` | Comparación de heurísticas y poda: 4 escenarios × profundidades {2,3,4} × 4 versiones (48 filas) |
| `resultados_bloque2.csv` | Análisis de sensibilidad bayesiano: 5 valores del prior |
| `sensibilidad.png` | Posterior vs prior, con el umbral de decisión marcado |
| `experimentos_log.txt` | Las tablas y el análisis completo por escrito |

### Comprobar que todo está bien

```bash
python test_regresion.py
```

31 pruebas que verifican que los resultados siguen coincidiendo con los de las Guías 5 y 6.
Debe terminar con `TODAS LAS PRUEBAS PASAN`.

### Ejecutar un módulo suelto

Cada módulo funciona por separado y muestra sus propios resultados:

```bash
python dominio.py     # métricas, función de utilidad, verificación contra la Guía 5
python bayes.py       # las tres CPTs y las cuatro consultas + bayes_bars.png
python strips.py      # planes forward, backward, A*, bloqueos + strips_graph.png
python minmax.py      # árbol, poda y decisión + minmax_tree.png
```

---

## 2. Qué hace el agente

```
  observe    →    posterior    →    plan    →    decision    →    acción
 (sensores)      (Bayes)          (STRIPS)      (Min-Max)
```

1. **Observe.** Los sensores (HRV, sueño, carga GPS/IMU de Kinexon) detectan que el atleta llega
   **fatigado**.
2. **Posterior.** La red bayesiana calcula que, con esa evidencia, la probabilidad de éxito
   competitivo baja de **57.8 %** a **32.5 %** — y de paso, que es un **62.5 %** probable que la
   causa sea la carga que le pusimos (el prior era 40 %).
3. **Plan.** Como 32.5 % está por debajo del umbral de **40 %**, el agente **cambia la meta de
   STRIPS** a la versión conservadora, que además de dejarlo listo exige reserva energética.
   A\* encuentra un plan de **6 acciones** y **10 kg CO₂eq**.
4. **Decision.** Min-Max con poda α-β recomienda **carga moderada** y **descansar al jugador**,
   con un valor garantizado de **+19**.
5. **Acción.** Se emite la recomendación, dejando explícito que es una recomendación y no un
   veredicto.

**La bisagra es el umbral.** Es lo que hace que la red bayesiana *realmente* cambie el plan de
STRIPS. Sin él habría tres programas en la misma carpeta; con él hay un agente.

---

## 3. Evidencia utilizada

| Variable | Qué es | De dónde saldría en la vida real |
|---|---|---|
| **C** — Carga semanal (Alta / Moderada) | Cuánto se hizo entrenar al atleta | Planillas del cuerpo técnico |
| **F** — Fatiga (Alta / Baja) | Cómo respondió su cuerpo | HRV, calidad de sueño y carga acumulada (Kinexon, Catapult) |
| **E** — Éxito competitivo (Éxito / Fallo) | Si llega disponible y rinde | Registro histórico de disponibilidad y rendimiento |

**La evidencia concreta de la corrida por defecto es `F = Alta`**: biomarcadores alterados el
miércoles previo al partido. Aparece escrita dentro de `bayes_bars.png` y en la cabecera de
`agent_summary.png`.

---

## 4. Estructura de los archivos

```
entregables/
├── dominio.py             Métricas, función de utilidad, escenarios y constantes.
│                          Todo lo que comparten los tres métodos.
├── bayes.py               Red bayesiana C → F → E. Es la misma de la Guía 6.
├── strips.py              Acciones STRIPS, forward, backward, A*, detección de bloqueos.
├── minmax.py              Árbol procedural, poda α-β y heurística de evaluación.
├── agente.py              El flujo integrador. ← punto de entrada
├── experimentos.py        Los dos bloques extra del enunciado.
├── test_regresion.py      31 comprobaciones automáticas.
├── README.md              Este archivo.
└── explicacion_algoritmo.md   Cómo funciona, a alto y bajo nivel.
```

Los cuatro PNG obligatorios se generan **en esta misma carpeta**, con los nombres exactos que pide
el enunciado.

---

## 5. Parámetros que se pueden cambiar en vivo

Todos están al principio de `dominio.py`:

| Parámetro | Valor | Qué controla |
|---|---|---|
| `LAMBDA` | `1.0` | Peso del CO₂ metabólico en la utilidad. Con `λ ≥ 1.5` la mejor hoja del árbol cambia de *Jugar* a *Descansar* |
| `UMBRAL_EXITO` | `0.40` | Por debajo de esta probabilidad, el agente cambia a la meta conservadora |
| `PROFUNDIDAD` | `3` | Profundidad del Min-Max. El experimento demuestra que 3 es el mínimo útil |
| `W_RENDIMIENTO`, `W_CO2`, `W_RIESGO`, `W_RECUPERACION` | `4, 2, 3, 2` | Pesos de la función de utilidad |

Las CPTs de la red están al principio de `bayes.py`; el estado inicial, las metas y las acciones
STRIPS, al principio de `strips.py`.

**Cambiar cualquiera de ellos y volver a ejecutar recalcula todo**: tablas, análisis y figuras.
No hay ningún número escrito a mano en las salidas.

---

## 6. Resultados principales

### Min-Max

| | |
|---|---|
| Decisión | `Carga Moderada → Fatiga Alta → Descansar` |
| Valor garantizado | **+19** |
| Nodos: sin poda → con poda | 28 → 20 (**−29 %**) |

> La **mejor hoja** del árbol vale **+42** (`Carga Moderada + Fatiga Baja + Jugar`), pero Min-Max
> **no la elige**, porque MIN —el organismo— nunca concede la fatiga baja.
> **La decisión no es la mejor posible: es la mejor garantizada.**

### STRIPS

| Meta | Acciones | CO₂ |
|---|---|---|
| Estándar | 5 | 9 |
| Conservadora | 6 | 10 |

El plan tiene un **cerrojo**: `co2_acumulado(alto)` es precondición negativa del entrenamiento
específico, así que hasta que `Monitorear_Biomarcadores` no baja el CO₂, la acción de alta
intensidad está bloqueada. Eso es lo que fuerza el orden del plan.

La búsqueda forward *greedy* encuentra un plan de **CO₂ = 10** para la meta estándar; **A\*
encuentra uno de 9**. Es la razón de usar A\* y no encadenamiento simple.

### Redes Bayesianas

| Consulta | Valor |
|---|---|
| `P(E=Éxito)` sin evidencia | 57.8 % |
| `P(E=Éxito \| F=Alta)` | **32.5 %** |
| `P(E=Éxito \| F=Baja)` | 81.2 % |
| `P(C=Alta \| F=Alta)` diagnóstico | 62.5 % (prior 40 %) |

### Bloque extra 1 — heurísticas y poda

- La poda α-β da **exactamente la misma decisión y el mismo valor** que la versión básica en los
  12 casos. Es su garantía teórica, y aquí queda verificada.
- Ahorro de la poda: **−33 % de nodos** en total.
- La heurística diseñada **solo cambia la decisión a profundidad 2**. De profundidad 3 en adelante
  ambas coinciden.
- **La decisión se estabiliza en profundidad 3.** Con profundidad 2 el agente elige *Carga Baja*,
  porque no alcanza a ver que todavía puede **descansar** al jugador; sin esa mitigación, la única
  forma de protegerlo es entrenarlo menos. Con profundidad 4 la decisión no cambia y el coste sube
  de 28 a 64 nodos.

### Bloque extra 2 — sensibilidad bayesiana

| `P(C=Alta)` | `P(E=Éxito \| F=Alta)` | Meta STRIPS | Decisión Min-Max |
|---|---|---|---|
| 0.10 | 40.6 % | estándar (5 pasos) | Moderada |
| 0.25 | 35.9 % | conservadora (6 pasos) | Moderada |
| 0.40 | 32.5 % | conservadora | Moderada |
| 0.60 | 29.2 % | conservadora | Moderada |
| 0.80 | 26.8 % | conservadora | Moderada |

- **El plan cambia entre 0.10 y 0.25**: ahí el sistema es frágil.
- **De 0.25 en adelante es estable**: da igual afinar el prior, el agente siempre protege al atleta.
- **La decisión de Min-Max no se mueve nunca.** No es un defecto: Min-Max razona sobre el peor
  caso, no sobre probabilidades. Lo que se mueve es el plan de preparación, no la recomendación
  de carga.

---

## 7. De dónde sale cada cosa

| Elemento | Origen |
|---|---|
| Función de utilidad y las 8 hojas base | Guía 5, `Algoritmo_Rendimiento_deportivo.ipynb` |
| Estructura STRIPS y las 5 acciones base | Guía 5 |
| Red bayesiana y sus CPTs | Guía 6, `Red_Bayesiana_Rendimiento.ipynb` |
| Uso de A\* como motor de la planificación | Guía 4 + instrucción explícita del profesor en la Guía 5 |
| Cierre ético (*human-in-command*) | Guía 2, Marco Ético para la IA en Colombia (2021) |
| CO₂ metabólico como métrica | Guía 5 — GHG Protocol adaptado, Catapult Sports |

Los tres métodos corren sobre **el mismo dominio** y comparten `dominio.py`. No hay modelos
paralelos.
