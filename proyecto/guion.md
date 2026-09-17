# Guion de exposición — Parcial Práctico 1
### 10 minutos · en inglés · 4 personas

> **Cómo usar este archivo:** cada persona busca su sección, lee **solo su bloque**, y graba su
> parte. Los cuatro bloques van **seguidos**: cada uno habla una sola vez, de corrido. Nadie repite
> turno.
>
> El texto en **inglés** es el que se lee en voz alta. El texto en *español* debajo es solo para
> entender lo que se está diciendo — **no se lee**.

---

## Reparto y tiempos

| # | Persona | Tema | Tiempo | Palabras | Figura en pantalla |
|---|---|---|---|---|---|
| 1 | **Harold** | El problema y el modelo de decisión (Min-Max) | 0:00 – 2:25 | 314 | `minmax_tree.png` |
| 2 | **Felipe** | Planificación con STRIPS y A\* | 2:25 – 5:00 | 330 | `strips_graph.png` |
| 3 | **Keiry** | Incertidumbre (Bayes) y el agente integrador | 5:00 – 7:25 | 314 | `bayes_bars.png` → `agent_summary.png` |
| 4 | **David** | Poda, heurísticas y análisis de sensibilidad | 7:25 – 10:00 | 335 | terminal + `sensibilidad.png` |

**Orden de la historia:** qué decidir → cómo llegar → cómo se unen los tres métodos → cómo lo
pusimos a prueba.

### ⏱️ Sobre el ritmo — importante

Son **1.293 palabras en total**. Para que quepan en 10 minutos hay que leer a un ritmo **normal de
conversación** (unas 140 palabras por minuto), no despacio.

**Cronométrate antes de grabar.** Si tu parte se pasa de **2:40**, cada sección tiene marcada una
frase que puedes **saltarte sin romper nada** (búscala como ✂️). No improvises recortes: usa los
marcados, que están elegidos para no dejar huecos en la explicación.

---

# ⚙️ ANTES DE GRABAR — hacer una sola vez (todos)

Aunque no sepas nada del proyecto, esto funciona. Son 5 minutos.

### 1. Instalar Python
Descárgalo de **python.org** (versión 3.8 o superior). En Windows, marca la casilla
**"Add Python to PATH"** durante la instalación.

Para comprobar que quedó bien, abre una terminal (en Windows: *Símbolo del sistema* o
*PowerShell*; en Mac: *Terminal*) y escribe:
```bash
python --version
```
Si dice `Python 3.x.x`, vas bien. *(En Mac quizá tengas que escribir `python3` en lugar de
`python` en todos los comandos de aquí en adelante.)*

### 2. Instalar las tres librerías
```bash
pip install matplotlib networkx pandas
```

### 3. Entrar a la carpeta del proyecto
Pide la carpeta `entregables` al grupo, déjala en el Escritorio, y en la terminal escribe:
```bash
cd Desktop/entregables
```
*(Si la carpeta está en otro sitio, escribe `cd ` con un espacio y arrastra la carpeta encima de la
ventana de la terminal: la ruta se escribe sola.)*

### 4. Comprobar que todo funciona
```bash
python test_regresion.py
```
Tiene que terminar con **`TODAS LAS PRUEBAS PASAN`**. Si sale eso, ya puedes grabar tu parte.

### 5. Generar todas las figuras una vez
```bash
python agente.py
```
Esto crea los cuatro PNG en la misma carpeta. Ábrelos con doble clic cuando tu guion lo diga.

> ### ⚠️ Tres reglas para grabar
> 1. **No muestres el código fuente en pantalla.** Muestra la **terminal** con el resultado, y las
>    **imágenes**. Es más claro y evita distracciones.
> 2. **Ejecuta el comando ANTES de empezar a hablar**, para que la salida ya esté en pantalla y no
>    se pierda tiempo esperando.
> 3. **Comparte pantalla completa**, no solo una ventana, para poder pasar de la terminal a la
>    imagen sin cortes.

---
---

# 1 · HAROLD — *The problem and the decision model*
### 0:00 – 2:25  ·  314 palabras

### 🖥️ Qué ejecutar y mostrar

```bash
python dominio.py
```
Deja esa salida en pantalla mientras hablas de la función de utilidad (se ve la fórmula y la tabla
de las 8 combinaciones con su valor).

Luego ejecuta:
```bash
python minmax.py
```
Y **abre `minmax_tree.png`** cuando llegues a la parte del árbol. Señala con el cursor:
- la **rama roja** (la decisión),
- la hoja que vale **+42** (abajo, en la zona de "Moderada → Baja"),
- la hoja resaltada que vale **+19**.

> ### ✂️ Si vas largo
> Sáltate el párrafo de las fuentes de los pesos:
> *"These weights are not arbitrary. They come from GPS sensors, from the GHG Protocol adapted to
> sport, and from UEFA medical reports."* — **ahorra 12 segundos.**

---

### 🇬🇧 Script (leer esto)

Good morning. Our sector is **sports performance analytics** — professional football.

Every week, a coaching staff faces the same decision. The match is on Saturday. It is Monday. How hard do we train this player? And on Saturday, do we play him, or do we rest him?

It is hard, because the athlete's body does not answer the same way every week. Sometimes a heavy week leaves him fresh. Sometimes an easy week leaves him exhausted.

We built an agent that makes this decision with three classical AI methods. My part is the **decision model**.

First, how we measure. Every situation is described by four numbers, on a zero to ten scale: **performance**, **metabolic CO2**, **injury risk**, and **recovery**. We combine them into one utility function:

*Utility equals performance times four, minus CO2 times two, minus injury risk times three, plus recovery times two.*

These weights are not arbitrary. They come from GPS sensors, from the GHG Protocol adapted to sport, and from UEFA medical reports.

Now, **Min-Max**. We model this as a game with two players. **MAX** is the coaching staff — us. **MIN** is the athlete's body, and we assume it always answers in the worst possible way for us.

The tree has three levels. We choose the training load — high, moderate, or low. The body answers with fatigue. Then we decide: play, play partially, or rest.

Here is the result — the most important idea in our project.

The **best leaf** in the tree is worth **plus forty-two**: moderate load, the body responds fresh, the player plays. But our agent **does not choose it**. It chooses a branch worth **plus nineteen**: moderate load, high fatigue, rest the player.

Why? Because reaching plus forty-two requires the body to cooperate — and a pessimist never counts on that.

**The decision is not the best possible one. It is the best guaranteed one.**

---

### 🇪🇸 Traducción (solo para entender)

> Buenos días. Nuestro sector es la **analítica del rendimiento deportivo** — fútbol profesional.
>
> Cada semana, un cuerpo técnico enfrenta la misma decisión. El partido es el sábado. Hoy es lunes.
> ¿Cuánto hacemos entrenar a este jugador? Y el sábado, ¿lo alineamos o lo dejamos descansar?
>
> Es difícil, porque el cuerpo del atleta no responde igual todas las semanas. A veces una semana
> dura lo deja fresco. A veces una semana suave lo deja agotado.
>
> Construimos un agente que toma esta decisión con tres métodos de IA clásica. Mi parte es el
> **modelo de decisión**.
>
> Primero, cómo medimos. Cada situación se describe con cuatro números, en escala de cero a diez:
> **rendimiento**, **CO2 metabólico**, **riesgo de lesión** y **recuperación**. Los combinamos en
> una sola función de utilidad:
>
> *Utilidad = rendimiento × 4 − CO2 × 2 − riesgo de lesión × 3 + recuperación × 2.*
>
> Estos pesos no son arbitrarios. Vienen de sensores GPS, del GHG Protocol adaptado al deporte, y
> de informes médicos de la UEFA.
>
> Ahora, **Min-Max**. Modelamos esto como un juego de dos jugadores. **MAX** es el cuerpo técnico
> — nosotros. **MIN** es el cuerpo del atleta, y asumimos que siempre responde de la peor forma
> posible para nosotros.
>
> El árbol tiene tres niveles. Elegimos la carga de entrenamiento — alta, moderada o baja. El
> cuerpo responde con fatiga. Después decidimos: jugar, jugar parcialmente, o descansar.
>
> Este es el resultado — la idea más importante de nuestro proyecto.
>
> La **mejor hoja** del árbol vale **+42**: carga moderada, el cuerpo responde fresco, el jugador
> juega. Pero nuestro agente **no la elige**. Elige una rama que vale **+19**: carga moderada,
> fatiga alta, descansar al jugador.
>
> ¿Por qué? Porque llegar al +42 requiere que el cuerpo colabore — y un pesimista nunca cuenta con
> eso.
>
> **La decisión no es la mejor posible. Es la mejor garantizada.**

---
---

# 2 · FELIPE — *Planning with STRIPS*
### 2:25 – 5:00  ·  330 palabras

### 🖥️ Qué ejecutar y mostrar

```bash
python strips.py
```

En la salida de la terminal se ven, en este orden: el plan estándar (5 acciones), el plan
conservador (6 acciones), la comparación forward/backward, los bloqueos, y la demostración de la
anomalía de Sussman. Ve bajando con el scroll a medida que hablas.

Cuando llegues a la parte del plan, **abre `strips_graph.png`** y señala:
- el **nodo verde** (estado inicial) y el **naranja** (meta),
- la **línea roja** = la ruta del plan,
- la etiqueta de **`Ejecutar Entrenamiento Especifico — CO2 = 5`**, que es la acción cara,
- los **tres recuadros de abajo**: estado inicial, meta y plan.

> ### ✂️ Si vas largo
> Sáltate el último párrafo:
> *"We do not just claim this. Our code runs the linear planner and shows it fail, then shows A
> star solving the same problem."* — **ahorra 11 segundos.**
> (El punto de la anomalía de Sussman ya quedó dicho en el párrafo anterior.)

---

### 🇬🇧 Script (leer esto)

Thank you, Harold. Harold explained **what** to decide. My part is **how to get there**.

For that we use **STRIPS planning**. STRIPS describes the world with predicates — simple facts that are either true or false.

Our **initial state**: the athlete is fatigued, the weekly load is high, injury risk is elevated, performance is low, accumulated CO2 is high, and the match is in five days.

Our **goal**: the athlete recovered, risk low, performance high, CO2 low, and ready to compete.

Between them, we defined **six actions**. Each one has **preconditions** — what must be true to execute it — and two effect lists: **ADD**, what becomes true, and **DELETE**, what stops being true.

Here is the most interesting action. *Execute specific training* produces high performance and low injury risk. But it requires **accumulated CO2 to be low**. And it costs **five kilograms** of CO2 equivalent — the most expensive action in the plan.

That precondition is a **lock**. While the athlete carries accumulated load, hard training is forbidden by the rules of the world, not by our choice. The lock only opens after we measure biomarkers. That is what forces the plan into one specific order.

We solved it in **two directions** — forward, from the initial state, and backward, by goal regression. Then we used **A star** as the search engine, over the space of states.

This matters. If the agent simply applies the first action it can, it finds a plan costing **ten**. A star finds one costing **nine**. Same goal, eleven percent less metabolic cost — just by searching better.

We also found a real **Sussman anomaly**. The action *adjust nutrition* deletes the fact *athlete in recovery*, which another action needs — and that fact can never be restored. A linear planner that solves the goals one by one gets permanently blocked.

We do not just claim this. Our code **runs** the linear planner and shows it fail, then shows A star solving the same problem.

---

### 🇪🇸 Traducción (solo para entender)

> Gracias, Harold. Harold explicó **qué** decidir. Mi parte es **cómo llegar ahí**.
>
> Para eso usamos **planificación STRIPS**. STRIPS describe el mundo con predicados — hechos
> simples que son verdaderos o falsos.
>
> Nuestro **estado inicial**: el atleta está fatigado, la carga semanal es alta, el riesgo de
> lesión es elevado, el rendimiento es bajo, el CO2 acumulado es alto, y el partido es en cinco
> días.
>
> Nuestra **meta**: el atleta recuperado, riesgo bajo, rendimiento alto, CO2 bajo, y listo para
> competir.
>
> Entre los dos, definimos **seis acciones**. Cada una tiene **precondiciones** — lo que debe ser
> verdad para poder ejecutarla — y dos listas de efectos: **ADD**, lo que pasa a ser verdad, y
> **DELETE**, lo que deja de serlo.
>
> Esta es la acción más interesante. *Ejecutar entrenamiento específico* produce rendimiento alto
> y riesgo de lesión bajo. Pero requiere que el **CO2 acumulado esté bajo**. Y cuesta **cinco
> kilogramos** de CO2 equivalente — la acción más cara del plan.
>
> Esa precondición es un **cerrojo**. Mientras el atleta arrastre carga acumulada, el entrenamiento
> fuerte está prohibido por las reglas del mundo, no por decisión nuestra. El cerrojo solo se abre
> después de medir los biomarcadores. Eso es lo que obliga al plan a ir en un orden específico.
>
> Lo resolvimos en **dos direcciones** — hacia adelante, desde el estado inicial, y hacia atrás,
> por regresión de metas. Después usamos **A estrella** como motor de búsqueda, sobre el espacio
> de estados.
>
> Esto importa. Si el agente simplemente aplica la primera acción que puede, encuentra un plan que
> cuesta **diez**. A estrella encuentra uno que cuesta **nueve**. La misma meta, once por ciento
> menos de costo metabólico — solo por buscar mejor.
>
> También encontramos una **anomalía de Sussman** real. La acción *ajustar nutrición* borra el
> hecho *atleta en recuperación*, que otra acción necesita — y ese hecho ya no se puede restaurar.
> Un planificador lineal que resuelve las metas una por una queda bloqueado para siempre.
>
> No solo lo afirmamos. Nuestro código **ejecuta** el planificador lineal y lo muestra fallar, y
> después muestra a A estrella resolviendo el mismo problema.

---
---

# 3 · KEIRY — *Uncertainty and the integrating agent*
### 5:00 – 7:25  ·  314 palabras

### 🖥️ Qué ejecutar y mostrar

```bash
python bayes.py
```
Se ven las tres tablas de probabilidad y las consultas. **Abre `bayes_bars.png`** y señala:
- la barra gris (**57.8 %**, sin evidencia),
- la barra naranja (**32.5 %**, atleta fatigado),
- la barra azul (**81.2 %**, atleta fresco),
- el **recuadro amarillo**, donde está escrita la evidencia usada.

Después ejecuta:
```bash
python agente.py
```
Muestra la terminal con el flujo `[OBSERVE] → [POSTERIOR] → [PLAN] → [DECISION] → [ACCION]`, y
para cerrar **abre `agent_summary.png`**.

> ### ✂️ Si vas largo
> Sáltate el párrafo del razonamiento hacia atrás:
> *"And the network does something we did not ask for: it reasons backwards… we believed only
> forty percent."* — **ahorra 20 segundos.**
> Es el párrafo más prescindible porque el enunciado no pide razonamiento diagnóstico; los tres
> puntos obligatorios (red, conjunta, inferencia con evidencia) quedan cubiertos igual.

---

### 🇬🇧 Script (leer esto)

Thank you, Felipe. So far, both methods assume things. STRIPS assumes nothing goes wrong. Min-Max assumes everything goes wrong. My part is the method that deals with reality: the **Bayesian network**.

We identified **three variables**. **C** is the weekly load we applied. **F** is the fatigue the body responds with. And **E** is competitive success: whether the player arrives available and performs.

The arrows say: the load influences the fatigue, and both together influence the success. Each arrow carries a table of conditional probabilities.

Now the results. **Without evidence**, our expectation of success is **fifty-seven point eight percent**. One number for the whole season.

Then the sensors speak. On Wednesday, heart rate variability is low and sleep is fragmented. The athlete is fatigued. With that evidence, the probability of success drops to **thirty-two point five percent**. If instead he arrives fresh, it rises to **eighty-one percent**.

And the network does something we did not ask for: it **reasons backwards**. Seeing the athlete fatigued, it deduces there is a **sixty-two point five percent** chance the cause was the load that *we ourselves* applied — when before, we believed only forty percent.

So how do three methods become **one agent**? The flow is: **observe, posterior, plan, decision, action**.

The hinge is a **threshold**, set at forty percent. Our posterior — thirty-two point five — is below it. So the agent **changes the STRIPS goal** to a conservative version that also demands an energy reserve. The plan grows from five actions to six.

That single decision is what makes this an agent. Without it, we would have three programs in the same folder. With it, **what the sensors observe changes the plan that is executed**.

One last number. Min-Max **guarantees** plus nineteen. Bayes **expects** plus thirty-five. They agree on what to do — they disagree on what it is worth. That difference is the price of caution.

---

### 🇪🇸 Traducción (solo para entender)

> Gracias, Felipe. Hasta ahora, los dos métodos asumen cosas. STRIPS asume que nada va a salir
> mal. Min-Max asume que todo va a salir mal. Mi parte es el método que lidia con la realidad: la
> **red bayesiana**.
>
> Identificamos **tres variables**. **C** es la carga semanal que aplicamos. **F** es la fatiga con
> la que responde el cuerpo. Y **E** es el éxito competitivo: si el jugador llega disponible y
> rinde.
>
> Las flechas dicen: la carga influye en la fatiga, y las dos juntas influyen en el éxito. Cada
> flecha lleva una tabla de probabilidades condicionales.
>
> Ahora los resultados. **Sin evidencia**, nuestra expectativa de éxito es del **57.8 %**. Un solo
> número para toda la temporada.
>
> Entonces hablan los sensores. El miércoles, la variabilidad de la frecuencia cardíaca está baja y
> el sueño está fragmentado. El atleta está fatigado. Con esa evidencia, la probabilidad de éxito
> cae al **32.5 %**. Si en cambio llega fresco, sube al **81 %**.
>
> Y la red hace algo que no le pedimos: **razona hacia atrás**. Al ver al atleta fatigado, deduce
> que hay un **62.5 %** de probabilidad de que la causa fuera la carga que *nosotros mismos*
> aplicamos — cuando antes creíamos que solo un 40 %.
>
> Entonces, ¿cómo tres métodos se convierten en **un agente**? El flujo es: **observar, posterior,
> plan, decisión, acción**.
>
> La bisagra es un **umbral**, fijado en 40 %. Nuestro posterior — 32.5 — está por debajo. Así que
> el agente **cambia la meta de STRIPS** a una versión conservadora que además exige reserva
> energética. El plan pasa de cinco acciones a seis.
>
> Esa sola decisión es lo que hace que esto sea un agente. Sin ella, tendríamos tres programas en
> la misma carpeta. Con ella, **lo que observan los sensores cambia el plan que se ejecuta**.
>
> Un último número. Min-Max **garantiza** +19. Bayes **espera** +35. Coinciden en qué hacer —
> difieren en cuánto vale. Esa diferencia es el precio de la prudencia.

---
---

# 4 · DAVID — *Pruning, heuristics and sensitivity*
### 7:25 – 10:00  ·  335 palabras

### 🖥️ Qué ejecutar y mostrar

```bash
python experimentos.py
```
⏱️ **Tarda unos 30 segundos.** Ejecútalo **antes** de empezar a hablar.

Deja la terminal en pantalla y ve bajando con el scroll. Verás, en orden: las cuatro tablas de
escenarios, y después el análisis con los cuatro puntos numerados. Señala:
- la columna **`Nodos`** al comparar `(i) Min-Max basico` contra `(ii) Min-Max + alfa-beta`,
- la columna **`Decision`** a profundidad 2, donde `(i)` dice `Moderada` y `(iii)` dice `Baja`.

Para la última parte, **abre `sensibilidad.png`** y señala:
- la **línea roja punteada** (el umbral del 40 %),
- el **punto verde** a la izquierda (el único que queda arriba del umbral),
- los cuatro puntos naranjas.

> ### ✂️ Si vas largo
> Sáltate la analogía de la camiseta:
> *"If you already found a shirt for fifty thousand pesos… without looking at the rest."* —
> **ahorra 14 segundos.**
> Empieza directamente en *"Alpha-beta discards whole branches of the tree."*

---

### 🇬🇧 Script (leer esto)

Thank you, Keiry. We had a working agent. My part was to **try to break it**.

First, **alpha-beta pruning**. If you already found a shirt for fifty thousand pesos, and you walk into a shop where shirts start at one hundred thousand, you turn around without looking at the rest. Alpha-beta does that with whole branches of the tree.

We ran a full comparison: **four scenarios**, **three depths** — two, three and four — and **four versions** of the algorithm. Forty-eight runs, measuring time, expanded nodes, and the chosen decision.

**Result one.** Alpha-beta gives **exactly the same decision and the same value** as the basic version, in all twelve cases, while expanding **thirty-six percent fewer nodes**. That is the theoretical guarantee of the algorithm — and we **verified** it instead of assuming it.

**Result two**, and this one surprised us. We compared a **naive evaluation** — one that looks only at performance — against our **designed heuristic**. They only disagree at **depth two**. There, the naive one says *moderate load*, and ours says *low load*.

Why? At depth two, the search stops right after the fatigue response. The agent cannot yet see that it can **rest** the player on Saturday. Without that option, the only way to protect him is to train him less. So our heuristic is more prudent, but more conservative than necessary.

The lesson is not that one evaluation beats the other. The lesson is that **no heuristic compensates for cutting the search too early**.

**Result three.** The decision **stabilizes at depth three**. Depth four costs sixty-four nodes instead of twenty-eight, and changes nothing.

Finally, the **sensitivity analysis**. We varied the prior across five values. The plan only changes between zero point one and zero point two five. After that, it is stable. And the Min-Max decision **never moves** — not a flaw: Min-Max reasons about the worst case, not about probabilities.

One closing note. This system **recommends**. It does not decide. The final call belongs to the medical staff. Thank you.

---

### 🇪🇸 Traducción (solo para entender)

> Gracias, Keiry. Teníamos un agente funcionando. Mi parte fue **intentar romperlo**.
>
> Primero, la **poda alfa-beta**. Si ya encontraste una camiseta por cincuenta mil pesos, y entras
> a una tienda donde las camisetas empiezan en cien mil, te das la vuelta sin mirar el resto.
> Alfa-beta hace eso con ramas enteras del árbol.
>
> Corrimos una comparación completa: **cuatro escenarios**, **tres profundidades** — dos, tres y
> cuatro — y **cuatro versiones** del algoritmo. Cuarenta y ocho ejecuciones, midiendo tiempo,
> nodos expandidos y la decisión escogida.
>
> **Resultado uno.** Alfa-beta da **exactamente la misma decisión y el mismo valor** que la versión
> básica, en los doce casos, expandiendo un **36 % menos de nodos**. Esa es la garantía teórica del
> algoritmo — y la **verificamos**, en vez de asumirla.
>
> **Resultado dos**, y este nos sorprendió. Comparamos una **evaluación ingenua** — una que solo
> mira el rendimiento — contra nuestra **heurística diseñada**. Solo difieren a **profundidad dos**.
> Ahí, la ingenua dice *carga moderada*, y la nuestra dice *carga baja*.
>
> ¿Por qué? A profundidad dos, la búsqueda se corta justo después de la respuesta de fatiga. El
> agente todavía no alcanza a ver que puede **descansar** al jugador el sábado. Sin esa opción, la
> única forma de protegerlo es entrenarlo menos. Así que nuestra heurística es más prudente, pero
> más conservadora de lo necesario.
>
> La lección no es que una evaluación le gane a la otra. La lección es que **ninguna heurística
> compensa cortar la búsqueda demasiado pronto**.
>
> **Resultado tres.** La decisión **se estabiliza en profundidad tres**. La profundidad cuatro
> cuesta 64 nodos en vez de 28, y no cambia nada.
>
> Por último, el **análisis de sensibilidad**. Variamos el prior en cinco valores. El plan solo
> cambia entre 0.1 y 0.25. Después de eso, es estable. Y la decisión de Min-Max **no se mueve
> nunca** — no es un defecto: Min-Max razona sobre el peor caso, no sobre probabilidades.
>
> Una nota de cierre. Este sistema **recomienda**. No decide. La decisión final es del cuerpo
> médico. Gracias.

---
---

# 🗣️ Pronunciación — palabras que se atragantan

| Palabra | Cómo suena (aprox.) | Quién la dice |
|---|---|---|
| **heuristic** | *hiu-RÍS-tik* | David, Harold |
| **threshold** | *ZRÉS-jould* (la "h" casi no suena) | Keiry |
| **alpha-beta pruning** | *ÁL-fa BÉI-ta PRÚ-ning* | David |
| **precondition** | *pri-con-DÍ-shon* | Felipe |
| **biomarkers** | *BÁI-o-mar-kers* | Keiry, Felipe |
| **fatigue** | *fa-TÍIG* (una sola sílaba al final) | todos |
| **weight / weights** | *uéit / uéits* | Harold |
| **guaranteed** | *ga-ran-TÍID* | Harold |
| **anomaly** | *a-NÓ-ma-li* | Felipe |
| **variability** | *ve-ria-BÍ-li-ti* | Keiry |

**Números decimales:** en inglés el punto se lee *point*.
`57.8` → *fifty-seven **point** eight* · `32.5` → *thirty-two **point** five*

**Nunca digas** "*fifty-seven coma eight*".

---

# ✅ Checklist antes de enviar tu video

- [ ] Corrí `python test_regresion.py` y salió `TODAS LAS PRUEBAS PASAN`
- [ ] Ejecuté mi comando **antes** de empezar a hablar
- [ ] Se ve la terminal **y** la imagen que me toca
- [ ] No se ve el código fuente en pantalla
- [ ] Hablé entre 2:20 y 2:40 (no más)
- [ ] Empecé agradeciendo a la persona anterior (menos Harold, que abre)
- [ ] Se me entiende el audio (probar con audífonos antes de enviar)

---

# 📌 Para quien edite el video final

Orden de los clips: **Harold → Felipe → Keiry → David**.

Los empalmes ya están escritos en el guion (*"Thank you, Harold"*, *"Thank you, Felipe"*,
*"Thank you, Keiry"*), así que suenan como una sola exposición continua y no como cuatro videos
pegados.

Duración objetivo: **10:00**.

Si al juntar los cuatro clips se pasa de 10:00, pide que se regrabe con los recortes ✂️ ya
marcados en cada sección. El orden en que conviene aplicarlos, de menos a más doloroso:

1. Keiry — párrafo del razonamiento hacia atrás (−20 s)
2. David — analogía de la camiseta (−14 s)
3. Harold — fuentes de los pesos (−12 s)
4. Felipe — último párrafo de Sussman (−11 s)

Los cuatro juntos ahorran **57 segundos** y no dejan ningún requisito del enunciado sin cubrir.
