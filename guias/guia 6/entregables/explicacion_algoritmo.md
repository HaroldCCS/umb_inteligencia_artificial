# Cómo funciona el algoritmo — Red Bayesiana aplicada al Rendimiento Deportivo

**Guía 6 · Inteligencia Artificial**
Keiry Lucía Olaya Noguera · Harold Stiven Camargo Castellanos · Juan Felipe Coronel Montes

Documento de acompañamiento del notebook `Red_Bayesiana_Rendimiento.ipynb`.
Se explica en dos niveles: **primero la idea** (sin una sola línea de código) y **después la
mecánica** (qué hace cada función, línea por línea).

---

# Índice

1. [El problema en una frase](#0)
2. [**Parte 1 — Cómo funciona a alto nivel**](#parte1)
3. [**Parte 2 — Cómo funciona a bajo nivel**](#parte2)
4. [Cómo verificar que está bien](#verificar)
5. [Cómo cambiar los datos](#cambiar)
6. [Glosario](#glosario)

---

<a name="0"></a>
# 0. El problema en una frase

> Queremos decidir cómo preparar a un futbolista durante la semana, sabiendo que **el cuerpo no
> responde siempre igual**: a veces una carga fuerte lo deja fresco y a veces una carga suave lo
> deja fundido.

En la **Guía 5** resolvimos esto con Min-Max, que asume lo peor: que el organismo **siempre** va a
responder de la forma que más nos perjudique. Es prudente, pero es pesimista.

Lo que falta es poder decir **"esto pasa el 75 % de las veces"** en lugar de **"esto puede pasar"**.
Eso es lo que hace una red bayesiana.

---

<a name="parte1"></a>
# PARTE 1 — Cómo funciona a ALTO NIVEL

*(Esta parte se entiende sin saber programar.)*

## 1.1 La analogía madre: el médico de cabecera

Imagina un médico con veinte años de consulta. Llega un paciente con fiebre. El médico **no** dice
"fiebre ⇒ gripe". Lo que hace su cabeza es algo más fino:

1. **Antes de verlo, ya tenía una expectativa.** Sabe que en esta época del año, más o menos 1 de
   cada 10 pacientes que entran tiene gripe. Eso es lo que en el algoritmo llamamos
   **probabilidad previa** o *prior*.
2. **Observa un síntoma.** Fiebre.
3. **Actualiza su expectativa.** No la reemplaza: la **mueve**. La gripe pasa de ser una sospecha
   del 10 % a una del 51 %.
4. **Si llega otro dato, vuelve a mover la expectativa.** Y si le dicen que el paciente acaba de
   volver de un viaje, puede incluso *bajar* la sospecha de gripe, porque ahora hay otra
   explicación que compite.

**Una red bayesiana es exactamente eso, escrito como programa.** Ese ejemplo de la gripe no es
inventado: es el primer ejemplo resuelto del material de clase, y da 50.9 %.

## 1.2 Qué es nuestra red

Nosotros cambiamos el consultorio por el gimnasio. El "paciente" es el futbolista, los "síntomas"
son los datos del chaleco GPS, y la "enfermedad" que queremos anticipar es **no llegar en forma al
partido**.

Nuestra red tiene **tres variables**:

| | Variable | Qué significa | Valores posibles |
|---|---|---|---|
| **C** | Carga semanal | Cuánto lo hicimos entrenar esta semana | Alta / Moderada |
| **F** | Fatiga | Cómo respondió su cuerpo | Alta / Baja |
| **E** | Éxito competitivo | Si llega disponible y rinde | Éxito / Fallo |

Y las conectamos con flechas que significan **"influye en"**:

```
             C  (Carga semanal)
            / \
           /   \
          v     v
         F ────> E
     (Fatiga)   (Éxito competitivo)
```

Se lee así:

- **La carga influye en la fatiga.** Si lo reventamos el martes, es más probable que llegue
  fundido el sábado.
- **La fatiga influye en el éxito.** Un jugador fundido rinde menos y se lesiona más.
- **La carga también influye directamente en el éxito**, por un camino que no pasa por la fatiga:
  un jugador que entrena poco llega descansado *pero sin ritmo de competencia*.

> ⚠️ **El detalle que hay que poder defender en la sustentación no son los números, son las
> flechas.** Los números se pueden discutir; la estructura es la afirmación fuerte que estamos
> haciendo sobre cómo funciona el mundo.

## 1.3 Qué información le damos: las tres "fichas"

Cada variable trae su propia **tablita de probabilidades**, que en la jerga se llama **CPT**
(*Tabla de Probabilidad Condicional*). Responde a: *"¿qué tan probable es esto, dado lo que pasó
antes?"*.

**Ficha de C** — no depende de nadie, así que es la más simple:
> De cada 10 semanas, en 4 aplicamos carga alta y en 6 carga moderada.

**Ficha de F** — depende de C:
> Si la carga fue alta → llega fatigado el 75 % de las veces.
> Si fue moderada → llega fatigado solo el 30 %.

**Ficha de E** — depende de C **y** de F, así que tiene 4 filas (todas las combinaciones):
> Carga alta + fatigado → rinde el 25 % de las veces.
> Carga alta + fresco → 65 %.
> Carga moderada + fatigado → 45 %.
> Carga moderada + fresco → 85 %.

**Analogía:** una CPT es como la etiqueta nutricional de un producto. No te dice qué vas a comer
hoy; te dice qué aporta *ese* producto si lo comes. La red junta todas las etiquetas para calcular
el resultado de la comida completa.

## 1.4 Qué le preguntamos: tres tipos de pregunta

Una vez armada la red, se le pueden hacer tres clases de preguntas. **Es la misma red, cambia la
dirección en la que se razona.**

### (a) Razonamiento causal — "si hago esto, ¿qué va a pasar?"

Va **a favor** de las flechas, de la causa al efecto.

> *"Si esta semana aplico carga moderada, ¿qué probabilidad hay de que el jugador rinda?"*
> **Respuesta: 73 %.** Con carga alta, solo **35 %.**

**Analogía:** es el pronóstico del tiempo. Sabes que viene un frente frío (causa) y predices que
va a llover (efecto).

**Para qué sirve:** para **planificar**. Es la pregunta que se hace el preparador físico el lunes.

### (b) Razonamiento diagnóstico — "vi esto, ¿qué lo causó?"

Va **en contra** de las flechas, del efecto a la causa. Aquí es donde entra el **Teorema de Bayes**
en su forma clásica.

> *"El jugador llegó fatigado. ¿Qué probabilidad hay de que sea porque le pusimos carga alta?"*
> **Respuesta: 62.5 %** — cuando antes de verlo pensábamos que solo un 40 %.

**Analogía:** es el mecánico. Oye un ruido en el motor (efecto) y deduce cuál de las piezas
posibles es la culpable (causa). No lo sabe con certeza, pero sabe cuál es **la explicación más
probable**.

**Para qué sirve:** para **auditar**. Es la pregunta que se hace el cuerpo técnico el viernes
cuando ve las planillas y el jugador está fundido.

### (c) Razonamiento intercausal — "¿esta evidencia descarta la otra posibilidad?"

Este es el más sutil y el más humano. Aparece cuando **un efecto tiene dos causas que compiten**.

**Analogía (la más clara de todas):** tu amigo llega tarde a la cita. Dos explicaciones posibles:
*se quedó dormido* o *había trancón en la Séptima*. Al principio sospechas de las dos. Pero
entonces ves en las noticias que hubo un choque que cerró la vía. En ese instante, **sin que nadie
te diga nada sobre tu amigo**, la sospecha de que se quedó dormido **baja**.

Eso se llama ***explaining away***: una causa confirmada "explica" el efecto y **descarta** a la
otra.

En nuestro caso añadimos una segunda causa de la fatiga: **un viaje largo**.

| Lo que sabemos | ¿Fue culpa de la carga alta? |
|---|---|
| Solo que llegó fatigado | **62.5 %** |
| … y además confirmamos que voló 9 horas el martes | **50.0 %** ↓ |
| … y confirmamos que **no** viajó | **68.0 %** ↑ |

**Por qué importa de verdad:** sin este razonamiento, el sistema le echaría la culpa a la
planificación **cada vez** que un jugador llega fatigado, y el preparador terminaría bajando cargas
que no eran el problema. Con él, el sistema distingue: *"está fundido, pero voló 9 horas; la carga
no era el problema"*.

## 1.5 El resultado, en una imagen

Antes de mirar los sensores, nuestra expectativa de éxito es **una sola cifra: 57.8 %**.
Después de mirarlos, esa cifra **se parte en dos mundos muy distintos**:

```
                          Sin evidencia
                             57.8 %
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
       llega FATIGADO                       llega FRESCO
           32.5 %                              81.2 %
```

Casi **49 puntos porcentuales** de diferencia. En la práctica, esa es la diferencia entre alinear
al jugador o dejarlo en el banco.

## 1.6 Por qué esto le faltaba al proyecto

Los tres métodos del corte se reparten el trabajo así:

| Método | Cómo trata al mundo | Analogía |
|---|---|---|
| **STRIPS** (Guía 5) | Como si nada pudiera salir mal | La receta de cocina: *"sigue estos 5 pasos y saldrá bien"* |
| **Min-Max** (Guía 5) | Como si todo fuera a salir mal | El ajedrecista: *"asumo que mi rival juega perfecto"* |
| **Bayes** (esta guía) | Como es: incierto | El médico: *"con lo que veo, creo esto — y cambio de opinión si llega otro dato"* |

> **Bayes es el único de los tres que cambia de opinión cuando llega un dato nuevo.**
> Por eso es el que le permite al agente del parcial **observar antes de decidir**.

Y hay un número que lo resume. En la Guía 5, Min-Max elegía carga moderada con un valor
**garantizado de +19**. Ponderando con las probabilidades reales, el valor **esperado** es **+35.1**:
casi el doble. Esa diferencia **es el precio del pesimismo**. Min-Max no se equivoca en *qué* hacer
—las dos decisiones coinciden—, pero sí subestima cuánto vale hacerlo.

---

<a name="parte2"></a>
# PARTE 2 — Cómo funciona a BAJO NIVEL

*(Aquí sí hace falta leer código. Todo está en `Red_Bayesiana_Rendimiento.ipynb`.)*

## 2.1 Decisión de diseño: por qué no usamos una librería

Existen librerías que hacen esto solas (`pgmpy`, por ejemplo). **No las usamos a propósito.**

El material de clase resuelve todos sus ejemplos a mano, paso a paso: `Paso 1 — Numerador`,
`Paso 2 — Contribución`, `Paso 3 — Denominador`, `Paso 4 — Resultado`. Si usáramos una librería,
tendríamos el número correcto pero **no podríamos mostrar el razonamiento**, que es justamente lo
que se está evaluando.

Así que todo el cálculo bayesiano son **diccionarios de Python y aritmética**. Las únicas librerías
son `matplotlib` (gráficos), `networkx` (dibujar el grafo) y `pandas` (tablas).

## 2.2 Cómo se representa la red: tres diccionarios

```python
# CPT 1: P(C) — no depende de nadie, es un diccionario plano
P_C = {
    "Alta":     0.40,
    "Moderada": 0.60,
}

# CPT 2: P(F | C) — depende de UN padre, es un diccionario de diccionarios
P_F_dado_C = {
    "Alta":     {"Alta": 0.75, "Baja": 0.25},   # si C=Alta...
    "Moderada": {"Alta": 0.30, "Baja": 0.70},   # si C=Moderada...
}

# CPT 3: P(E | C, F) — depende de DOS padres, la clave es una TUPLA
P_E_dado_CF = {
    ("Alta",     "Alta"): {"Exito": 0.25, "Fallo": 0.75},
    ("Alta",     "Baja"): {"Exito": 0.65, "Fallo": 0.35},
    ("Moderada", "Alta"): {"Exito": 0.45, "Fallo": 0.55},
    ("Moderada", "Baja"): {"Exito": 0.85, "Fallo": 0.15},
}
```

**La regla que hay que entender:** *la forma de la estructura de datos refleja el número de padres
del nodo en el grafo.*

- Sin padres → diccionario plano.
- Un padre → diccionario de diccionarios: `P_F_dado_C[valor_del_padre][valor_propio]`.
- Dos padres → clave **tupla**: `P_E_dado_CF[(padre1, padre2)][valor_propio]`.

Se usa tupla porque en Python una tupla **sí puede ser clave** de un diccionario (una lista no,
porque es mutable). Y leerlo `P_E_dado_CF[("Alta", "Baja")]["Exito"]` se parece muchísimo a
escribir `P(E=Éxito | C=Alta, F=Baja)`, que era el objetivo.

**Validación automática.** Al final de la celda 2 se comprueba que **toda distribución sume 1.0**.
Es la primera defensa contra errores de dedo: si alguien cambia un 0.75 por 0.85 y olvida ajustar
el complemento, el notebook lo grita.

## 2.3 La probabilidad conjunta: multiplicar las tres fichas

```python
def p_conjunta(c, f, e):
    """Probabilidad conjunta de una combinacion completa (c, f, e)."""
    return P_C[c] * P_F_dado_C[c][f] * P_E_dado_CF[(c, f)][e]
```

Tres líneas, pero es **el teorema que sostiene todo**:

$$P(C, F, E) = P(C)\cdot P(F \mid C)\cdot P(E \mid C, F)$$

Cada factor es la ficha de un nodo, evaluada en los valores de sus padres.

**Analogía:** es una receta. En vez de memorizar el sabor final de los 8 platos posibles, memorizas
qué aporta cada ingrediente y lo multiplicas. Con 3 variables la diferencia parece poca (8 casos
contra 3 tablitas), pero con 20 variables serían **más de un millón** de casos contra 20 tablitas.
**Esa es la razón de existir de las redes bayesianas.**

Ejemplo real del notebook:

```
P(C=Moderada, F=Baja, E=Exito)
  = P(C=Moderada) × P(F=Baja|C=Moderada) × P(E=Exito|C=Moderada,F=Baja)
  = 0.60 × 0.70 × 0.85
  = 0.357   →   35.7 %
```

Y la comprobación: **las 8 combinaciones suman exactamente 1.00000**. Si no sumaran 1, habría un
error en las CPTs.

## 2.4 La probabilidad marginal: sumar lo que no sabemos

```python
p_exito_marginal = 0.0
for c, f in product(VALORES_C, VALORES_F):
    term = P_C[c] * P_F_dado_C[c][f] * P_E_dado_CF[(c, f)]["Exito"]
    p_exito_marginal += term
```

`product()` genera las 4 combinaciones de `(C, F)`. Para cada una calculamos la conjunta y las
sumamos todas.

Esto se llama **marginalizar**: eliminar una variable sumando sobre todos sus valores posibles.

**Analogía:** es como calcular el promedio de notas de un salón cuando no sabes quién es quién.
Sumas todos los casos posibles con el peso que le corresponde a cada uno.

Resultado: **57.8 %**. Esta es la **línea base** contra la que se compara todo lo demás.

## 2.5 Inferencia causal: `p_exito_dado_carga()`

```python
def p_exito_dado_carga(c, verbose=True):
    """P(E=Exito | C=c) por la regla de la probabilidad total."""
    total = 0.0
    for f in VALORES_F:
        pe = P_E_dado_CF[(c, f)]["Exito"]
        pf = P_F_dado_C[c][f]
        total += pe * pf
    return total
```

Fórmula: $P(E \mid C) = \sum_F P(E \mid C,F)\cdot P(F \mid C)$

Sabemos `C`, no sabemos `F`, así que marginalizamos sobre `F`, pesando cada valor de `F` por su
probabilidad **dada la carga que ya conocemos**.

### 🔑 El detalle fino que casi siempre se pasa por alto

**Fíjate que esta función NO divide por nada.** La de la sección siguiente **sí divide**. ¿Por qué?

> Porque `C` es la **raíz** de la red. Sus hijos ya vienen expresados "condicionados a C":
> `P(F|C)` ya suma 1 para cada valor de `C`. Los pesos ya están normalizados, no hay nada que
> repartir.
>
> Cuando la evidencia está en una variable que **no** es raíz (como `F`), los pesos **no** suman 1
> y hay que **normalizar dividiendo**. Eso es, literalmente, el denominador del Teorema de Bayes.

Si alguien pregunta en la sustentación *"¿por qué aquí divides y allá no?"*, esa es la respuesta.

Resultados: `P(E|C=Moderada) = 73.0 %` · `P(E|C=Alta) = 35.0 %`.

## 2.6 Inferencia diagnóstica: el Teorema de Bayes explícito

Esta es la celda 8, y está escrita **imitando el formato del material de clase**, con sus cuatro
pasos:

```python
# Paso 1 — numerador
num = P_F_dado_C["Alta"][f_obs] * P_C["Alta"]          # 0.75 × 0.40 = 0.3000

# Paso 2 — contribucion del otro valor de C
otro = P_F_dado_C["Moderada"][f_obs] * P_C["Moderada"] # 0.30 × 0.60 = 0.1800

# Paso 3 — denominador  P(F=Alta)
p_f = num + otro                                       # 0.3000 + 0.1800 = 0.4800

# Paso 4 — resultado
post_c_alta = num / p_f                                # 0.3000 / 0.4800 = 0.6250
```

$$P(C \mid F) = \frac{P(F \mid C)\cdot P(C)}{P(F)}$$

**Qué es cada pieza, en palabras:**

- **Numerador** = "qué tan bien explica la hipótesis *carga alta* lo que estoy viendo, pesado por
  lo probable que era esa hipótesis de entrada".
- **Denominador** = "la suma de lo mismo para **todas** las hipótesis posibles".
- **La división** = convertir eso en un porcentaje.

**Analogía del denominador:** es como una elección. Lo que importa no es cuántos votos sacó un
candidato en bruto, sino **qué porcentaje del total** sacó. El denominador es el total de votos, y
dividir es calcular el porcentaje. Por eso, cuando aparece una **nueva** explicación posible, el
porcentaje de las anteriores **baja** aunque sus votos no hayan cambiado — y eso es exactamente el
mecanismo de *explaining away*.

Resultado: **62.5 %**, desde un prior de 40 %.

## 2.7 La consulta del agente: `p_exito_dado_fatiga()`

```python
def p_exito_dado_fatiga(f_obs, verbose=True):
    """P(E=Exito | F=f_obs). Marginaliza sobre C."""
    num = sum(P_C[c] * P_F_dado_C[c][f_obs] * P_E_dado_CF[(c, f_obs)]["Exito"]
              for c in VALORES_C)
    den = sum(P_C[c] * P_F_dado_C[c][f_obs] for c in VALORES_C)
    return num / den
```

Esta es la más completa de todas, porque combina las dos direcciones:

1. **Va hacia atrás** de `F` a `C` (no sabemos qué carga se aplicó).
2. **Va hacia adelante** de `C` a `E`.

El `num` recorre las dos hipótesis de carga, y para cada una multiplica: *qué tan probable era esa
carga* × *qué tan bien explica la fatiga observada* × *qué éxito produce*.
El `den` es `P(F=f_obs)`: el total, para normalizar (por lo explicado en 2.5).

Resultados: `P(E|F=Alta) = 32.5 %` · `P(E|F=Baja) = 81.2 %`.

**Este es el número que el agente integrador del parcial usa en su paso `observe → posterior`.**

## 2.8 *Explaining away*: `p_carga_alta_dado()`

Para mostrar el tercer tipo de razonamiento hace falta una **segunda causa** de la fatiga, así que
se extiende temporalmente la red:

```
      C (Carga alta)      V (Viaje largo)
              \            /
               v          v
                 F (Fatiga)
```

```python
def p_carga_alta_dado(f_obs="Alta", v_obs=None):
    """P(C=Alta | F=f_obs [, V=v_obs]) en la red extendida."""
    valores_v = [v_obs] if v_obs else list(P_V)     # <- la clave está aquí

    def peso(c, v):
        pf = P_F_dado_CV[(c, v)] if f_obs == "Alta" else 1 - P_F_dado_CV[(c, v)]
        return P_C[c] * P_V[v] * pf

    num = sum(peso("Alta", v) for v in valores_v)
    den = sum(peso(c, v) for c in VALORES_C for v in valores_v)
    return num / den
```

**El truco está en una sola línea:** `valores_v = [v_obs] if v_obs else list(P_V)`.

- Si **no** sabemos nada del viaje → se recorren **los dos** valores de `V` (se marginaliza).
- Si **sí** sabemos del viaje → se recorre **solo** ese valor (se condiciona).

Es decir: **marginalizar y condicionar son el mismo bucle, cambiando sobre qué se itera.** Esa es
una de las ideas más elegantes de todo el tema.

**Calibración honesta de las CPTs.** Los valores de `P(F|C,V)` no son inventados al azar: están
elegidos para que, **al marginalizar el viaje, se recupere la `P(F|C)` de la red original**:

```
P(F=Alta|C=Alta)     = 0.20×0.90 + 0.80×0.70 = 0.740   (red simple: 0.75)
P(F=Alta|C=Moderada) = 0.20×0.60 + 0.80×0.22 = 0.296   (red simple: 0.30)
```

Por eso el resultado sin evidencia de viaje da **62.5 %**: exactamente el mismo número de la red de
3 nodos. **La extensión es consistente con el modelo principal, no es un modelo distinto.**

## 2.9 Las dos figuras

| Función | Qué hace | Archivo |
|---|---|---|
| Celda 3 | Dibuja el DAG con `networkx` y anota las tres CPTs en recuadros | `red_bayesiana.png` |
| Celda 10 | Gráfico de barras de `P(E=Éxito)` bajo cada evidencia | `bayes_bars.png` |

Detalles de implementación que importan:

- Las posiciones de los nodos son **manuales** (`pos = {"C": (0,1), ...}`), no automáticas. Con un
  layout automático la red sale rotada y distinta en cada ejecución; con posiciones fijas, la
  figura es siempre idéntica y se puede explicar en clase.
- En `bayes_bars.png` la **evidencia utilizada está escrita dentro de la figura** (el recuadro
  amarillo). No es decoración: es un **requisito explícito** del Parcial Práctico 1.
- La línea punteada gris marca la línea base sin evidencia, para que se vea de un golpe qué
  evidencias suben la expectativa y cuáles la bajan.

## 2.10 Coste computacional

Con 3 variables binarias hay $2^3 = 8$ combinaciones. Los bucles son triviales.

En general, este método (**inferencia por enumeración**) recorre $2^n$ combinaciones para $n$
variables binarias: crece exponencialmente y deja de ser viable alrededor de las 25–30 variables.
Existen algoritmos más eficientes (*eliminación de variables*, *árbol de uniones*) y métodos
aproximados por muestreo. **Para nuestro caso la enumeración es lo correcto**: es exacta, es
inmediata y —lo más importante— **es la única que permite mostrar el paso a paso** en la
sustentación.

---

<a name="verificar"></a>
# 3. Cómo verificar que está bien

El notebook trae sus propias comprobaciones. Si alguna falla, hay un error:

| # | Comprobación | Dónde | Qué debe dar |
|---|---|---|---|
| 1 | Toda CPT suma 1.0 | Celda 2 | *"Todas las distribuciones suman 1.0"* |
| 2 | La conjunta de las 8 filas suma 1.0 | Celda 4 | `SUMA TOTAL = 1.00000` |
| 3 | La marginal cae entre los dos condicionales | Celdas 6–7 | `35.0 % < 57.8 % < 73.0 %` |
| 4 | El posterior se mueve respecto al prior | Celda 8 | `40 % → 62.5 %` |
| 5 | *Explaining away* baja la sospecha | Celda 11 | `62.5 % → 50.0 %` |
| 6 | Min-Max reproduce la Guía 5 | Celda 12 | garantizado `+19`, carga moderada |

La comprobación **3** es la más útil como prueba de olfato: **una probabilidad marginal siempre
tiene que quedar entre el mínimo y el máximo de sus condicionales**. Si la marginal se sale de ese
rango, hay un error de cálculo seguro.

---

<a name="cambiar"></a>
# 4. Cómo cambiar los datos

Todo el modelo vive en la **celda 2**. Para probar otro escenario:

1. Cambia el valor que quieras en `P_C`, `P_F_dado_C` o `P_E_dado_CF`.
2. Asegúrate de que cada distribución siga sumando 1 (si subes `"Alta": 0.75` a `0.85`, baja
   `"Baja"` a `0.15`).
3. Ejecuta el notebook completo (`Entorno de ejecución → Ejecutar todas`).

**Todo se recalcula solo:** las tablas, los cuatro tipos de inferencia, las dos figuras y la
comparación con Min-Max. No hay ningún número escrito a mano en el texto de salida.

Escenarios interesantes para probar en vivo:

| Prueba | Qué cambiar | Qué debería pasar |
|---|---|---|
| Un atleta muy entrenado | `P_F_dado_C["Alta"]["Alta"]` de `0.75` a `0.45` | El diagnóstico `P(C=Alta\|F=Alta)` baja: la fatiga ya no delata la carga |
| Pretemporada (casi siempre carga alta) | `P_C["Alta"]` de `0.40` a `0.80` | `P(E=Éxito)` marginal se desploma |
| Un plantel frágil | Bajar todas las `P(E=Exito\|...)` | Min-Max y Bayes se separan: ahí empieza la discusión interesante |

---

<a name="glosario"></a>
# 5. Glosario

| Término | En una frase |
|---|---|
| **DAG** | Grafo dirigido acíclico: flechas con un sentido y sin poder volver al inicio siguiéndolas |
| **Prior** (probabilidad previa) | Lo que creías **antes** de ver ningún dato |
| **Posterior** | Lo que crees **después** de ver el dato |
| **Evidencia** | El dato que observaste (aquí: la fatiga medida por los sensores) |
| **CPT** | La tablita de un nodo: su probabilidad para cada combinación de valores de sus padres |
| **Marginalizar** | Eliminar una variable que no conoces, sumando sobre todos sus valores |
| **Normalizar** | Dividir por el total para que el resultado sea un porcentaje válido |
| **Razonamiento causal** | Ir de la causa al efecto (a favor de las flechas) |
| **Razonamiento diagnóstico** | Ir del efecto a la causa (contra las flechas) — Teorema de Bayes |
| **Explaining away** | Confirmar una causa baja la probabilidad de la otra causa rival |
| **Independencia condicional** | Dos variables dejan de informarse entre sí cuando ya conoces a su causa común |

---

## Fuentes

- **Material de clase:** `guias/guia 6/recursos/PLANIFIC BAYESIANO.md` — de ahí salen la
  estructura de la red (`Clima → Transporte → Actividad`), el formato de resolución en cuatro pasos
  y los tres tipos de razonamiento.
- **Fatiga:** variabilidad de la frecuencia cardíaca (HRV), calidad de sueño y carga acumulada
  medida con GPS/IMU — Kinexon, Catapult Sports.
- **Carga semanal:** planillas de planificación del cuerpo técnico.
- **Éxito competitivo:** registro histórico de disponibilidad y rendimiento en partido.
- **Función de utilidad de la sección Min-Max:** Guía 5,
  `entregables/Algoritmo_Rendimiento_deportivo.ipynb`.
