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
🔴 **No desarrollado.** Carpeta `entregables/` vacía.
👉 Ver `planeacion.md` en esta misma carpeta (versión 2, con cronograma de 3 días).

## Punto de partida real
La **guía 5 ya está completa** (`Algoritmo_Rendimiento_deportivo.ipynb`): tiene Min-Max con poda
α-β y STRIPS forward/backward con detección de bloqueos, en el dominio de **gestión de carga del
atleta**. Eso es aproximadamente el **60 % del código del parcial**.

**Lo que falta construir:**
1. El módulo **bayesiano** (que además cierra la guía 6).
2. El **agente integrador** y su `agent_log.txt`.
3. Los **4 PNG con nombres exactos** y el README.
4. Generalizar el árbol Min-Max a **profundidades {2,3,4}** y **3 escenarios** (hoy es un
   diccionario fijo de profundidad 3).
5. Añadir **A\*** como motor de la búsqueda STRIPS (requisito explícito del profesor en la guía 5).

**Deuda técnica heredada de la guía 5** (detallada en `../guia 5/contexto.md`): `ruta_optima` guarda
un solo nodo en vez de la rama completa, el conteo de nodos podados es aproximado, y
`busqueda_forward` devuelve un número variable de elementos. Todo eso hay que arreglarlo porque el
parcial **califica exactamente esas cosas** (rama resaltada, nodos expandidos medidos).
