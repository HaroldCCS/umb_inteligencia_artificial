# Cómo funciona el agente — explicación en dos niveles

**Parcial Práctico 1 · Inteligencia Artificial**
Keiry Lucía Olaya Noguera · Harold Stiven Camargo Castellanos · Juan Felipe Coronel Montes · David ⟪APELLIDOS PENDIENTES⟫

Documento de acompañamiento del código. **Primera parte:** cómo funciona a alto nivel, sin una
sola línea de código. **Segunda parte:** cómo funciona por dentro, función por función.

---

# Índice

1. [El problema en una frase](#p0)
2. [**PARTE 1 — Alto nivel**](#parte1)
   - [La analogía madre: el preparador físico](#p11)
   - [Los tres especialistas](#p12)
   - [Cómo trabajan juntos](#p13)
   - [La frase que resume el proyecto](#p14)
3. [**PARTE 2 — Bajo nivel**](#parte2)
   - [El dominio compartido](#p21)
   - [Min-Max y la poda α-β](#p22)
   - [STRIPS y el motor A\*](#p23)
   - [La red bayesiana](#p24)
   - [El agente](#p25)
4. [Cómo verificar que está bien](#verificar)
5. [Glosario](#glosario)

---

<a name="p0"></a>
# 0. El problema en una frase

> Faltan **5 días para el partido**. El futbolista llega cansado. ¿Cuánto lo hacemos entrenar
> esta semana, qué pasos damos para recuperarlo, y lo alineamos el fin de semana o lo dejamos
> descansar?

Es una decisión que los cuerpos técnicos toman todas las semanas, con datos incompletos y
consecuencias caras: si se pasan, lesionan al jugador; si se quedan cortos, llega sin ritmo.

---

<a name="parte1"></a>
# PARTE 1 — CÓMO FUNCIONA A ALTO NIVEL

<a name="p11"></a>
## 1.1 La analogía madre: el preparador físico

Imagina un preparador físico con veinte años de experiencia. El miércoles mira los datos del
chaleco GPS y ve que el jugador tiene la variabilidad cardíaca por el suelo. En su cabeza pasan
tres cosas distintas, casi a la vez:

1. **"¿Qué tan probable es que llegue bien al sábado?"** — pondera, estima, calcula riesgos.
   *Eso es razonamiento probabilístico.*
2. **"¿Qué pasos tengo que dar de aquí al sábado?"** — sesión regenerativa, medir biomarcadores,
   ajustar la comida, entrenar fuerte un día, revisarlo. En ese orden y no en otro.
   *Eso es planificación.*
3. **"Y si el cuerpo responde mal, ¿qué hago?"** — piensa en el peor caso y decide algo que
   aguante incluso si todo sale mal.
   *Eso es decisión bajo adversidad.*

**Nuestro agente hace exactamente esas tres cosas, cada una con un método de IA clásica distinto,
y luego las encadena.**

<a name="p12"></a>
## 1.2 Los tres especialistas

Piénsalo como tres personas sentadas en la misma mesa técnica.

### El pesimista — Min-Max con poda α-β

**Su lema:** *"asume que el cuerpo del jugador va a responder de la peor manera posible."*

Trata al organismo como un **rival de ajedrez**: cada vez que el cuerpo técnico elige una carga,
el organismo "responde" con el nivel de fatiga que más nos perjudica. No es paranoia: es la forma
de no llevarse sorpresas.

**El árbol tiene cuatro niveles**, y se alternan porque las decisiones se alternan en la realidad:

| Nivel | Quién decide | Opciones |
|---|---|---|
| 1 | **Nosotros** (MAX) | Carga alta / moderada / baja |
| 2 | **El organismo** (MIN) | Llega fatigado / llega fresco |
| 3 | **Nosotros** (MAX) | Jugar / jugar parcial / descansar |
| 4 | **El organismo** (MIN) | Aparece molestia muscular / no aparece |

Cada hoja del árbol recibe una nota, calculada con una fórmula que usa métricas reales del sector:

```
Utilidad = (Rendimiento × 4) − (CO₂ metabólico × 2) − (Riesgo de lesión × 3) + (Recuperación × 2)
```

**El resultado más importante de todo el parcial está aquí:** la mejor hoja del árbol vale **+42**
(carga moderada, el cuerpo responde fresco, el jugador juega). Pero el agente **no la elige**.
Elige una que vale **+19**.

¿Por qué? Porque para llegar al +42 hace falta que el organismo colabore, y el pesimista jamás
cuenta con eso. **La decisión no es la mejor posible: es la mejor garantizada.**

> **La poda α-β**, en una frase: si ya encontraste una camiseta a $50.000 y entras a una tienda
> donde las camisetas *empiezan* en $100.000, te das la vuelta sin mirar el resto. El algoritmo
> hace lo mismo con ramas enteras del árbol: descarta sin evaluar todo lo que ya no puede ganar.
> En nuestro árbol se ahorra **un tercio** de los cálculos, y —esto es lo importante— **da
> exactamente la misma respuesta**.

### El organizador — STRIPS con motor A\*

**Su lema:** *"dime dónde estás y a dónde quieres llegar, y yo te doy los pasos."*

Trabaja con **recetas**. Cada acción tiene ingredientes (precondiciones) y resultados
(lo que cambia). Por ejemplo:

> **Acción:** *Ejecutar entrenamiento específico*
> **Necesita:** el atleta recuperado, la nutrición ajustada y **el CO₂ acumulado bajo**
> **Produce:** rendimiento alto y riesgo de lesión bajo
> **Cuesta:** 5 kg CO₂eq — es la acción más cara del plan

Ese "**necesita CO₂ bajo**" es el detalle que hace bonito el modelo. Es un **cerrojo**: mientras
el jugador arrastre carga acumulada, el entrenamiento fuerte **está prohibido por las reglas del
mundo**, no por una decisión nuestra. Solo se abre después de medir los biomarcadores. Eso es lo
que obliga al plan a ir en un orden y no en otro.

**El motor de búsqueda importa.** Si el agente simplemente va aplicando la primera acción que
puede (encadenamiento simple), encuentra un plan de **10 kg CO₂**. Con **A\*** —el mismo algoritmo
de la Guía 4— encuentra uno de **9**. Un kilo de diferencia no parece mucho, pero es un 11 % del
gasto de la semana y sale gratis: solo hay que buscar mejor.

> **Analogía:** el encadenamiento simple es salir del aeropuerto y tomar el primer bus que pase.
> A\* es mirar el mapa antes.

### El realista — la Red Bayesiana

**Su lema:** *"el pesimista exagera. Déjame ponerle números."*

Es el único de los tres que **cambia de opinión cuando llega un dato nuevo**.

Tiene un mapa de causas y efectos: la **carga** que aplicamos influye en la **fatiga** del jugador,
y las dos juntas influyen en el **éxito** del fin de semana. Cada flecha trae una tablita de
probabilidades.

Lo que hace es **repartir la creencia**:

```
              Antes de mirar los sensores
                      57.8 %
                         │
        ┌────────────────┴────────────────┐
        │                                 │
  llega FATIGADO                    llega FRESCO
      32.5 %                           81.2 %
```

Y de regalo hace algo que nadie le pidió: **razona hacia atrás**. Al ver al jugador fatigado,
deduce que es un **62.5 %** probable que la causa fuera la carga que *nosotros* le pusimos —cuando
antes de verlo pensábamos que solo un 40 %—. Es el mismo mecanismo del médico que, al ver fiebre,
sube su sospecha de gripe del 10 % al 51 %.

<a name="p13"></a>
## 1.3 Cómo trabajan juntos

Aquí está el truco que convierte tres programas sueltos en **un agente**:

```
   1. OBSERVE      Los sensores dicen: el jugador llega fatigado.
        ↓
   2. POSTERIOR    Bayes: "con eso, la probabilidad de éxito es 32.5 %".
        ↓
   3. ¿UMBRAL?     ¿32.5 % está por debajo del 40 % que nos fijamos?  SÍ.
        ↓
   4. PLAN         STRIPS cambia de meta: ya no basta con dejarlo listo,
                   ahora además exige reserva energética.
                   A* recalcula: 6 pasos en vez de 5.
        ↓
   5. DECISION     Min-Max: carga moderada y que descanse el sábado.
        ↓
   6. ACCIÓN       Se emite la recomendación al cuerpo técnico.
```

**El umbral es la bisagra.** Sin él, los tres métodos correrían en paralelo sin hablarse y el
"agente" sería una carpeta con tres archivos. Con él, **lo que observan los sensores cambia el
plan que se ejecuta**. Eso es un agente.

> **Analogía:** el umbral es el termostato. Sin termostato tienes un termómetro y una calefacción
> en la misma habitación, pero no tienes un sistema de climatización.

<a name="p14"></a>
## 1.4 La frase que resume el proyecto

Corriendo los dos modelos sobre los mismos datos sale un número que vale toda la exposición:

| | Qué decide | Cuánto promete |
|---|---|---|
| **Min-Max** (pesimista) | Carga moderada | **+19** garantizado |
| **Bayes** (realista) | Carga moderada | **+35.1** esperado |

**Coinciden en qué hacer, no en cuánto vale.** La diferencia —casi el doble— es lo que cuesta ser
prudente. Min-Max no se equivoca en la decisión; subestima el beneficio, porque supone que el
organismo siempre responde mal, cuando con carga moderada eso solo pasa el 30 % de las veces.

> **Min-Max dice qué hacer cuando no te puedes permitir fallar.**
> **Bayes dice qué esperar en promedio.**
> **STRIPS es el plan que te lleva de una cosa a la otra.**

Que los dos coincidan es tranquilizador. **El día que no coincidan, sabremos que estamos ante una
apuesta** — y el agente lo dice explícitamente en su registro.

---

<a name="parte2"></a>
# PARTE 2 — CÓMO FUNCIONA A BAJO NIVEL

<a name="p21"></a>
## 2.1 `dominio.py` — la base compartida

Existe para que **nada se defina dos veces**. Si el grafo, las métricas o los pesos vivieran en
cada módulo, cambiar un número obligaría a cambiarlo en cuatro sitios y tarde o temprano se
desincronizarían.

### El vector de métricas

Todo estado del mundo se resume en cuatro números, en escala 0–10:

```python
(rendimiento, co2, riesgo_lesion, recuperacion)
```

La función de utilidad de la Guía 5 los colapsa en uno solo:

```python
def utilidad(rendimiento, co2, riesgo_lesion, recuperacion, lam=None):
    return (rendimiento     * W_RENDIMIENTO      #  ×4
            - co2           * W_CO2 * lam        #  ×2
            - riesgo_lesion * W_RIESGO           #  ×3
            + recuperacion  * W_RECUPERACION)    #  ×2
```

### La identidad de un estado: su ruta

Un nodo del árbol no guarda su historia: **es** su historia. Se identifica por la tupla de
decisiones que llevaron hasta él:

```python
()                                            # raíz
("Moderada",)                                 # tras elegir la carga
("Moderada", "Alta")                          # tras la respuesta de fatiga
("Moderada", "Alta", "Descansar")             # tras decidir el uso
("Moderada", "Alta", "Descansar", "Molestia") # hoja
```

Esto tiene una ventaja práctica grande: las tuplas son **inmutables y hashables**, así que sirven
directamente como clave de diccionario para guardar valores, marcar nodos podados o resaltar la
rama elegida en el dibujo. No hace falta una clase `Nodo` con punteros.

### Las 8 filas sagradas

```python
METRICAS_N3 = {
    ("Alta", "Alta", "Jugar"):      (3, 8, 9, 2),   # [G5] U=-27
    ("Alta", "Alta", "Descansar"):  (2, 4, 5, 7),   # [G5] U= -1
    ...
}
```

Las marcadas `[G5]` son **literalmente** las de la Guía 5. No se recalcularon ni se "mejoraron":
si cambiaran, todo lo ya presentado en clase dejaría de cuadrar. Las demás filas (carga baja,
jugar parcial) son las opciones que añadimos para poder explorar profundidad 4.

### El truco de los niveles intermedios

La heurística necesita poder evaluar un nodo **a media altura** del árbol, donde todavía no hay un
vector medido. La solución: precalcular los promedios **una sola vez al importar el módulo**.

```python
METRICAS_N2 = {(c, f): _promedio([METRICAS_N3[(c, f, d)] for d in OPC_DECISION])
               for c in OPC_CARGA for f in OPC_FATIGA}
METRICAS_N1 = {c: _promedio([METRICAS_N2[(c, f)] for f in OPC_FATIGA])
               for c in OPC_CARGA}
```

**Por qué importa:** así la heurística cuesta **una consulta de diccionario**, no una expansión del
árbol. Si calculara el promedio sobre la marcha estaría expandiendo justamente lo que dice evitar,
y la comparación de "nodos expandidos" no significaría nada. Es el mismo papel que una *tabla de
patrones* en los motores de ajedrez: trabajo hecho antes, consultado en tiempo constante.

<a name="p22"></a>
## 2.2 `minmax.py` — Min-Max, poda y heurística

### Las tres versiones que pide el enunciado

La diferencia entre ellas está **en qué hacen cuando la búsqueda se corta** antes de llegar a una
hoja real:

```python
def eval_ingenua(ruta, delta):
    """Mira SOLO el rendimiento. Es el cuerpo técnico sin datos."""
    return D.utilidad_ingenua(D.vector_estado(ruta, delta))   # rend × 4

def eval_heuristica(ruta, delta):
    """La función de utilidad completa: rendimiento, CO₂, riesgo y recuperación."""
    return D.utilidad_vector(D.vector_estado(ruta, delta))
```

| Versión del enunciado | Poda | Evaluación en el corte |
|---|---|---|
| (i) Min-Max básico | ✗ | ingenua |
| (ii) Min-Max + α-β | ✓ | ingenua |
| (iii) Min-Max + heurística | ✗ | diseñada |
| (iii+) heurística + α-β | ✓ | diseñada |

### El algoritmo

```python
def minimax(ruta, profundidad, alpha, beta, cnt, evaluar, delta, poda, opciones):
    cnt.nodos_expandidos += 1          # ← se cuenta en CADA llamada
    nivel = len(ruta)

    if nivel >= D.PROFUNDIDAD_MAXIMA or profundidad == 0:
        cnt.hojas_evaluadas += 1
        valor = evaluar(ruta, delta)
        cnt.valores[ruta] = valor
        return valor, ruta                       # ← devuelve VALOR y RUTA
    ...
```

Dos detalles que parecen menores y no lo son:

**1. El contador va en cada llamada, no solo en las hojas.** El enunciado pide *nodos expandidos*
como métrica medida. Contar solo hojas subestima el trabajo real y hace que la comparación entre
versiones no signifique nada.

**2. La función devuelve `(valor, ruta)`, no solo el valor.** Es lo que permite resaltar **la rama
completa** en el dibujo, que es un requisito explícito. Cada nodo propaga hacia arriba la ruta de
su mejor hijo; al final, la raíz tiene la cadena entera.

### La poda, línea por línea

```python
alpha = max(alpha, mejor_val)

if poda and alpha >= beta:
    cnt.podas += 1
    for restante in hijos[i + 1:]:
        cnt.rutas_podadas.add(ruta + (restante,))
    break
```

- `alpha` = lo mejor que MAX tiene asegurado hasta ahora.
- `beta` = lo mejor que MIN tiene asegurado.
- Cuando `alpha >= beta`, seguir mirando es perder el tiempo: el jugador de arriba nunca va a
  dejar que lleguemos a esta rama.
- Los hermanos no visitados se guardan en `rutas_podadas` para poder **pintarlos en gris** en la
  figura.

### Cómo se dibuja el árbol cumpliendo los tres requisitos

El enunciado exige que **todos** los nodos muestren su valor, pero la poda precisamente evita
calcular algunos. La solución es correr **dos veces**:

```python
completo = decidir(profundidad, poda=False, ...)   # (a) valores de TODOS los nodos
podado   = decidir(profundidad, poda=True,  ...)   # (b) qué subárboles se descartaron
```

Se dibujan los valores de (a) y se pintan en gris los nodos que (b) descartó. Así el árbol muestra
todo *y* deja ver cuánto se ahorró.

<a name="p23"></a>
## 2.3 `strips.py` — planificación y motor A\*

### La clase `Accion`

Es literalmente la estructura que sugiere el material de clase, con un campo añadido:

```python
class Accion:
    def __init__(self, nombre, precondiciones, add, delete, co2_costo=1):
        ...
    def es_aplicable(self, estado):
        return self.precondiciones <= estado        # ⊆ : subconjunto

    def aplicar(self, estado):
        if not self.es_aplicable(estado):
            return None
        return frozenset((estado - self.delete) | self.add)
```

Esa última línea **es** el axioma de persistencia de STRIPS: solo cambia lo que está en ADD y
DELETE; todo lo demás se mantiene solo. Es lo que evita tener que escribir miles de axiomas de
"esto no cambió".

Se usa `frozenset` y no `set` porque los estados tienen que ser **claves de diccionario** en el A\*
(para `g_score` y para el conjunto de visitados), y un `set` normal no es hashable.

> **Nota de lectura:** `precondiciones <= estado` no es "menor o igual". En conjuntos de Python,
> `<=` es "es subconjunto de". Se lee: *"¿todo lo que necesito está presente?"*

### El A\* sobre el espacio de estados

Aquí viene el salto conceptual de la Guía 4 a esta:

> **En la Guía 4 un nodo era un jugador del campo. Aquí un nodo es un estado completo del mundo:
> el conjunto de todo lo que es verdad en ese momento.**

```python
def heuristica(estado, meta):
    """h(n) = (predicados de la meta que faltan) × (costo mínimo de una acción)"""
    return len(meta - estado) * COSTO_MIN_ACCION
```

**¿Por qué es admisible?** Porque nunca promete de menos:

- Ninguna acción de costo 1 aporta **más de un** predicado de la meta.
- La única que aporta varios (`Ejecutar_Entrenamiento_Especifico`, 2–3 predicados) cuesta **5**,
  que es mayor que los 3 que estimaría la heurística.

Como `h` nunca sobreestima, A\* garantiza el plan óptimo. Es exactamente el mismo argumento de
relajación que usamos en la Guía 4 con `h(n) = (4 − zona) × 2`.

### La anomalía de Sussman, demostrada y no afirmada

Lo fácil habría sido escribir "aquí hay una anomalía de Sussman" en un comentario. En vez de eso,
el código **la provoca**:

```python
def planificador_lineal(estado_inicial, meta, acciones, orden_submetas):
    """Resuelve las sub-metas UNA POR UNA, como el STRIPS original."""
    estado = frozenset(estado_inicial)
    plan = []
    for submeta in orden_submetas:
        r = planificar_astar(estado, {submeta}, acciones)
        if not r["exito"]:
            return plan, estado, False, submeta      # ← se atascó
        ...
```

El conflicto real de nuestro dominio:

- `Ajustar_Plan_Nutricional` **borra** `atleta(en_recuperacion)`.
- `Aplicar_Descarga_Extra` **necesita** `atleta(en_recuperacion)`.
- Y esa precondición **no se puede recuperar**, porque la única acción que la produce
  (`Aplicar_Sesion_Regenerativa`) requiere `atleta(fatigado)` y `carga_semanal(alta)`, que ya se
  consumieron al principio y nadie vuelve a poner.

Resultado, medido por el propio programa:

| Orden de sub-metas | Resultado |
|---|---|
| Primero `atleta(recuperado)` | **BLOQUEADO** al intentar `reserva_energetica(alta)` |
| Primero `reserva_energetica(alta)` | Funciona: 6 pasos, CO₂ 10 |
| **A\*** (intercala en vez de ordenar) | Funciona siempre: 6 pasos, CO₂ 10 |

**Esa tabla es la demostración.** Un planificador lineal depende del orden en que le den las
sub-metas; A\*, que busca sobre estados completos y no sobre metas sueltas, no.

<a name="p24"></a>
## 2.4 `bayes.py` — la red

Es el código de la Guía 6 reorganizado como módulo. Tres diccionarios y cuatro funciones.

**La forma de la estructura de datos refleja el número de padres del nodo:**

```python
P_C         = {"Alta": 0.40, ...}                              # sin padres → plano
P_F_dado_C  = {"Alta": {"Alta": 0.75, "Baja": 0.25}, ...}      # un padre  → anidado
P_E_dado_CF = {("Alta", "Alta"): {"Exito": 0.25, ...}, ...}    # dos padres→ clave tupla
```

### El detalle que casi siempre se pasa por alto

Fíjate en que estas dos funciones hacen lo mismo conceptualmente, pero una divide y la otra no:

```python
def p_exito_dado_carga(c, p_c=None):
    return sum(P_E_dado_CF[(c, f)]["Exito"] * P_F_dado_C[c][f]
               for f in VALORES_F)                              # ← sin dividir

def p_exito_dado_fatiga(f_obs, p_c=None):
    num = sum(p_c[c] * P_F_dado_C[c][f_obs] * P_E_dado_CF[(c, f_obs)]["Exito"]
              for c in VALORES_C)
    den = sum(p_c[c] * P_F_dado_C[c][f_obs] for c in VALORES_C)
    return num / den                                            # ← dividiendo
```

**La razón:** `C` es la **raíz** de la red. Sus hijos ya vienen expresados condicionados a ella, así
que `P(F|C)` ya suma 1 para cada valor de `C`: los pesos están normalizados y no hay nada que
repartir.

Cuando la evidencia está en una variable que **no** es raíz (como `F`), los pesos ya no suman 1 y
hay que normalizar dividiendo. **Ese denominador es, literalmente, el `P(E)` del Teorema de Bayes.**

> **Analogía del denominador:** es como una elección. No importa cuántos votos sacó un candidato en
> bruto, sino qué **porcentaje** del total sacó. El denominador es el total de votos.

Si en la sustentación preguntan *"¿por qué aquí divides y allá no?"*, esa es la respuesta.

<a name="p25"></a>
## 2.5 `agente.py` — el pegamento

Todo el agente cabe en diez líneas conceptuales:

```python
evidencia = observar()                                  # F = Alta
post      = bayes.inferir(evidencia, p_c)               # P(E|F) = 0.325

conservador = post["exito"] < D.UMBRAL_EXITO            # 0.325 < 0.40 → True
meta = strips.META_CONSERVADORA if conservador else strips.META_BASE

plan = strips.planificar_astar(strips.ESTADO_INICIAL, meta, strips.ACCIONES)
dec  = minmax.decidir(profundidad, poda=True, heuristica=True, delta=escenario)
```

**La línea que hace que esto sea un agente es la tercera.** Es el único punto del programa donde
una probabilidad calculada cambia el objetivo de otro módulo.

### El registro doble

El enunciado pide que el flujo salga **en consola y en archivo**. Se resuelve en `dominio.py` con
seis líneas:

```python
_buffer_log = []

def log(texto=""):
    print(texto)                # consola
    _buffer_log.append(texto)   # y se guarda

def guardar_log(ruta=ARCHIVO_LOG):
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(_buffer_log) + "\n")
```

Todo lo que el agente "dice" pasa por `log()`, así que las dos salidas **no pueden
desincronizarse**: son el mismo texto.

### `agent_summary.png`

Se construye con `gridspec` en tres zonas, siguiendo al pie de la letra lo que pide el enunciado:

```python
gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.0], height_ratios=[1.0, 0.85])
ax1 = fig.add_subplot(gs[:, 0])   # el plan STRIPS, columna izquierda completa
ax2 = fig.add_subplot(gs[0, 1])   # la probabilidad bayesiana, arriba derecha
ax3 = fig.add_subplot(gs[1, 1])   # la decisión Min-Max, abajo derecha
```

La probabilidad se repite como **número grande** (32.5 %) además de la barra, y la decisión va en
un bloque rojo con tipografía de 23 puntos, porque el requisito dice *"a primera vista"*.

---

<a name="verificar"></a>
# 3. Cómo verificar que está bien

```bash
python test_regresion.py
```

31 comprobaciones repartidas en cinco grupos:

| Grupo | Qué verifica |
|---|---|
| 1 | Las 8 utilidades de la Guía 5 salen idénticas (−27, −1, +4, +21, +9, +19, +42, +41) |
| 2 | Min-Max reproduce la Guía 5: valor **+19**, rama `Moderada → Alta → Descansar`, 8 hojas sin poda, 6 con poda, 2 podas |
| 3 | Las 9 consultas bayesianas de la Guía 6 |
| 4 | STRIPS: 5 acciones y CO₂ 9 (estándar), 6 y 10 (conservadora), A\* mejora al forward, y el monitoreo precede al entrenamiento |
| 5 | La anomalía de Sussman se reproduce: el orden A se bloquea, el B no |

**La prueba más valiosa es la 2.** Verifica no solo que el resultado es el correcto, sino que
**la poda no cambia la decisión ni el valor** — que es la garantía teórica de α-β. Si alguna vez
difieren, hay un bug en la poda, no un descubrimiento.

---

<a name="glosario"></a>
# 4. Glosario

| Término | En una frase |
|---|---|
| **MAX / MIN** | Los dos "jugadores": nosotros y el organismo del atleta |
| **Utilidad** | La nota numérica de un resultado, para poder compararlo con otros |
| **Poda α-β** | Descartar ramas que ya no pueden cambiar la decisión |
| **Heurística de evaluación** | Estimar el valor de un estado sin expandir lo que queda debajo |
| **Precondición / ADD / DELETE** | Lo que una acción necesita, lo que enciende y lo que apaga |
| **Axioma de persistencia** | Solo cambia lo que está en ADD/DELETE; el resto se queda quieto |
| **Forward / Backward** | Razonar desde el estado inicial, o desde la meta hacia atrás |
| **Anomalía de Sussman** | Resolver una sub-meta puede bloquear otra para siempre |
| **Admisible** | Una heurística que nunca promete menos esfuerzo del real → A\* da el óptimo |
| **Prior / Posterior** | Lo que creías antes / lo que crees después de ver el dato |
| **CPT** | La tabla de probabilidades de un nodo, según los valores de sus padres |
| **Marginalizar** | Eliminar una variable que no conoces, sumando sobre sus valores |
| **Normalizar** | Dividir por el total para que el resultado sea un porcentaje válido |

---

## Fuentes

- **Guía 4** — A\* y Weighted A\*, y el argumento de admisibilidad por relajación.
- **Guía 5** — `PLANIFICACION-MAX MIN.md` y `Planificación STRIPS.md`: Min-Max, poda α-β, función
  de utilidad con métricas del sector, STRIPS forward/backward y la anomalía de Sussman. La
  instrucción de usar A\* como motor del planificador sale de su ACTIVIDAD 2.
- **Guía 6** — `PLANIFIC BAYESIANO.md`: estructura de la red, CPTs y los tres tipos de
  razonamiento.
- **Guía 2** — Marco Ético para la IA en Colombia (2021): el cierre *human-in-command*.
- **Métricas:** Catapult Sports y Kinexon (GPS/IMU, HRV, sueño), GHG Protocol adaptado a deporte
  (CO₂ metabólico), UEFA Medical Matters 2021 (riesgo de lesión por carga acumulada).
