# Planeación — Guía 6: Red Bayesiana del proyecto

> ⚠️ **Versión 2** — reescrita después de que la guía 5 cambiara de dominio.
> La red ahora modela la **gestión de carga del atleta** (Dominio B), que es donde viven el
> Min-Max y el STRIPS. Todo lo de aquí se reutiliza tal cual en el parcial.

## 1. Decisión de diseño: qué red construir

El profesor pide **tres variables que afectan un resultado**. Se copia la **estructura exacta** de
su ejemplo de turismo (`Clima → Transporte → Actividad`, con `P(C)`, `P(T|C)`, `P(A|C,T)`), porque
es la que él resolvió paso a paso.

Y se eligen las variables de modo que sean **las mismas del árbol Min-Max de la guía 5**:

```
        C (Carga semanal)
       / \
      /   \
     v     v
    F ---> E
 (Fatiga)  (Éxito competitivo)
```

| Variable | Significado | Valores | De dónde sale el dato |
|---|---|---|---|
| **C** | Carga de entrenamiento aplicada en la semana | Alta / Moderada | Decisión del cuerpo técnico — **es el Nivel 1 del árbol Min-Max** |
| **F** | Fatiga con que responde el organismo | Alta / Baja | HRV, sueño y carga GPS/IMU (Kinexon) — **es el Nivel 2 (MIN) del árbol** |
| **E** | Éxito competitivo (llega disponible y rinde) | Éxito / Fallo | Registro de disponibilidad y rendimiento en partido |

### Por qué esta elección es fuerte (decirlo en la exposición)
En el Min-Max, **MIN es un adversario perfecto**: siempre concede la fatiga que más nos perjudica.
Eso es pesimista por diseño. **La red bayesiana le pone probabilidad a ese mismo nodo MIN**: en vez
de asumir que el organismo siempre responde mal, calcula **qué tan probable es** que responda mal.

> **Min-Max da la decisión garantizada; Bayes da la decisión esperada. El agente del parcial usa
> las dos y muestra cuándo coinciden y cuándo no.**

Justificación de los arcos:
- `C → F`: una carga alta hace mucho más probable la fatiga alta. Es la relación que miden los GPS.
- `C → E` y `F → E`: el éxito depende de **ambos** — de cuánto entrenamos y de cómo respondió el
  cuerpo. Es el análogo exacto de `P(Actividad | Clima, Transporte)`.

## 2. CPTs propuestas (valores a validar con el grupo)

**Prior — `P(C)`**
| C | P |
|---|---|
| Alta | 0.40 |
| Moderada | 0.60 |

**`P(F | C)`**
| C | P(F=Alta) | P(F=Baja) |
|---|---|---|
| Alta | 0.75 | 0.25 |
| Moderada | 0.30 | 0.70 |

**`P(E | C, F)`**
| C | F | P(E=Éxito) | P(E=Fallo) |
|---|---|---|---|
| Alta | Alta | 0.25 | 0.75 |
| Alta | Baja | 0.65 | 0.35 |
| Moderada | Alta | 0.45 | 0.55 |
| Moderada | Baja | 0.85 | 0.15 |

> Se justifican como **estimaciones del cuerpo técnico a partir del histórico de disponibilidad**,
> igual que el profesor justifica las suyas ("probabilidades de ejemplo"). Están en un diccionario:
> cambiarlas es una línea.
>
> **Coherencia con el Min-Max:** el orden de estas probabilidades reproduce el orden de las
> utilidades de la guía 5 (`CM_FB` mejor, `CA_FA` peor). No son números sueltos.

## 3. Punto 2 del enunciado — probabilidad conjunta

`P(C, F, E) = P(C) · P(F|C) · P(E|C,F)`

```
P(C=Moderada, F=Baja, E=Éxito) = 0.60 × 0.70 × 0.85 = 0.357  →  35.7 %
```
**Interpretación:** algo más de un tercio de las semanas transcurren en el escenario ideal —carga
moderada, el cuerpo responde fresco y el atleta rinde—. Es el escenario que el Min-Max valora en
**+42** pero que **no puede garantizar**.

Contraste obligatorio:
```
P(C=Alta, F=Alta, E=Éxito) = 0.40 × 0.75 × 0.25 = 0.075  →  7.5 %
```
Es decir: forzar la carga y aun así rendir ocurre 1 de cada 13 semanas. En el árbol Min-Max esa
misma combinación vale **−27**, la peor hoja. Los dos modelos dicen lo mismo por vías distintas.

## 4. Punto 3 del enunciado — inferencia con evidencia parcial

**Marginal (sin evidencia):**
```
P(E=Éxito) = Σ_{C,F} P(C)·P(F|C)·P(E=Éxito|C,F) = 0.578  →  57.8 %
```

**Razonamiento causal — evidencia sobre la carga** (es la consulta idéntica a la del profesor,
`P(A|C=Bueno) = Σ_T P(A|C,T)·P(T|C)`):
```
P(E=Éxito | C=Moderada) = 0.30·0.45 + 0.70·0.85 = 0.135 + 0.595 = 0.730  →  73.0 %
P(E=Éxito | C=Alta)     = 0.75·0.25 + 0.25·0.65 = 0.1875 + 0.1625 = 0.350  →  35.0 %
```

**Razonamiento diagnóstico — evidencia sobre la fatiga (Bayes puro, contra la flecha):**
```
P(F=Alta) = 0.40·0.75 + 0.60·0.30 = 0.48
P(C=Alta | F=Alta) = 0.30 / 0.48 = 0.625  →  62.5 %   (el prior era 40 %)
```

**La consulta que usa el agente del parcial:**
```
P(E=Éxito | F=Alta) = [0.40·0.75·0.25 + 0.60·0.30·0.45] / 0.48 = 0.156 / 0.48 = 0.325  →  32.5 %
P(E=Éxito | F=Baja) = [0.40·0.25·0.65 + 0.60·0.70·0.85] / 0.52 = 0.422 / 0.52 = 0.812  →  81.2 %
```

**Interpretación para la exposición:** ver los biomarcadores alterados no solo hunde la expectativa
de éxito de **57.8 % a 32.5 %** — además **delata la carga que le pusimos al atleta**
(40 % → 62.5 %). Una sola observación actualiza dos creencias a la vez: eso es razonamiento
**causal** (C→E) y **diagnóstico** (F→C) sobre la misma red.

## 5. Qué construir (entregable de la guía 6)

Notebook `entregables/Red_Bayesiana_Rendimiento.ipynb`, con el estilo de la guía 5
(celda comentada → cálculo → lectura del resultado):

1. **Celda 1:** CPTs como diccionarios. **Bayes a mano**, sin librerías de redes bayesianas, para
   poder mostrar el paso a paso como en los ejemplos del profesor.
2. **Celda 2:** dibujo de la red con `networkx`, con las CPTs anotadas junto a cada nodo.
   Paleta de la guía 5 (`ROJO="#E74C3C"`, `AZUL="#2980B9"`, `VERDE="#27AE60"`, `NARANJA="#E67E22"`).
3. **Celda 3:** tabla de la **distribución conjunta completa** (8 filas) + verificación de que suma 1.
4. **Celda 4:** probabilidad conjunta del escenario pedido + interpretación.
5. **Celda 5:** inferencia con evidencia parcial: marginal vs `C=Moderada` vs `C=Alta` vs `F=Alta`,
   más el diagnóstico `P(C=Alta|F=Alta)`.
6. **Celda 6:** **gráfico de barras** con `P(E=Éxito)` en los distintos escenarios de evidencia.
   👉 Hacerlo ya con el nombre y el formato de **`bayes_bars.png`** del parcial: la evidencia usada
   debe aparecer escrita **dentro** de la figura.
7. **Celda 7:** los tres tipos de razonamiento del PDF aplicados al caso:
   - **Causal:** "si aplicamos carga alta, ¿qué probabilidad de éxito hay?" → 35 %.
   - **Diagnóstico:** "el atleta llegó fatigado, ¿fue por la carga?" → 62.5 %.
   - **Intercausal (explaining away):** si confirmamos que la fatiga vino de un **viaje largo** y no
     de la carga, la probabilidad de `C=Alta` vuelve a bajar. Una causa explica y descarta la otra.
8. **Celda 8 — la que conecta con la guía 5:** comparar la **decisión Min-Max** (pesimista,
   garantizada) con la **decisión bayesiana** (esperada). Tabla: para cada carga, utilidad Min-Max
   vs utilidad esperada ponderada por `P(F|C)`. Es el puente hacia el parcial.

## 6. Orden de trabajo
1. Validar las 3 variables y las CPTs con el grupo *(ver `../../preguntas.md`)*.
2. Escribir el notebook; verificar que la conjunta suma 1 y que los números coinciden con los de
   arriba (están calculados y verificados).
3. Generar `bayes_bars.png`.
4. Presentación (Gamma).

## 7. Enlaces con el resto del curso
- **Guía 5:** mismas variables que los niveles 1 y 2 del árbol Min-Max. El CO₂ metabólico es el
  mecanismo físico detrás de `P(F|C)`.
- **Guía 4:** allí un escenario adverso se **imponía** a mano (marca sobre MO); aquí se le asigna
  **probabilidad**.
- **Parcial:** `P(E=Éxito | F=Alta)` es la "probabilidad de éxito" del agente, y `P(C=Alta)` es el
  prior que se barre en el análisis de sensibilidad.
