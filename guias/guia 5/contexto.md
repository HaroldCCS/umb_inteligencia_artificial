# Contexto — Guía 5: Min-Max + poda α-β y Planificación STRIPS

> ✅ **Guía completa.** Es la base directa del parcial práctico 1.
> ⚠️ **Ojo:** esta guía introduce un **segundo dominio** distinto al de las guías 3 y 4.

## Qué pide el profesor

**Actividad 1 — Min-Max:**
1. Definir **MAX** y **MIN** en el sector.
2. Árbol de decisión de **2–3 niveles**.
3. **Función de utilidad con indicadores reales** del sector (no +10/−10 arbitrarios).
   Ejemplo dado: `Utilidad = (Apoyo local × 5) − (Huella CO₂ × 2) − (Residuos × 1)`.

**Actividad 2 — STRIPS:**
1. **Plan maestro** en dos direcciones: **Fase A forward** (justificando precondiciones paso a paso)
   y **Fase B backward / regresión de metas** (desde la meta, buscar la acción cuyo **ADD** la cumple
   y convertir sus precondiciones en sub-metas).
2. **Detección de bloqueos:** ¿alguna acción forward hace **DELETE** de algo que backward marcó como
   necesario? (→ **Anomalía de Sussman**). ¿Hay **acciones huérfanas**?
3. **Grafo espejo:** nodos = estados, aristas = acciones, flechas azules = forward, rojas = backward.

(El profesor aclara: **no buscar los links en internet, los PDF están en `recursos/`**.)

## Finalidad dentro del curso
Es la guía **bisagra**: construye dos de los tres métodos que el parcial exige integrar.
El código de esta guía es **~60 % del código del parcial**.

## Recursos (resumen para no releerlos)

### `PLANIFICACION-MAX MIN.md`
- **Min-Max:** árbol de juego; MAX maximiza, MIN minimiza. Nodo = estado, arista = jugada.
- **Poda α-β:** `α` = mejor valor asegurado para MAX; `β` = mejor asegurado para MIN;
  si `α ≥ β` se poda. Analogía de la camiseta de $50.000 vs la tienda que empieza en $100.000.
  Ejemplo trabajado: raíz A (MAX), hijos B y C (MIN), hojas D=3, E=5, F=2, G podado → resultado 3.
- **Cómo adaptarlo a cada sector:** (1) MAX vs MIN como fuerzas opuestas (salud: médico vs
  enfermedad; banca: banco vs riesgo de impago); (2) estados = nodos, acciones = aristas;
  (3) función de utilidad con métricas del sector; (4) apoyarse en indicadores oficiales
  (ONU, OMS, ISO, OECD, GSTC, GHG Protocol) o justificar los propios.
- **Función de utilidad** = calificación numérica que hace comparables las consecuencias.
  Sin utilidad el agente "se queda ciego".
- Cierre: todo agente hace **Percibir → Evaluar → Decidir → Actuar**.

### `Planificación STRIPS.md`
- **STRIPS** = estados (conjuntos de predicados) + acciones (**precondiciones**, **ADD**, **DELETE**)
  + meta.
- **Axioma de persistencia:** solo cambia lo que está en ADD/DELETE. Resuelve el **Frame Problem**
  por simplificación; su límite es el **Ramification Problem**.
- **Forward State-Space Search** vs **Backward Chaining / Goal Regression**.
  **Test para elegir:** ¿pocas acciones aplicables al inicio? → forward. ¿pocas acciones logran la
  meta? → backward.
- **Anomalía de Sussman:** interferencia de metas — resolver la sub-meta 1 bloquea la sub-meta 2.
  Analogía: ponerse los zapatos antes que las medias.
- **PDDL:** separa **Dominio** (predicados + acciones) de **Problema** (objetos + inicial + meta).
- **Instrucción explícita (ACTIVIDAD 2):** *"no van a dejar que el agente elija acciones al azar.
  Van a implementar el algoritmo de búsqueda que identificaron como el más eficiente (ej. A\*)"*,
  usando las acciones STRIPS como generador de sucesores y devolviendo el **Plan** como lista
  ordenada de pasos.
- Estructura de código sugerida: clase `Accion(nombre, precondiciones, add, delete)`,
  `aplicar_accion(estado, accion)` con `(estado − delete) | add`.

## Qué entregamos (`entregables/Algoritmo_Rendimiento_deportivo.ipynb`)

**17 celdas, dos capas.** ⚠️ **El dominio cambió:** ya no es la red de pases de las guías 3–4,
sino la **gestión de carga y preparación del atleta** antes del partido.

### Capa 1 — Min-Max + α-β
- **MAX** = cuerpo técnico / IA de rendimiento. **MIN** = riesgo fisiológico y huella de carbono
  metabólica, que reducen la disponibilidad del atleta.
- **Función de utilidad** (todas las variables en escala 0–10):
  ```
  U = (Rendimiento × 4) − (CO₂ × 2) − (Riesgo_lesión × 3) + (Recuperación × 2)
  ```
  Pesos justificados en una tabla: Catapult GPS/IMU (rendimiento), GHG Protocol adaptado (CO₂),
  UEFA Medical Matters 2021 (riesgo de lesión), Kinexon HRV/sueño (recuperación).
- **Árbol de 3 niveles:**
  - Nivel 1 (MAX): **Carga de entrenamiento** → Alta / Moderada
  - Nivel 2 (MIN): **Fatiga** con que responde el organismo → Alta / Baja
  - Nivel 3 (MAX): **Uso del jugador** → Jugar / Descansar
- **Valores de las hojas (recalculados y verificados):**

| Hoja | Rend | CO₂ | Riesgo | Recup | **U** |
|---|---|---|---|---|---|
| Carga Alta + Fat. Alta + Jugar | 3 | 8 | 9 | 2 | **−27** |
| Carga Alta + Fat. Alta + Descansar | 2 | 4 | 5 | 7 | **−1** |
| Carga Alta + Fat. Baja + Jugar | 7 | 7 | 6 | 4 | **+4** |
| Carga Alta + Fat. Baja + Descansar | 5 | 3 | 3 | 8 | **+21** |
| Carga Mod. + Fat. Alta + Jugar | 6 | 5 | 5 | 5 | **+9** |
| Carga Mod. + Fat. Alta + Descansar | 4 | 2 | 3 | 8 | **+19** |
| Carga Mod. + Fat. Baja + Jugar | 9 | 3 | 2 | 9 | **+42** |
| Carga Mod. + Fat. Baja + Descansar | 7 | 1 | 1 | 9 | **+41** |

- **Resultado Min-Max verificado a mano:**
  `Carga_Alta (MIN) = min(−1, 21) = −1` · `Carga_Moderada (MIN) = min(19, 42) = 19`
  → **Raíz (MAX) = 19 → Carga Moderada**, y dentro de ella la rama que MIN concede es
  **Fatiga Alta → Descansar (+19)**.
- **La lección clave de esta guía:** la mejor hoja del árbol es `Carga Mod. + Fat. Baja + Jugar`
  con **+42**, pero **Min-Max no la elige** porque MIN (el organismo) nunca concede fatiga baja
  después de una carga. El agente se queda con **+19** garantizado. *La decisión no es la mejor
  posible: es la mejor garantizada.*
- **Poda α-β:** funciona, se podan 2 hojas de 8 (`CA_FB_Desc` y `CM_FB_Desc`); se evalúan 6.
- **Experimento λ:** al variar el peso del CO₂, la mejor hoja cambia de
  `Carga Mod. + Fat. Baja + **Jugar**` (λ ≤ 1) a `... + **Descansar**` (λ ≥ 1.5).
  El punto de quiebre está en **λ ≈ 1.5**.

### Capa 2 — STRIPS
- **Pregunta:** *"¿Qué secuencia de acciones lleva al atleta de fatiga elevada a estar listo para
  competir, minimizando la huella de carbono metabólica acumulada?"*
- **Estado inicial S0:** `atleta(fatigado)`, `carga_semanal(alta)`, `riesgo_lesion(elevado)`,
  `rendimiento(bajo)`, `co2_acumulado(alto)`, `partido_en(5_dias)`.
- **Meta G:** `atleta(recuperado)`, `riesgo_lesion(bajo)`, `rendimiento(alto)`,
  `co2_acumulado(bajo)`, `listo_para_competir`.
- **5 acciones** con `co2_costo` (escala 1–5):

| Acción | Pre | ADD | DELETE | CO₂ |
|---|---|---|---|---|
| `Aplicar_Sesion_Regenerativa` | fatigado, carga alta | en_recuperacion, carga moderada | fatigado, carga alta | 1 |
| `Monitorear_Biomarcadores` | en_recuperacion | datos_fisiologicos, **co2(bajo)** | co2(alto) | 1 |
| `Ajustar_Plan_Nutricional` | datos_fisiologicos, co2(bajo) | nutricion(optimizada), recuperado | en_recuperacion | 1 |
| `Ejecutar_Entrenamiento_Especifico` | recuperado, nutricion, **co2(bajo)** | rendimiento(alto), riesgo(bajo), carga(optima) | rendimiento(bajo), riesgo(elevado), carga(moderada) | **5** |
| `Validar_Estado_Competitivo` | rendimiento(alto)… | listo_para_competir | — | 1 |

- **El "cerrojo" del plan:** `co2_acumulado(alto)` **bloquea** el entrenamiento específico (CO₂ = 5)
  hasta que `Monitorear_Biomarcadores` lo baja. Es lo que fuerza el orden del plan y lo que
  convierte la huella de carbono en una **precondición lógica**, no en un adorno.
- Se implementan **búsqueda forward**, **búsqueda backward (goal regression)**, **detección de
  interferencias / acciones huérfanas / anomalía de Sussman** y el **grafo espejo**
  (forward azul arriba, backward rojo abajo).

## Estado
✅ **Completa.** Min-Max + α-β ✓, STRIPS forward + backward ✓, detección de bloqueos ✓,
grafo espejo ✓, función de utilidad con métricas reales ✓.

## ⚠️ Cosas a corregir antes de reutilizar este código en el parcial

1. **`ruta_optima` guarda un solo nodo, no la rama completa.** En la celda 5 solo se asigna en el
   nodo `"Inicio"` como `ruta_actual + [mejor_hijo]`, así que el resumen imprime únicamente
   `Carga_Moderada`. El parcial exige **resaltar la rama escogida completa** → hay que propagar el
   mejor hijo recursivamente hacia arriba.
2. **El conteo de nodos podados es aproximado.** `nodos_podados` solo agrega hermanos directos y no
   los subárboles completos; además `nodos_evaluados` solo registra hojas. El parcial pide
   **nodos expandidos** como métrica medida → hace falta un contador global que incremente en
   *cada* llamada a `minimax`.
3. **Comentarios de valores desactualizados.** En la celda 4 los comentarios dicen `-29, -3, +6,
   +36, +37`; los valores reales son `−27, −1, +4, +42, +41`. Corregir antes de proyectar en clase.
4. **`busqueda_forward` devuelve 4 elementos si falla y 5 si tiene éxito** → el desempaquetado
   revienta cuando no encuentra plan. Devolver siempre 5.
5. **La conclusión del experimento λ mezcla dos cosas:** dice "consolidando la decisión Carga
   Moderada + Fatiga Baja + Descansar", pero eso es la **mejor hoja**, no la **decisión Min-Max**
   (MIN nunca concede fatiga baja). Precisar la redacción: λ cambia la mejor hoja; la decisión
   garantizada sigue siendo `Carga Moderada → Fatiga Alta → Descansar`.

## Relación con las guías 3 y 4 — importante
El proyecto tiene ahora **dos dominios**:
- **Dominio A — red de pases** (guías 3 y 4): la jugada de salida POR→DL, riesgo de intercepción,
  A\*/Weighted A\*.
- **Dominio B — gestión de carga del atleta** (esta guía): fatiga, recuperación, riesgo de lesión,
  CO₂ metabólico, Min-Max y STRIPS.

Ambos son el mismo sector y comparten la métrica de **CO₂ metabólico (GPS/IMU)**, que es el puente.
**El parcial se construye sobre el Dominio B**, porque es donde ya viven Min-Max y STRIPS.
Ver `../parcial practico 1/planeacion.md`.
