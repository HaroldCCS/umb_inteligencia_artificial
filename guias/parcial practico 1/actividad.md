Parcial Integrador – Inteligencia Artificial Clásica

Cada grupo debe aplicar Min-Max, STRIPS y Redes Bayesianas en su sector y entregar un agente

sencillo en Python que integre los tres métodos. Todas las visualizaciones listadas abajo son

obligatorias.

Entregables (obligatorios)

1. PRESENTACION (parte conceptual).

2. 3. 4. 5. Código Python ejecutable (script o notebook) con comentarios y un README que explique

cómo ejecutar.

Visualizaciones (archivos PNG) — nombres exactos requeridos:

o minmax_tree.png

o strips_graph.png

o bayes_bars.png

o agent_summary.png

Registro textual / log de ejecución (impreso en consola o archivo agent_log.txt) mostrando

el flujo del agente.

Breve demo en clase (5 minutos por grupo).

Es decir, todo suma 15 minutos por grupo aprox.

Requerimientos explícitos de visualización

Min-Max

• Dibujar el árbol de decisiones: todos los nodos y las hojas deben mostrar el valor

evaluado.

• Resaltar la rama escogida por el agente (por ejemplo, con color/anchura distinta).

• Debe quedar claro qué movimiento corresponde a cada rama (etiquetas en aristas o

nodos).

STRIPS

• Visualizar el grafo de estados (cada nodo = estado o proposición compuesta).

• Resaltar la ruta del plan encontrado (los estados/links que conforman el plan deben estar

destacados).

• Incluir leyenda que indique: estado inicial, metas, y plan.PARCIAL CORTE1 IA

Bayesiano

• Gráfico de barras con las probabilidades calculadas (por ejemplo: P(H1|evidencia),

P(H2|evidencia), ...).

• Eje y etiquetas claras; mostrar la evidencia usada (en texto dentro del gráfico o en el

filename/README).

Agente integrador

• Salida textual completa del flujo (ej. observe -> posterior -> plan -> decision -> acción)

guardada en agent_log.txt y mostrada en consola.

• Gráfica resumen (agent_summary.png) que combine en una sola figura:

1. El plan (representado como mini-grafo o lista visual) — extraído de STRIPS.

2. La probabilidad de éxito (resultado Bayesiano) — mini gráfico de barras o número

destacado.

3. La decisión final (resultado Min-Max) — mostrada visiblemente (texto grande o

anotación sobre la figura) y, si procede, la rama seleccionada superpuesta al plan.

Es decir: agent_summary.png debe ofrecer, a primera vista, la síntesis del agente: qué plan

propuso, qué probabilidad asignó al éxito y qué decisión final tomó.

Comparación de heurísticas y poda en Min-Max

Enunciado:

Comparen la versión “naive” de Min-Max (búsqueda completa hasta cierta profundidad) con:

1. Min-Max + poda α-β.

2. Min-Max + heurística de evaluación (su heurística diseñada).

Evalúen: tiempo de ejecución, nodos expandidos y consistencia de la decisión (mismo

movimiento o distinto) en varias profundidades y escenarios.

Tareas concretas:

• Implementar: (i) Min-Max básico; (ii) Min-Max + α-β; (iii) Min-Max + su heurística (y

opcionalmente + α-β).

• Ejecutar experimentos en 3 escenarios representativos del sector y profundidades {2,3,4}

(o lo que sea razonable computacionalmente).

• Registrar: tiempo, nodos_expandidos, decisión escogida.

• Si la decisión varía entre versiones, analizar si la heurística mejora o empeora resultadoPARCIAL CORTE1 IA

Análisis de sensibilidad Bayesiano

Partiendo del modelo bayesiano que ya construyeron, realicen un análisis de sensibilidad donde

varíen las probabilidades a priori (o parámetros clave de las CPT) y muestren el impacto en:

1. Posteriores para la(s) hipótesis clave.

2. Plan propuesto por STRIPS (si el umbral de posterior altera el objetivo).

3. Decisión final del agente (Min-Max), cuando aplique.

Tareas concretas:

• Seleccionar 4–6 valores distintos para el prior(s) relevante(es) (ej.: P(Severe) =

[0.01,0.05,0.1,0.2,0.4]).

• Para cada prior: calcular posterior(s) dado el mismo conjunto de evidencia; ejecutar el flujo

del agente (observe → plan → decide) y registrar resultados.

• Comparar resultados y discutir estabilidad/fragilidad de decisiones.