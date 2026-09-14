# Proyecto de grupo — IA aplicada al Rendimiento Deportivo

> Ficha maestra del proyecto. Es el archivo que hay que leer **antes** de trabajar en cualquier guía.
> Si algo aquí contradice una guía, gana este archivo (o se corrige aquí explícitamente).

## 1. Identidad

- **Curso:** Inteligencia Artificial — Universidad Manuela Beltrán (UMB)
- **Sector elegido:** Rendimiento Deportivo y Analítica Avanzada — **fútbol profesional**
- **Integrantes:**
  - Keiry Lucía Olaya Noguera
  - Harold Stiven Camargo Castellanos
  - Juan Felipe Coronel Montes
- **Idioma de los entregables:** español.

## 2. El problema que resolvemos (hilo conductor del curso)

**Producto imaginado:** un **asistente de IA para el cuerpo técnico**, que apoya dos decisiones
distintas del mismo club:

1. **En el partido** *(Dominio A)* — una tablet en el banquillo recibe el posicionamiento en tiempo
   real y responde: *"¿por qué cadena de pases debe salir el equipo desde su portería para llegar
   al delantero perdiendo el balón lo menos posible?"*
   Restricción de negocio: **no sirve la ruta perfecta calculada tarde**. Por eso Weighted A\*, y
   por eso el peso `w` se calibra con datos, no por intuición.

2. **En la semana** *(Dominio B)* — el mismo sistema planifica la preparación: *"¿qué secuencia de
   acciones lleva al atleta de fatigado a listo para competir, sin romperlo?"*
   Restricción: el daño no aparece el mismo día, así que la decisión se toma asumiendo la **peor
   respuesta posible del organismo** (Min-Max) y se corrige con lo que dicen los sensores (Bayes).

En ambos casos la métrica que atraviesa todo es la **carga metabólica del atleta medida con
GPS/IMU**, expresada como CO₂ equivalente.

## 3. Los dos dominios del proyecto

El sector es uno solo (rendimiento deportivo), pero el proyecto ha modelado **dos problemas
distintos** dentro de él. Hay que tener claro cuál se usa en cada guía.

| | **Dominio A — Red de pases** | **Dominio B — Gestión de carga del atleta** |
|---|---|---|
| Pregunta | ¿Por qué cadena de pases sale el equipo desde la portería hasta el delantero? | ¿Cómo llevo al atleta de fatigado a listo para competir sin romperlo? |
| Guías | 3, 4 | 5, 6, **parcial práctico 1** |
| Métodos | BFS, DFS, UCS, Greedy, A\*, Weighted A\* | Min-Max + α-β, STRIPS, Redes Bayesianas |
| Métrica principal | Riesgo de intercepción (1–10) | Rendimiento, riesgo de lesión, recuperación (0–10) |
| Métrica puente | **CO₂ metabólico (GPS/IMU)** | **CO₂ metabólico (GPS/IMU)** |

**El CO₂ metabólico es lo que une los dos dominios**, y es el sello del grupo: no es ambientalismo
decorativo, es la **carga metabólica del atleta** medida con GPS/IMU (Catapult, Kinexon) bajo
metodología GHG Protocol adaptada.

- En el **Dominio A** funciona como **costo de arista**: `Costo = Riesgo + (CO₂ × λ)`.
- En el **Dominio B** funciona como **penalización en la utilidad** (`− CO₂ × 2`) y, sobre todo,
  como **precondición lógica** en STRIPS: `co2_acumulado(alto)` bloquea el entrenamiento de alta
  intensidad hasta que se reduce.

> ⚠️ **El parcial se construye sobre el Dominio B.** El Dominio A se menciona como antecedente,
> no se integra.

---

## 4. Dominio A — Modelo técnico (guías 3 y 4)

**Nunca redefinir esto. Copiarlo del entregable de la guía 5.**

### Nodos = jugadores (formación 4-2-3-1)
`POR, LTI, DFI, DFD, LTD, MC1, MC2, EXI, MO, EXD, DL`

| Zona | Jugadores |
|---|---|
| 0 — portería | POR |
| 1 — defensa | LTI, DFI, DFD, LTD |
| 2 — mediocampo | MC1, MC2 |
| 3 — último tercio | EXI, MO, EXD |
| 4 — área rival | DL |

### Aristas = pases posibles
```python
grafo = {
    'POR': [('DFI', 2), ('DFD', 2), ('LTI', 2), ('LTD', 2)],
    'DFI': [('DFD', 1), ('LTI', 1), ('MC1', 2)],
    'DFD': [('DFI', 1), ('LTD', 1), ('MC2', 2)],
    'LTI': [('DFI', 1), ('MC1', 3), ('EXI', 4)],
    'LTD': [('DFD', 1), ('MC2', 3), ('EXD', 4)],
    'MC1': [('MC2', 1), ('MO',  2), ('EXI', 3)],
    'MC2': [('MC1', 1), ('MO',  3), ('EXD', 3)],
    'EXI': [('DL',  8), ('MO',  2)],
    'MO':  [('DL',  3), ('EXI', 2), ('EXD', 2)],
    'EXD': [('DL',  9), ('MO',  2)],
    'DL':  [],
}
```

### Métricas del sector (las dos que justifican todo)
1. **Riesgo de intercepción (1–10)** = peso de la arista. *No es distancia*: es cuántas veces se
   pierde ese pase según el análisis de video. Fuente conceptual: Stats Perform / Hudl.
2. **Huella de CO₂ equivalente (1–5)** = **carga metabólica** del pase, medida con GPS/IMU
   (Catapult, Kinexon), bajo metodología GHG Protocol adaptada.
   1 = pase corto en defensa · 2 = pase medio · 3 = pase largo a banda · 5 = centro al área.

### Función de costo combinada
```
Costo(pase) = Riesgo_intercepción + (CO₂ × λ)      con λ = 2.0
```

### Heurística
```
h(n) = (4 − zona(n)) × RIESGO_MIN_POR_PASE          con RIESGO_MIN_POR_PASE = 2
```
Lectura futbolística: *"en el mejor caso imaginable, cada pase que aún falta saldría tan limpio
como el mejor pase que este equipo sabe dar."* Es una **relajación** → admisible y consistente
(demostrado con Dijkstra invertido en el notebook de la guía 4).

### Parámetros operativos elegidos
| Parámetro | Valor | Por qué |
|---|---|---|
| `w` (Weighted A\*) | **1.5** en vivo, **1.2** si se quiere óptimo, **1.0** en análisis post-partido | Calibrado sobre los 10 orígenes posibles (Reto 4, guía 4) |
| `λ` (peso ecológico) | **2.0** | Penaliza centros al área y pases largos de banda |
| `INICIO / OBJETIVO` | `POR` / `DL` | |

### Resultados canónicos del Dominio A (citarlos, no recalcularlos a ojo)

| Escenario | Jugada óptima | Riesgo `C*` |
|---|---|---|
| Partido normal | `POR → DFI → MC1 → MO → DL` | **9** |
| Marca personal sobre MO | `POR → LTI → EXI → DL` | **14** |
| MO fuera del campo | `POR → LTI → EXI → DL` | **14** |

**Las tres grandes conclusiones del proyecto hasta hoy:**
1. **Greedy cae en la trampa del extremo**: `EXI`/`EXD` tienen `h` bajísimo por estar pegados al
   área, pero su único pase al `DL` es un centro de riesgo 8–9. Greedy manda centrar ignorando que
   hay tres centrales esperando.
2. **La adaptabilidad viene de `g(n)`, no de `h(n)`.** En escenario dinámico, Greedy devuelve la
   misma jugada incluso cuando un jugador **desapareció del campo**. Un algoritmo puramente
   heurístico no es "rápido pero aproximado": es **inservible**.
3. **Marcar al mediapunta cuesta lo mismo que expulsarlo** (`C*` 9 → 14 en ambos casos).
   Lectura táctica: vale la pena gastar un jugador en esa marca.

---

## 5. Dominio B — Modelo técnico (guía 5, 6 y parcial)

### Función de utilidad (Min-Max) — todas las variables en escala 0–10
```
U = (Rendimiento × 4) − (CO₂ × 2·λ) − (Riesgo_lesión × 3) + (Recuperación × 2)
```
Pesos justificados: Catapult GPS/IMU (rendimiento), GHG Protocol adaptado (CO₂),
UEFA Medical Matters 2021 (riesgo de lesión), Kinexon HRV/sueño (recuperación).

### Árbol Min-Max
- **MAX** = cuerpo técnico / IA de rendimiento · **MIN** = riesgo fisiológico y CO₂ metabólico.
- Nivel 1 (MAX) **Carga**: Alta / Moderada · Nivel 2 (MIN) **Fatiga**: Alta / Baja ·
  Nivel 3 (MAX) **Uso del jugador**: Jugar / Descansar.

**Resultado canónico (verificado):**
| Nodo | Valor |
|---|---|
| Carga Alta (MIN) | −1 |
| Carga Moderada (MIN) | +19 |
| **Raíz (MAX)** | **+19 → Carga Moderada** |
| Rama elegida | `Carga Moderada → Fatiga Alta → Descansar` |
| Podas α-β | 2 hojas de 8 |

> **La frase del proyecto:** la mejor hoja del árbol vale **+42** (`Carga Mod. + Fat. Baja +
> Jugar`), pero Min-Max elige **+19**, porque MIN nunca concede fatiga baja. *La decisión no es la
> mejor posible: es la mejor garantizada.*

### Modelo STRIPS
- **S0:** atleta fatigado, carga alta, riesgo elevado, rendimiento bajo, **CO₂ acumulado alto**,
  partido en 5 días.
- **Meta:** recuperado, riesgo bajo, rendimiento alto, CO₂ bajo, listo para competir.
- **Plan (CO₂ total = 9):** Sesión Regenerativa (1) → Monitorear Biomarcadores (1) → Ajustar
  Nutrición (1) → Entrenamiento Específico (5) → Validar Estado (1).
- **El cerrojo:** `co2_acumulado(alto)` bloquea el entrenamiento específico hasta que
  `Monitorear_Biomarcadores` lo baja. Eso es lo que fuerza el orden del plan.

## 6. Modelo probabilístico (guía 6 y parcial)

Red bayesiana sobre el **Dominio B**, con las **mismas variables del árbol Min-Max**:
`C → F`, `C → E`, `F → E`

- **C** = Carga semanal (Alta 0.40 / Moderada 0.60) — es el Nivel 1 del árbol.
- **F** = Fatiga (Alta/Baja) — es el Nivel 2 (MIN) del árbol.
- **E** = Éxito competitivo (Éxito/Fallo).

| Consulta | Valor |
|---|---|
| `P(E=Éxito)` marginal | 57.8 % |
| `P(E=Éxito \| C=Moderada)` | 73.0 % |
| `P(E=Éxito \| C=Alta)` | 35.0 % |
| `P(E=Éxito \| F=Alta)` | 32.5 % |
| `P(E=Éxito \| F=Baja)` | 81.2 % |
| `P(F=Alta)` | 48.0 % |
| `P(C=Alta \| F=Alta)` | 62.5 % |

> **Por qué esta red y no otra:** en Min-Max, MIN es un adversario perfecto que siempre concede la
> peor fatiga. La red bayesiana le pone **probabilidad** a ese mismo nodo. **Min-Max da la decisión
> garantizada; Bayes da la decisión esperada; STRIPS es el plan para pasar de una a la otra.**

## 7. Postura ética del grupo (guía 2)

> **"La IA debe asistir las decisiones deportivas, nunca absorber la responsabilidad humana."**

- Nivel de control humano exigido: **human-in-command** para decisiones de alto riesgo.
- Principios citables: **No Discriminación** e **Inclusión** del *Marco Ético para la IA en
  Colombia* (2021); gobernanza del ciclo de vida del **CONPES 4144 de 2025**.
- Referentes del sector: **Olympic AI Agenda** del COI (2024) y el *Fujitsu Judging Support System*
  de gimnasia (París 2024) — la IA asiste, el juez humano firma.

Toda presentación del curso cierra con esta idea.

## 8. Estilo de los entregables

- **Notebooks** en español, con estructura: celda de modelo → celda de cálculo → **celda de lectura
  del resultado en lenguaje del sector**. Nunca dejar una tabla sin su interpretación futbolística.
- **Paleta gráfica fija:** `ROJO='#EE2A49'`, `AZUL='#3E4B5B'`, `CLARO='#D8D8D8'`,
  `FONDO='#EDEDED'`, `VERDE='#2ECC71'`.
- **Librerías:** `networkx`, `matplotlib`, `pandas`, `heapq`, `collections`. Sin dependencias nuevas.
- **Presentaciones:** se han hecho en **Gamma** (gamma.app).
- Todos los parámetros ajustables van en constantes al inicio, con una nota de "cambia esto y
  re-ejecuta y todo se recalcula solo" — le gusta al profesor y facilita la demo en vivo.

## 9. Estado del curso

| Guía | Tema | Estado |
|---|---|---|
| 1 | Ecosistema de IA en el sector | ✅ entregada |
| 2 | Ética y riesgos | ✅ entregada |
| 3 | Espacio de búsqueda, BFS/DFS/UCS | ✅ presentada (notebook incompleto en disco) |
| 4 | Heurísticas: Greedy, A\*, Weighted A\* | ✅ entregada — la mejor |
| 5 | Min-Max + α-β y STRIPS | ✅ entregada — Min-Max, α-β, STRIPS forward/backward y grafo espejo. **Base del parcial** |
| 6 | Redes bayesianas | 🔴 pendiente — hay `planeacion.md` |
| Parcial 1 | Agente integrador (los 3 métodos) | 🔴 pendiente — **entrega jueves 17 sep 2026** — hay `planeacion.md` con cronograma |
