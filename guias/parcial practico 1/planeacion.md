# Planeación — Parcial Práctico 1

> ⚠️ **Versión 2** — reescrita tras la actualización del entregable de la guía 5.
> 📅 **ENTREGA: jueves 17 de septiembre de 2026.** Hoy es lunes 14 → **quedan 3 días.**
> La buena noticia: con la guía 5 terminada, **ya existe cerca del 60 % del código**.

---

## 0. Idea central: un solo dominio, tres métodos

El parcial se construye sobre el **Dominio B** de la guía 5: **gestión de carga y preparación del
atleta antes del partido**. Ahí ya viven el Min-Max y el STRIPS, así que no hay que reconstruir nada.

| Método | Pregunta que responde | Estado |
|---|---|---|
| **Min-Max + α-β** | *"El organismo responde a cada carga que le pongo: ¿qué decido asumiendo la peor respuesta?"* | ✅ existe (guía 5, capa 1) |
| **STRIPS** | *"¿Qué secuencia de acciones lleva al atleta de fatigado a listo para competir?"* | ✅ existe (guía 5, capa 2) |
| **Redes Bayesianas** | *"¿Qué tan probable es realmente esa respuesta del organismo y ese éxito?"* | 🔴 por hacer (guía 6) |
| **Agente integrador** | `observe → posterior → plan → decision → acción` | 🔴 por hacer |

### El argumento que une todo (es el corazón de la exposición)
- El **Min-Max** trata al organismo como un **adversario perfecto**: siempre concede la fatiga que
  más perjudica. Por eso el agente se conforma con **+19 garantizado** en vez del **+42** de la
  mejor hoja.
- La **red bayesiana** le pone **probabilidad** a ese mismo nodo MIN: la fatiga alta no es segura,
  es un 48 %.
- El **STRIPS** es lo que el agente hace para **cambiar esa probabilidad**: bajar el CO₂ acumulado
  y recuperar al atleta.

> **Min-Max da la decisión garantizada. Bayes da la decisión esperada. STRIPS es el plan para pasar
> de una a la otra.** Ese es el mensaje de cierre.

---

## 1. Módulo Bayesiano (`bayes.py`) — 🔴 nuevo

Ver `../guia 6/planeacion.md`: **es la misma red**, no se construyen dos.

`C` = Carga semanal (Alta/Moderada) → `F` = Fatiga (Alta/Baja) → `E` = Éxito competitivo.
Son **las mismas variables de los niveles 1 y 2 del árbol Min-Max**.

**Resultados ya calculados y verificados (sirven de test de regresión):**

| Consulta | Valor |
|---|---|
| `P(E=Éxito)` marginal | **57.8 %** |
| `P(E=Éxito \| C=Moderada)` | **73.0 %** |
| `P(E=Éxito \| C=Alta)` | **35.0 %** |
| `P(E=Éxito \| F=Alta)` ← la que usa el agente | **32.5 %** |
| `P(E=Éxito \| F=Baja)` | **81.2 %** |
| `P(F=Alta)` | **48.0 %** |
| `P(C=Alta \| F=Alta)` (diagnóstico) | **62.5 %** |

**`bayes_bars.png`:** barras de `P(E=Éxito)` en los escenarios de evidencia (sin evidencia /
C=Moderada / C=Alta / F=Alta), más `P(C=Alta|F=Alta)`. Escribir la evidencia **dentro** de la
figura, como exige el enunciado.

---

## 2. Módulo STRIPS (`strips.py`) — ✅ portar desde la guía 5

Se copia tal cual de la guía 5: S0, meta G, las 5 acciones con `co2_costo`, forward, backward,
detección de interferencias/huérfanas/Sussman y el grafo espejo.

### Cambios necesarios
1. **Arreglar `busqueda_forward`**: devolver siempre 5 elementos (hoy devuelve 4 si falla → revienta
   el desempaquetado).
2. **Meta variable según Bayes** — es lo que convierte el módulo en parte de un agente:
   ```python
   if posterior_exito >= UMBRAL:      # UMBRAL = 0.40
       meta = META_BASE                                   # plan estándar de 5 días
   else:
       meta = META_BASE | {"carga_semanal(optima)"}       # plan conservador: exige descarga extra
   ```
3. **Motor A\*** (requisito explícito del profesor: *"implementen el algoritmo de búsqueda que
   identificaron como el más eficiente"*):
   - Nodo = estado STRIPS (`frozenset` de predicados).
   - Sucesores = acciones aplicables; `(estado − DELETE) | ADD`.
   - `g(n)` = CO₂ acumulado del plan.
   - `h(n)` = **nº de predicados de la meta que aún faltan × CO₂ mínimo por acción (=1)**.
     Es una **relajación** (suponer que cada predicado faltante se logra con la acción más barata)
     → **admisible**, mismo argumento que la heurística de la guía 4.
   - Si falta tiempo, la búsqueda forward greedy de la guía 5 ya produce el plan correcto; A\* es
     el que hay que añadir para cumplir el requisito. **No saltárselo: el profesor lo pidió por
     escrito.**
4. **`strips_graph.png`:** el grafo espejo de la guía 5 ya sirve; hay que añadirle lo que el
   enunciado exige explícitamente: **leyenda con estado inicial, metas y plan**, y la **ruta del
   plan resaltada** frente al resto de estados explorados.

**Plan esperado (referencia):**
```
1. Aplicar_Sesion_Regenerativa      CO₂ 1
2. Monitorear_Biomarcadores         CO₂ 1   ← desbloquea co2_acumulado(bajo)
3. Ajustar_Plan_Nutricional         CO₂ 1
4. Ejecutar_Entrenamiento_Especifico CO₂ 5  ← estaba BLOQUEADA hasta el paso 2
5. Validar_Estado_Competitivo       CO₂ 1
                                    ───────
                          CO₂ total   9
```

---

## 3. Módulo Min-Max (`minmax.py`) — ⚠️ existe, pero hay que generalizarlo

El árbol de la guía 5 es un **diccionario fijo de profundidad 3**. El parcial exige correr
**profundidades {2, 3, 4}** en **3 escenarios**, así que hay que generarlo **proceduralmente**.

### 3.1 Árbol procedural (extensión natural del de la guía 5)
El estado es el vector de métricas `(rendimiento, co2, riesgo_lesion, recuperacion)`; cada decisión
le aplica un delta.

| Nivel | Jugador | Opciones |
|---|---|---|
| 1 | **MAX** cuerpo técnico | Carga **Alta / Moderada / Baja** *(se añade "Baja" para ampliar el árbol)* |
| 2 | **MIN** organismo | Fatiga **Alta / Baja** |
| 3 | **MAX** cuerpo técnico | **Jugar / Jugar parcial / Descansar** |
| 4 | **MIN** organismo | **Molestia muscular / Sin molestia** |

Hojas: 3×2×3×2 = **36** a profundidad 4; 18 a profundidad 3; 6 a profundidad 2.
Suficiente para que α-β pode de forma visible y para medir tiempos.

**La utilidad no cambia** — se sigue usando la de la guía 5:
```
U = (Rendimiento × 4) − (CO₂ × 2·λ) − (Riesgo_lesión × 3) + (Recuperación × 2)
```

**Verificación obligatoria:** con el árbol limitado a profundidad 3 y solo las opciones
`{Alta, Moderada} × {Alta, Baja} × {Jugar, Descansar}`, el resultado **tiene que reproducir el de
la guía 5**:

| Nodo | Valor |
|---|---|
| Carga Alta (MIN) | **−1** |
| Carga Moderada (MIN) | **+19** |
| **Raíz (MAX)** | **+19 → Carga Moderada** |
| Rama elegida | `Carga Moderada → Fatiga Alta → Descansar` |
| Hojas podadas por α-β | 2 de 8 (`CA_FB_Desc`, `CM_FB_Desc`) |

Si el generador no da eso, hay un bug. **Es el mejor test que tenemos.**

### 3.2 Correcciones obligatorias del código de la guía 5
1. **Propagar la rama completa**, no solo el primer hijo. Hoy `ruta_optima` guarda un único nodo,
   y el enunciado exige **resaltar la rama escogida** con etiquetas por movimiento.
   Solución: que `minimax()` devuelva `(valor, ruta)` en vez de solo el valor.
2. **Contador global de nodos expandidos** que incremente en **cada** llamada (no solo en hojas).
   El enunciado pide `nodos_expandidos` como métrica medida.
3. **Cronometrar** con `time.perf_counter()`.
4. Corregir los comentarios de valores de la celda 4 (`-29,-3,+6,+36,+37` → `−27,−1,+4,+42,+41`).

### 3.3 Heurística de evaluación (la tercera versión que pide el enunciado)
Para nodos **no terminales** cuando se corta por profundidad:
```
eval(estado_parcial) = U(vector de métricas acumulado hasta aquí)
```
Es decir: **evaluar el estado con la misma función de utilidad, sin expandir el resto del árbol.**
Es el equivalente exacto de lo que en la guía 4 hacía `h(n)`: estimar lo que falta sin recorrerlo.

### 3.4 `minmax_tree.png`
Requisitos explícitos del enunciado, todos verificables:
- ✅ **Todos** los nodos y hojas con su valor evaluado escrito.
- ✅ **Rama escogida resaltada** (color + anchura distinta).
- ✅ **Etiquetas en las aristas** con el movimiento (`"Carga Moderada"`, `"Fatiga Alta"`, `"Descansar"`).
- ✅ Nodos podados en gris (la guía 5 ya lo hace).
- Para la figura entregable usar **profundidad 3** (legible); las profundidades 2 y 4 van en la
  tabla del experimento, no en el dibujo.

### 3.5 Experimento del bloque extra 1
**3 escenarios** = tres vectores iniciales distintos del atleta:
1. **Atleta fresco** (inicio de semana): CO₂ acumulado bajo, riesgo base bajo.
2. **Atleta cargado** (48 h después de partido): CO₂ acumulado alto.
3. **Atleta con historial de lesión**: riesgo base elevado.

Tabla a generar (×3 escenarios × 3 profundidades × 3 versiones = 27 filas):

| Escenario | Profundidad | Versión | Tiempo (ms) | Nodos expandidos | Decisión |
|---|---|---|---|---|---|
| … | 2 / 3 / 4 | naive / α-β / heurística (+α-β) | | | |

**Qué hay que demostrar:**
- α-β debe dar **exactamente la misma decisión** que naive con menos nodos. Si difiere, es un bug.
- La versión con heurística **puede** cambiar la decisión: ahí va el análisis de si mejora o empeora.
- Hipótesis esperada: a profundidad 2 la heurística decide "Carga Alta" (todavía no ve la molestia
  muscular del nivel 4) y a profundidad 4 se corrige. **Es el argumento de por qué la profundidad
  importa en decisiones de carga**: el daño no aparece el mismo día.

---

## 4. Agente integrador (`agente.py`) — 🔴 nuevo

```python
evidencia   = observar()                    # F = Alta (biomarcadores alterados, HRV baja)
posterior   = bayes.inferir(evidencia)      # P(E|F=Alta)=0.325 ; P(C=Alta|F=Alta)=0.625
meta        = META_BASE if posterior['exito'] >= UMBRAL else META_CONSERVADORA
plan        = strips.planificar_astar(S0, meta, acciones)
decision, rama = minmax.decidir(escenario, profundidad=3, poda=True, heuristica=True)
actuar(decision)
```
`UMBRAL = 0.40`. Es la bisagra: lo que hace que Bayes **realmente** cambie el plan de STRIPS.

### `agent_log.txt` (formato propuesto — consola **y** archivo)
```
============================================================
 AGENTE INTEGRADOR — IA CLÁSICA — CORTE 1
 Sector: Rendimiento deportivo / gestión de carga del atleta
============================================================
[OBSERVE  ] Evidencia: F = Fatiga alta (HRV baja + sueño fragmentado, Kinexon)
[POSTERIOR] P(C=Alta | F=Alta)  = 0.625   (prior 0.400)
[POSTERIOR] P(E=Éxito | F=Alta) = 0.325   (marginal 0.578)
[POSTERIOR] Umbral = 0.400 → POR DEBAJO → meta conservadora
[PLAN     ] Meta STRIPS: {atleta(recuperado), riesgo_lesion(bajo), rendimiento(alto),
                          co2_acumulado(bajo), listo_para_competir, carga_semanal(optima)}
[PLAN     ] 1. Aplicar_Sesion_Regenerativa        CO2 1
[PLAN     ] 2. Monitorear_Biomarcadores           CO2 1   [desbloquea co2(bajo)]
[PLAN     ] 3. Ajustar_Plan_Nutricional           CO2 1
[PLAN     ] 4. Ejecutar_Entrenamiento_Especifico  CO2 5   [estaba bloqueada]
[PLAN     ] 5. Validar_Estado_Competitivo         CO2 1
[PLAN     ] CO2 total del plan: 9 kg CO2eq | nodos expandidos: NN
[DECISION ] Min-Max (prof=3, α-β, heurística) → Carga Moderada → Fatiga Alta → Descansar
[DECISION ] Valor garantizado: +19.0 | nodos: NN | podados: NN | tiempo: NN ms
[CONTRASTE] Utilidad esperada (ponderada por Bayes): NN.N → coincide/no con Min-Max
[ACCION   ] Recomendación: carga moderada esta semana y NO alinear al atleta el fin de semana.
[ÉTICA    ] Recomendación, no veredicto. La decisión final es del cuerpo médico (human-in-command).
============================================================
```

### `agent_summary.png`
Una figura con `plt.subplots` en 3 zonas (el enunciado lo detalla mucho: seguirlo al pie de la letra):
- **Izquierda (≈50 %)**: mini-grafo del plan STRIPS (5 pasos encadenados, con el CO₂ de cada uno).
- **Arriba derecha**: mini-barras de `P(E=Éxito)` marginal vs con evidencia + **número grande** `32.5 %`.
- **Abajo derecha**: la decisión Min-Max en **texto grande** (`"CARGA MODERADA → DESCANSAR"`) con su
  valor `+19`, y la rama seleccionada anotada.
- **Título** con la evidencia usada.

---

## 5. Análisis de sensibilidad bayesiano (bloque extra 2)

Barrer el prior `P(C=Alta)` con **5 valores**, manteniendo la evidencia `F = Alta`.
**Posteriores ya calculados (test de regresión):**

| `P(C=Alta)` | `P(E=Éxito \| F=Alta)` | ¿supera umbral 0.40? | Meta STRIPS | Decisión Min-Max |
|---|---|---|---|---|
| 0.10 | **40.7 %** | ✅ sí | estándar | (a registrar) |
| 0.25 | **35.9 %** | ❌ no | conservadora | (a registrar) |
| 0.40 | **32.5 %** | ❌ no | conservadora | (a registrar) |
| 0.60 | **29.2 %** | ❌ no | conservadora | (a registrar) |
| 0.80 | **26.8 %** | ❌ no | conservadora | (a registrar) |

**Hallazgo a discutir (ya se ve en los números):** la decisión **cambia solo entre 0.10 y 0.25**.
- **Fragilidad:** si el cuerpo técnico cree que casi nunca aplica cargas altas, el agente se
  confía y propone el plan estándar. Basta una desviación pequeña en esa creencia para cambiar
  el plan del atleta.
- **Estabilidad:** de 0.25 en adelante da igual afinar el prior — el agente siempre protege al
  atleta. **La decisión es robusta justo donde importa.**

Conclusión para la exposición: *el parámetro que hay que medir con rigor es el registro real de
carga semanal. Todo lo demás el modelo lo aguanta.*

Añadir `sensibilidad.png` (opcional pero refuerza): posterior vs prior con la línea del umbral.

---

## 6. Estructura de archivos

```
parcial practico 1/entregables/
├── README.md               # cómo ejecutar, evidencia usada, qué genera cada script
├── dominio.py              # métricas, utilidad, escenarios, constantes (λ, UMBRAL, priors)
├── bayes.py                # CPTs, inferencia, bayes_bars.png
├── strips.py               # acciones, forward, backward, A*, strips_graph.png
├── minmax.py               # árbol procedural, α-β, heurística, minmax_tree.png
├── agente.py               # flujo integrador → agent_log.txt + agent_summary.png
├── experimentos.py         # tablas de los bloques extra 1 y 2
├── minmax_tree.png · strips_graph.png · bayes_bars.png · agent_summary.png
└── agent_log.txt
```

- Los PNG se generan **en la raíz de esa carpeta**, con los nombres **exactos**. Sin subcarpetas.
- `python agente.py` debe generar **todo** en una sola ejecución.
- Dependencias: `networkx`, `matplotlib`, `pandas` — las mismas de la guía 5. **Sin librerías nuevas**
  (nada de `pgmpy`): Bayes a mano, como en los ejemplos del profesor.
- Si quieren notebook para la demo, que **importe** los módulos, no que duplique código.

---

## 7. 📅 Cronograma de 3 días

### Lunes 14 (hoy) — Bayes
- [ ] Validar CPTs con el grupo → cierra la **guía 6** también.
- [ ] `dominio.py` + `bayes.py` + `bayes_bars.png`.
- [ ] Notebook de la guía 6 (mismo código, presentación distinta).

### Martes 15 — portar y arreglar
- [ ] `strips.py`: portar de la guía 5, arreglar el retorno de 5 elementos, añadir **A\***,
      meta variable, leyenda de `strips_graph.png`.
- [ ] `minmax.py`: generador procedural + **ruta completa** + contador de nodos + cronómetro.
- [ ] **Verificar contra el test de §3.1** (raíz = +19, rama = Moderada→Alta→Descansar, 2 podas).

### Miércoles 16 — integrar y experimentar
- [ ] `agente.py` + `agent_log.txt` + `agent_summary.png`.
- [ ] `experimentos.py`: los dos bloques extra.
- [ ] `README.md`.
- [ ] Presentación en Gamma + **ensayar la demo cronometrada**.

### Jueves 17 — entrega
- [ ] Ejecución limpia desde cero (borrar PNGs y volver a generar) para confirmar que no falla.
- [ ] Demo.

### 🔺 Si el tiempo se acorta, este es el orden de recorte
1. `sensibilidad.png` (gráfica opcional).
2. Profundidad 4 del bloque extra 1 → quedarse en {2, 3}.
3. Escenario 3 del bloque extra 1 → quedarse con 2 escenarios.

**Lo que NO se puede recortar** (es lo explícitamente exigido y lo que se califica):
los 4 PNG con nombres exactos, `agent_log.txt`, el README, y el A\* dentro de STRIPS.

---

## 8. Guion de la demo de 5 minutos

| Tiempo | Contenido | Figura |
|---|---|---|
| 0:00–0:45 | El problema: preparar al atleta en 5 días sin romperlo. MAX vs MIN. | — |
| 0:45–1:45 | **Min-Max**: el árbol, la utilidad con métricas reales, por qué el agente se queda con **+19** y no con **+42**. Cuánto podó α-β. | `minmax_tree.png` |
| 1:45–2:45 | **STRIPS**: S0, meta, el plan de 5 pasos y **el cerrojo del CO₂** que bloquea el entrenamiento. Forward vs backward. | `strips_graph.png` |
| 2:45–3:30 | **Bayes**: la red C→F→E, la evidencia, y cómo `P(éxito)` cae de 57.8 % a 32.5 %. | `bayes_bars.png` |
| 3:30–4:30 | **El agente**: el log corriendo en vivo + la síntesis. | `agent_summary.png` |
| 4:30–5:00 | Cierre: *Min-Max garantiza, Bayes espera, STRIPS ejecuta* + la línea ética de la guía 2. | — |

---

## 9. Trampas a evitar

- ❌ **No mezclar los dos dominios.** El parcial es **solo** gestión de carga del atleta (Dominio B).
  La red de pases (guías 3–4) se menciona como antecedente, no se integra: no hay tiempo y
  confundiría la exposición.
- ❌ No usar `pgmpy` ni un planificador PDDL externo.
- ❌ No entregar `minmax_tree.png` sin los valores en **todos** los nodos ni sin etiquetas de
  movimiento: es un requisito explícito y es donde se pierden puntos fáciles.
- ❌ No olvidar que `agent_log.txt` debe salir **también por consola**.
- ❌ No confundir **mejor hoja** (+42) con **decisión Min-Max** (+19). Es el error que hay en la
  conclusión del experimento λ de la guía 5; corregirlo antes de proyectar.
- ✅ Sí dejar `λ`, `UMBRAL` y los priors como constantes al inicio de `dominio.py`, para poder
  cambiarlos en vivo si el profesor lo pide en la demo. Queda muy bien.
