ALGORITMOS BUSQUEDA

## ¿Qué es un agente de IA?

Un agente de IA es un "programa inteligente" que percibe un entorno (recibe información) y actúa en él (toma decisiones). Ejemplo: un agente turístico que recibe datos de gustos, tiempo y presupuesto de un viajero, y propone un itinerario.

# Dos formas de ver un agente IA

- Un agente es simplemente:

Algo que percibe su entorno, razona y actúa para cumplir objetivos.

- Dentro de esa definición caben dos enfoques:

- IA clásica (simbólica)

- El agente tiene un modelo del entorno (grafo, reglas, estados).

- Usa algoritmos de búsqueda o planificación (Greedy, A*, etc.) para decidir la acción.

- Ejemplo: un robot aspiradora planeando el camino óptimo para limpiar un cuarto.

- IA moderna (aprendizaje profundo / LLMs)

- El agente no tiene un modelo explícito, sino que usa una red neuronal entrenada con datos masivos.

- Razona o genera respuestas prediciendo la salida más probable.

- Ejemplo: un asistente de voz que responde preguntas o da instrucciones.

- Ambos son agentes, solo que usan mecanismos distintos de decisión.

Cuando hablamos de agentes de IA, podemos tener agentes clásicos que piensan en grafos y reglas, o agentes modernos que piensan en probabilidades y datos. Ambos son agentes, pero con cerebros diferentes. Hoy en la industria incluso se combinan: un LLM entiende la orden, y un planificador clásico decide cómo cumplirla.

# Ejemplo para un proyecto

Un agente explorador en un laberinto:

- Clásico: usa Algoritmos para encontrar la ruta más corta a la salida.

- LLM (API): recibe la instrucción en lenguaje natural (“quiero ir por el camino más seguro, no

el más corto”).

- Híbrido: el LLM traduce esa orden en un criterio, y el planificador clásico la ejecuta en el grafo.

Evolución de los agentes IA:

- primero razonaban con reglas y grafos (Algoritmos),

- hoy razonan con redes neuronales gigantes (LLMs),

- y lo más avanzado es combinarlos en agentes

híbridos.

# ¿Hay relación entre ambos mundos?

- Planificación + LLMs

- Un LLM puede generar un plan en lenguaje natural (“los pasos para cocinar algo”), pero la ejecución precisa

de ese plan en un robot puede requerir algoritmos clásicos de búsqueda.

- Ejemplo: un robot con un LLM “entiende la instrucción del humano” y luego usa Algoritmo para caminar

físicamente hasta la cocina.

- Razonamiento simbólico + LLMs

- Se está investigando cómo combinar heurísticas y búsqueda con LLMs para que razonen mejor (ej. Tree of

Thoughts, Monte Carlo Tree Search con LLMs).

- Aquí los LLMs generan posibles pasos, y la búsqueda clásica evalúa qué camino es más prometedor.

- Inspiración conceptual

- Los algoritmos de búsqueda enseñan cómo un agente decide qué acción tomar.

- Los LLMs, aunque no usen A*, siguen siendo agentes: toman decisiones (qué token predecir, qué acción

ejecutar en un entorno).

- Muchos papers recientes hablan de “LLM agents” que se comportan como agentes clásicos, pero con un

cerebro neuronal en vez de reglas fijas.

- Los algoritmos como A = IA clásica, simbólica, basada

en reglas y heurísticas.*

- Los LLMs = IA moderna, estadística, basada en datos y

aprendizaje profundo.

- Hoy en día se integran:

- El LLM interpreta instrucciones → parte “cognitiva”.

- Algoritmos de búsqueda heurística ejecutan el plan → parte

“operativa”.

Entonces sí hay relación conceptual, entender la IA clásica es clave para comprender cómo diseñar agentes híbridos modernos.

# Tipos de Agente

Reflex (simple)

Basado en Modelo

Basado en Metas (Goalbased) Basado en Utilidad

Agente de Aprendizaje (Learning)

Reflex (Simple): Un agente de reflejo simple actúa únicamente en función de la percepción actual del entorno, sin considerar el historial o estados futuros. Toma decisiones basadas en reglas predefinidas del tipo "si-entonces" (ejemplo: si detecta un obstáculo, gira a la derecha). Es rápido, pero limitado, ya que no planifica ni aprende. Ejemplo: un robot aspirador que esquiva objetos.

Basado en Modelo: Este agente utiliza un modelo interno del entorno para tomar decisiones. Además de percibir el estado actual, mantiene un "modelo" de cómo funciona el mundo (estado previo o consecuencias de acciones). Esto le permite manejar situaciones donde la percepción actual no es suficiente. Ejemplo: un coche autónomo que estima la trayectoria de otros vehículos.

Basado en Metas (Goal-based): Este agente toma decisiones orientadas a alcanzar un objetivo específico. Considera el estado actual, el modelo del entorno y evalúa posibles acciones para acercarse a la meta. Usa planificación para determinar la mejor secuencia de acciones. Ejemplo: un sistema de navegación GPS que calcula la ruta más corta.

Basado en Utilidad: Va un paso más allá del agente basado en metas. No solo busca alcanzar un objetivo, sino que evalúa las acciones según una función de utilidad que mide qué tan "deseable" es un resultado. Esto permite elegir entre múltiples opciones considerando preferencias o costos. Ejemplo: un sistema de recomendación que elige películas según preferencias del usuario.

Agente de Aprendizaje (Learning):

Este agente mejora su desempeño con el tiempo al aprender de la experiencia. Utiliza algoritmos de aprendizaje (como refuerzo o supervisado) para ajustar sus acciones basándose en retroalimentación del entorno. Es adaptable a entornos cambiantes o desconocidos. Ejemplo: un agente de juego que mejora su estrategia tras múltiples partidas.

# Tipos de búsqueda en IA

### No informada (o ciega):

No usa conocimiento adicional del problema, solo explora. BFS, DFS, UCS entran aquí.

### Informada (o heurística):

Usa funciones heurísticas (A*, Greedy, etc.).

- En IA clásica, un agente se ve

como "percibir → decidir → actuar". Los algoritmos de búsqueda se aplican en la fase de decisión, donde el agente evalúa el espacio de estados y selecciona el mejor camino según:

- Costo (tiempo, esfuerzo,

distancia).

- Necesidad de optimalidad.

- Limitaciones de tiempo/memoria.

## ¿Qué tiene que ver la búsqueda con los agentes?

- Cuando un agente debe tomar decisiones, muchas veces se enfrenta a un

espacio de posibilidades.

- Puede ser un mapa de rutas.

- Puede ser una lista de actividades turísticas.

- Puede ser un tablero de ajedrez.

- Ese espacio de posibilidades se representa como un árbol o grafo de opciones.

- Y aquí entran los algoritmos de búsqueda: sirven para explorar ese espacio y

encontrar la mejor opción según lo que queremos.

## Tipos de Agentes de IA y relación con BFS, DFS y UCS

- Agentes Reflexivos Simples (Reflex/Rule-based agents)

- Agentes Basados en Modelo (Model-based agents)

- Agentes Basados en Metas (Goal-based agents)

- Agentes Basados en Utilidad (Utility-based agents)

- Agentes de Aprendizaje (Learning agents)

Relación General

- BFS / DFS: encajan en agentes basados en modelo y metas, porque exploran

el espacio de estados hasta encontrar un itinerario válido.

- UCS: encaja más con goal-based y utility-based, porque considera el costo

total.

- Aprendizaje automático: va más allá de estos algoritmos, corresponde a

learning agents.

Agente reactivo simple (Reflex Agent)

Qué hace: Actúa según la situación inmediata (condición → acción). No planifica.

Ejemplo turismo: El agente recomienda la primera actividad disponible que cumpla una regla simple ("si el turista quiere playa → recomendar playa").

Agente reactivo basado en modelo (Model-based Reflex Agent)

Qué hace: Tiene un modelo del entorno para recordar qué actividades ya probó o qué restricciones existen (ej. presupuesto usado).

Ejemplo turismo: Si ya gastó $50 en comida, el agente evita recomendar otra cena costosa.

Agente basado en objetivos (Goal-based Agent)

Qué hace: Decide acciones con base en un objetivo definido (ej. "itinerario completo de 8 horas que incluya naturaleza").

Ejemplo turismo: El agente busca itinerarios que cumplan con todos los objetivos del turista (tiempo, gustos, actividades).

Agente basado en utilidad (Utility-based Agent)

Qué hace: No solo alcanza objetivos, sino que evalúa qué tan buenos son (optimización).

Ejemplo turismo: El agente pondera factores como satisfacción del turista, costo, tiempo libre, descanso, etc.

Puede que haya dos itinerarios válidos, pero elige el que maximiza la utilidad global.

Ejemplo turismo: Si el turista rechaza constantemente "museos", el agente aprende a no ofrecerlos más.

Qué hace: Mejora con la experiencia, ajustando recomendaciones en base al feedback del turista.

Agente que aprende (Learning Agent)

# Qué es un grafo

Un grafo es una estructura compuesta por:

- Vértices (nodos) → representan entidades.

Ej: ciudades, puntos turísticos, hoteles, museos.

- Aristas (edges) → representan relaciones o

conexiones. Ej: una carretera, una ruta de tren, un sendero.

- Ejemplo en turismo

Nodos: Bogotá, Medellín, Cartagena Aristas: Vuelo Bogotá–Medellín, Carretera Medellín–Cartagena

https://www.youtube.com/watch?v=_A9EpjnmZz4

# Tipos de

# grafos

Dirigidos: las conexiones tienen dirección (A → B ≠ B → A). Ej: rutas de buses que solo van en un sentido.

No dirigidos: las conexiones funcionan en ambos sentidos. Ej: carreteras de doble vía.

Ponderados: cada arista tiene un valor (peso). Ej: distancia en km, costo del boleto, tiempo de viaje.

No ponderados: todas las conexiones se consideran iguales.

# Representación de grafos

Para programación, se usan principalmente: a) Matriz de adyacencia

b) Lista de adyacencia

# Conceptos

# clave

Camino: secuencia de aristas que conecta nodos.

Costo: suma de los pesos del camino.

Vecinos: nodos conectados directamente.

Nodo visitado: un nodo ya explorado para evitar ciclos.

Grafo conexo: cualquier nodo se puede alcanzar desde otro.

### Tipos de búsqueda en IA

No informada (o ciega):

- No usa conocimiento

adicional del problema, solo explora.

- BFS, DFS, UCS entran

aquí.

Informada (o heurística):

- Usa funciones

heurísticas (A*, Greedy, etc.).

## Algoritmos de

## Búsqueda

## Heurística en

## Agentes de IA

Cuando hablamos de agentes inteligentes que resuelven problemas, necesitamos algoritmos de búsqueda en grafos o árboles de estados. Aquí entran los algoritmos que usan heurísticas: una estimación de qué tan cerca estamos de la meta.

- Greedy Best-First Search (GBFS)

- A* (A estrella)

- RBFS (Recursive Best-First Search)

# Criterios

# para

# comparar

# algoritmos

# de búsqueda

Criterio Qué significa Por qué importa

Completitud ¿Siempre encontrará una solución si existe?

Si el problema debe resolverse sí o sí, un algoritmo incompleto no es opción. Ej: búsqueda de rutas en un sistema de emergencia.

Optimalidad ¿La solución es la mejor posible (menor costo o menos pasos)?

En problemas de logística o costos, una solución “subóptima” puede ser más cara o lenta.

Complejidad en tiempo

Cuántos nodos expande antes de encontrar la meta.

Si el tiempo de respuesta es crítico (juegos, operaciones quirúrgicas robotizadas), importa mucho.

Complejidad en memoria Cuánta memoria consume para almacenar nodos.

En sistemas con recursos limitados (IoT, microcontroladores) no se puede usar algo que gaste demasiada memoria.

En la IA clásica, antes de que existiera el boom del aprendizaje automático, resolver problemas se trataba de buscar soluciones en un espacio de estados. Ese “espacio de estados” es como un mapa de todas las posibilidades para llegar de un punto inicial a una meta. Los algoritmos de búsqueda son las “estrategias” que usamos para movernos en ese mapa.

Ejemplos de problemas:

Encontrar la ruta más corta en un mapa.

Resolver un rompecabezas como el 8-puzzle.

Planificar pasos para que un robot complete una tarea.

- En el mundo de la inteligencia artificial

(IA), los algoritmos de búsqueda son herramientas fundamentales para la resolución de problemas. Entre la vasta gama de opciones, los algoritmos de búsqueda Breadth-First Search (BFS) y Depth-First Search (DFS) destacan por su simplicidad y aplicabilidad.

# BFS – Búsqueda en Anchura (Breadth-First Search)

Idea: Explorar nivel por nivel.

- Empiezas en el nodo inicial, visitas todos los vecinos, luego los vecinos de esos

vecinos, y así sucesivamente.

Ventajas:

- Encuentra la solución más corta (en pasos) si todos los costos son iguales.

Desventajas:

- Consume mucha memoria si el árbol es grande.

Ejemplo: Si buscas un amigo en una red social, revisas primero tus amigos directos, luego los amigos de tus amigos, y así.

## Búsqueda en Amplitud

## (BFS – Breadth-First

## Search)

¿Cómo funciona?

- Imagina que estás en un laberinto y decides explorar

todas las salidas cercanas primero, antes de ir más lejos.

- Empiezas por el nodo inicial.

- Luego miras todos sus hijos (nivel 1).

- Luego los nietos (nivel 2).

- Y así sucesivamente…

¿Qué estructura usa?

- Una cola (queue): el primero en entrar es el primero en

salir (FIFO).

¿Cuándo es útil?

- Cuando necesitas la solución más corta (menos pasos).

- Cuando todos los movimientos tienen el mismo costo.

Búsqueda en Amplitud (BFS – Breadth-First Search)

Pros Contras

Encuentra la solución más corta Usa mucha memoria si hay muchos caminos

Sencillo de entender Puede tardar mucho en problemas grandes

DFS – Búsqueda en Profundidad (Depth-First Search)

Idea: Explorar una rama hasta el final antes de retroceder.

- Va profundo, y si no encuentra la meta, retrocede y prueba

otro camino.

Ventajas:

- Usa menos memoria.

- Bueno si la solución está muy profunda.

Desventajas:

- Puede perder tiempo en caminos sin salida o muy

largos.

- Ejemplo: Buscar un archivo en carpetas anidadas: entras

en una carpeta y sigues bajando hasta que no haya más, luego retrocedes.

UCS – Búsqueda de Costo Uniforme (Uniform Cost Search)

Idea: Siempre expande el nodo con menor costo acumulado desde el inicio.

- Funciona como Dijkstra.

Ventajas:

- Encuentra el camino más barato incluso si los

costos son diferentes.

Desventajas:

- Puede ser más lento si hay muchos caminos

posibles.

- Ejemplo: En Google Maps, cuando buscas la ruta

más barata en tiempo o distancia, no necesariamente la más corta en pasos.

# Cómo se comparan BFS, DFS y UCS

Algoritmo Completitud Optimalidad Tiempo Memoria

BFS

(si espacio de estados es finito y con detección de ciclos)

(si costo uniforme) Exponencial en profundidad Alta (guarda todos los nodos del nivel)

DFS

(en grafos finitos con detección de ciclos), ✘ en infinitos

✘ (no siempre el camino más corto) Exponencial en profundidad Baja (guarda solo el camino actual)

UCS (si costos positivos) (encuentra el mínimo costo) Exponencial en peor caso

Alta (cola de prioridad con nodos visitados)

# Relevancia en la IA clásica

Estos algoritmos son fundamentales porque:

- Base de la búsqueda heurística

- A* y otros algoritmos más avanzados son

extensiones de estos.

- Fundamentos de planificación

- Sirven para entender cómo explorar y representar

problemas.

- Aplicaciones prácticas

- Juegos (como ajedrez), navegación de robots,

análisis de grafos.

- Pensamiento sistemático

- Enseñan a estructurar problemas de forma que una

máquina pueda resolverlos.

## En resumen:

BFS = “Exploro todo parejo, y así encuentro lo más corto en pasos.”

DFS = “Me lanzo a fondo por un camino antes de probar otro.”

UCS = “Voy siempre por lo que me cueste menos hasta ahora.”

- BFS: iría de A a todos sus

vecinos (B, C), luego a los vecinos de esos, y así.

- DFS: seguiría un camino

completo (por ejemplo, A → B → D → G) antes de retroceder.

- UCS: expandiría siempre el

nodo con menor costo acumulado, lo que podría llevarlo a tomar rutas diferentes a BFS aunque pase por los mismos nodos.

- BFS (izquierda): explora por niveles, asegurando la menor cantidad de pasos

hasta la meta.

- DFS (centro): se lanza profundo por un camino antes de retroceder.

- UCS (derecha): elige siempre expandir el nodo con menor costo acumulado,

aunque eso implique un orden distinto al de BFS.

### Formulación de problemas y espacio de búsqueda

Modelar un problema real como un espacio de búsqueda, definiendo:

- Estado inicial

- Estado objetivo

- Acciones posibles

- Restricciones y costos

- Tipo de entorno (estático/dinámico, observable/no observable, etc.)

Escenario de ejemplo: Distribución de frutas desde un centro logístico a tiendas locales

1. Contexto:

Una empresa distribuye frutas desde un centro logístico a varias tiendas de barrio. Cada tienda necesita una combinación diferente de frutas, y el camión debe planificar su ruta para cumplir las entregas con el menor costo posible. Cada acción tiene un costo (distancia, gasolina, tiempo). Además, algunas frutas son perecederas y deben entregarse antes que otras.

# Problema como espacio de búsqueda:

Elemento Ejemplo para este escenario Estado inicial Camión en el centro logístico, sin entregas realizadas Estado objetivo Todas las tiendas han recibido sus frutas correspondientes Estados intermedios Camión ha visitado ciertas tiendas, con carga parcial Acciones "Ir a tienda A", "Entregar frutas", "Volver al centro", etc. Restricciones Capacidad del camión, frutas perecederas, horario de tiendas Costo Distancia recorrida, tiempo consumido Tipo de entorno Parcialmente observable, dinámico si cambian condiciones

## Actividad práctica de la semana – parte1

Cada grupo construye un modelo de su problema como espacio de búsqueda.

- Paso 1: Describen el contexto de su problema (por sector)

- Paso 2: Definen los elementos del espacio de búsqueda

- Paso 3: Representan al menos cinco estados y transiciones (puede ser en

diagrama o tabla)

- Paso 4: Representar búsqueda en árbol o en grafo

# Ejemplo :

Elemento Descripción

Estado inicial Camión en bodega central con frutas A, B, C

Estado objetivo Tiendas T1, T2 y T3 han recibido sus pedidos

Acciones Ir a tienda T1, Entregar A y B, Ir a T2, Entregar C, etc.

Restricciones Solo puede llevar 3 tipos de fruta, T1 cierra a las 3 pm

Costos 10 km hasta T1, 7 km hasta T2, 5 km hasta T3

Representación Grafo con nodos (estado) y aristas (acciones)

## Ejemplos de

## aplicación de

## búsqueda

Búsqueda en amplitud (BFS) Encuentra todas las combinaciones posibles de itinerarios desde el más corto hasta el más largo, útil para proponer varias opciones iniciales.

Búsqueda en profundidad (DFS) Explora una posible secuencia de actividades hasta completarla, y si no es óptima, retrocede y busca otra alternativa.

Búsqueda de costo uniforme (UCS) Prioriza itinerarios con menor costo total (transporte + entrada + comida) en vez de menor tiempo.

Paso 1: Contexto (sector turismo)

- Un agente de IA ayuda a un turista a armar el mejor itinerario del día

según sus intereses, tiempo máximo 300 min y presupuesto ≤ $60. El objetivo es alcanzar satisfacción ≥ 20 con actividades compatibles.

## Paso 2: Elementos del espacio de búsqueda

- Estado: itinerario parcial + métricas

estado = (lista_actividades, tiempo_acum, costo_acum, satisfacción_acum)

- Acciones: agregar una actividad disponible y no repetida (Museo, Tour

Gastronómico, Mercado, Show, Taller), sin violar tiempo/presupuesto.

- Modelo de transición: al agregar una actividad se suman tiempo y costo, y se

acumula satisfacción.

- Costo (para UCS): usamos tiempo en minutos como costo del paso.

- Prueba de meta: satisfacción ≥ 20 y tiempo ≤ 300, costo ≤ 60

# Paso 3: Representación de al menos 5 estados y

# transiciones

- Un grafo dirigido con los estados S0…S5 (nodos) y transiciones (aristas) con la acción y su costo

(+minutos).

- Una tabla de estados con Itinerario, Tiempo, Presupuesto, Satisfacción y si es Meta.

- Una tabla de transiciones con “De → A”, Acción y Costo tiempo.

:

- S0: ∅ (inicio)

- S1: [Museo]

- S2: [Gastronómico]

- S3: [Museo, Mercado]

- S4: [Gastronómico, Show]

- S5 (Meta): [Museo, Show, Mercado] → T=240m, $=45, S=21

## Paso 4: ¿Búsqueda en árbol o en grafo? (y por qué)

Elección: búsqueda en grafo.

- Distintos órdenes pueden representar el mismo conjunto de actividades (p. ej.,

[Museo, Mercado] y [Mercado, Museo]), lo que generaría estados duplicados si usamos solo árbol.

- Con grafo + conjunto de visitados (definiendo el estado por el conjunto de actividades

y recursos consumidos) evitamos recomputar combinaciones equivalentes y ciclos (no repetir actividades).

- Esto mejora tiempo y memoria respecto a un árbol puro en problemas combinatorios.

# Estados (itinerarios) y si cumplen meta

## •Criterios de

## meta:

## satisfacción ≥ 20,

## tiempo ≤ 300

## min, presupuesto

## ≤ $60.

Estado Itinerario Tiempo (m) Presupuesto ($) Satisfacción ¿Meta?

S0 ∅ 0 0 0 No

S1 Museo 90 20 7 No

S2 Gastronómico 120 35 9 No

S3 Museo / Mercado 150 20 13 No

S4 Gastronómico / Show 210 60 17 No

S5 Museo / Show / Mercado 240 45 21 Sí

# Transiciones (acciones) y costos

De A Acción Costo tiempo (+m)

S0 S1 Agregar Museo 90

S0 S2 Agregar Tour Gastronómico 120

S1 S3 Agregar Mercado 60

S2 S4 Agregar Show 90

S3 S5 Agregar Show 90

### ¿Qué algoritmo usar aquí?

- BFS: útil si todas las acciones “valen 1” y queremos el itinerario con

menos pasos (nº de actividades).

- DFS: para explorar rápidamente rutas largas de actividades (no

garantiza meta/óptimo).

- UCS: ideal aquí porque minimizamos tiempo total bajo restricciones;

encuentra la solución de menor costo (tiempo) que cumple meta.

### Orden de expansión — BFS

- BFS visita por niveles;

encontró S5 cuando exploró nodos de nivel 3.

Orden Nodo 1 S0 2 S1 3 S2 4 S3 5 S4 6 S5

### Orden de expansión — DFS (iterativo, determinístico)

- DFS siguiendo la rama

izquierda exploró en profundidad y llegó rápidamente a S5 por la ruta S0→S1→S3→S5.

Orden Nodo

1 S0

2 S1

3 S3

4 S5

## Orden de expansión — UCS (por costo acumulado =

## tiempo)

UCS expandió nodos en orden de tiempo acumulado y también llegó a S5 con costo 240 min. En este grafo pequeño las tres estrategias convergen al mismo camino, pero UCS garantiza optimalidad en costo, mientras que BFS garantiza optimalidad en número de pasos (si no hay pesos).

Paso Nodo Costo acumulado (min)

1 S0 0

2 S1 90

3 S2 120

4 S3 150

5 S4 210

6 S5 240

### Resultados de la simulación

- Meta encontrada por: BFS, DFS y

UCS → S5

- Camino encontrado (todos): S0 →

S1 → S3 → S5

- Costo (tiempo) del camino

S0→S1→S3→S5: 240 minutos (UCS confirma costo mínimo)

## Interpretación

- Aunque aquí BFS, DFS y UCS encontraron la misma

solución, las razones difieren:

- DFS la encontró rápido porque la rama correcta estaba cerca de la

primera explorada.

- BFS la encontró por niveles asegurando menor número de

acciones.

- UCS la encontró tras considerar tiempo acumulado; confirma que la

solución tiene costo mínimo (240 min).

## Interpretación

- En problemas reales (más nodos, costos distintos, ciclos, o

rutas alternativas), los resultados suelen divergir y la elección del algoritmo importa:

- Usa UCS/A* cuando el costo (tiempo/dinero) sea crítico.

- Usa BFS cuando quieras minimizar número de acciones y el grafo

sea no ponderado.

- Usa DFS para explorar soluciones completas o cuando la memoria

sea limitada (pero con cuidado).

# Ejemplo de

# caso aplicado:

# “Ruta turística

# óptima en una

# ciudad”

1. FORMULACIÓN DEL

PROBLEMA ESTADO INICIAL: PUNTO DE INICIO DEL TURISTA (HOTEL, AEROPUERTO).

ESTADOS INTERMEDIOS: LUGARES TURÍSTICOS.

ESTADO OBJETIVO: DESTINO FINAL O COMPLETAR LA VISITA DE CIERTOS LUGARES.

ACCIONES: MOVERSE DE UN PUNTO TURÍSTICO A OTRO.

COSTO: PUEDE SER DISTANCIA, TIEMPO DE TRASLADO O PRECIO DE TRANSPORTE.

# Grafo de ejemplo

Supongamos una ciudad ficticia con estos puntos:

- Hotel - Plaza Central - Museo - Parque - Catedral - Mirador

Y las conexiones:

- Hotel Plaza Central (1 km)

- Plaza Central Museo (2 km)

- Plaza Central Catedral (3 km)

- Museo Parque (2 km)

- Catedral Mirador (4 km)

- Parque Mirador (3 km)

# Aplicación de los algoritmos

BFS (Breadth-First Search)

Encuentra la ruta con menor número de transiciones sin importar el costo real.

Ejemplo: Ideal si queremos minimizar cambios de transporte o “visitas” intermedias.

DFS (Depth-First Search)

Explora profundamente hasta llegar a un destino antes de retroceder.

Ejemplo: Útil si queremos encontrar rápidamente una ruta cualquiera aunque no sea la más corta.

UCS (Uniform Cost Search)

Expande siempre el camino con menor costo acumulado.

Ejemplo: Perfecto para encontrar la ruta turística más barata o rápida considerando distancias o tiempo real.

Librerías que ya implementan algoritmos de búsqueda

1. networkx

Una de las librerías más conocidas para trabajar con grafos.

Tiene funciones para BFS y DFS.

No incluye UCS directamente, pero se puede adaptar con Dijkstra (que es equivalente cuando no hay heurísticas).

- Importar la librería NetworkX y la referencia

como nx..

- Importar matplotlib.pyplot para

dibujar/visualizar el grafo; referenciado como plt.

- Importar PriorityQueue (cola de prioridad) de

la librería estándar queue. Se usa para UCS, Greedy y A*/priorización por costos/heurística.

- Importar el módulo time. Se usa time.sleep()

para pausar entre pasos y mostrar la visualización paso a paso.

Creación del grafo y posiciones Crea un grafo no dirigido llamado G. Graph() implica que cada arista es bidireccional.

Define una lista de aristas con pesos. Cada tupla (u, v, w) indica una arista entre u y v con peso w (por ejemplo, distancia o costo).

Añade todas las aristas edges al grafo G incluyendo el atributo 'weight' para cada arista.

Calcula una disposición (posicionamiento) de los nodos para dibujar el grafo usando el algoritmo spring layout (simula resortes). seed=42 fija la semilla aleatoria para que la disposición sea reproducible (mismo dibujo cada ejecución).

POSIBLES CASOS

1. Tutor inteligente para rutas de aprendizaje

personalizadas

- Algoritmo: BFS/DFS para explorar diferentes secuencias

de temas y UCS/A* para optimizar el tiempo total.

- Aplicación: El agente busca la mejor ruta para que un

estudiante aprenda un tema complejo (por ejemplo, matemáticas) pasando por lecciones previas necesarias.

- Ejemplo: Un alumno quiere aprender “derivadas” y el

agente encuentra la secuencia óptima: álgebra → funciones → límites → derivadas.

2. Búsqueda de recursos educativos más relevantes

- Algoritmo: Best-First Search (por relevancia).

- Aplicación: El agente examina un grafo donde los nodos

son recursos (artículos, videos, ejercicios) y busca los que más se ajusten al nivel y estilo de aprendizaje del estudiante.

- Ejemplo: Para un estudiante visual, prioriza recursos con

videos interactivos antes que texto plano.

3. Asistencia en resolución de problemas paso a paso

- Algoritmo: DFS para exploración profunda o

Bidirectional Search si hay estado final conocido.

- Aplicación: El agente ayuda al estudiante a resolver

problemas matemáticos o lógicos, buscando caminos de solución paso a paso.

- Ejemplo: Resolver un rompecabezas lógico buscando

todas las soluciones posibles antes de elegir la más corta.

## ¿Cómo se

## integra en el

## proyecto por

## sector?

Paso 1: Replantear el problema de su sector como espacio de búsqueda

Define el estado inicial y el estado objetivo en el contexto de tu sector.

Identifica qué representa un "nodo" y una "acción".

¿Cuál sería el "costo" en tu sector (tiempo, dinero, distancia, riesgo, etc.)?

# Escenario

- Un agente de IA ayuda a un turista a planificar actividades diarias según sus intereses, tiempo

disponible y presupuesto. El agente debe encontrar la mejor secuencia de actividades para cumplir con las preferencias del usuario.

- Estado inicial: Día vacío sin actividades.

- Acciones: Agregar una actividad turística disponible.

- Restricciones: Tiempo y presupuesto.

- Objetivo: Itinerario óptimo que maximice satisfacción y minimice costos o tiempos muertos.

# Ejemplos de

# aplicación de

# búsqueda

Búsqueda en amplitud (BFS) Encuentra todas las combinaciones posibles de itinerarios desde el más corto hasta el más largo, útil para proponer varias opciones iniciales.

Búsqueda en profundidad (DFS) Explora una posible secuencia de actividades hasta completarla, y si no es óptima, retrocede y busca otra alternativa.

Búsqueda de costo uniforme (UCS) Prioriza itinerarios con menor costo total (transporte + entrada + comida) en vez de menor tiempo.

Caso: Agente de IA para Planificación de Experiencias Turísticas

Objetivo: El agente busca armar el itinerario óptimo de un turista considerando gustos, presupuesto, tiempo disponible y disponibilidad de actividades. No es un problema de caminos físicos, sino de exploración de combinaciones de actividades.

1. Búsqueda en amplitud (BFS)

- Problema: Encontrar todas las combinaciones de

actividades posibles para un día, empezando por las más simples y aumentando la complejidad. Ejemplo: El agente genera primero itinerarios de 1 actividad, luego de 2, luego de 3, hasta encontrar uno que cumpla todas las restricciones del usuario. Uso real: Ideal para explorar muchas opciones sin priorizar, garantizando encontrar la más corta en cantidad de actividades.

Caso: Agente de IA para Planificación de Experiencias Turísticas

2. Búsqueda en profundidad (DFS)

- Problema: Explorar una secuencia completa

de actividades de manera rápida antes de retroceder. Ejemplo: El agente prueba primero un itinerario de 8 horas totalmente lleno, si no cumple criterios (ej. presupuesto o gustos), retrocede y prueba otra combinación. Uso real: Útil cuando queremos encontrar itinerarios largos y no nos preocupa tanto el costo computacional inicial.

Caso: Agente de IA para Planificación de Experiencias Turísticas

3. Búsqueda de costo uniforme (UCS)

- Problema: Encontrar el itinerario más

económico posible dentro de las preferencias. Ejemplo: El agente asigna un "costo" a cada actividad (entradas, transporte interno, comidas) y busca la combinación más barata que aún sea atractiva. Uso real: Muy útil para viajeros con presupuesto limitado.

En este árbol:

- Nodos = estados del itinerario

(combinaciones de actividades)

- Ramas = decisiones posibles (agregar

actividad compatible)

- Los algoritmos de búsqueda deciden

cómo recorrer este árbol.

Búsqueda en amplitud (BFS)

- Objetivo: encontrar la primera combinación de actividades que cumpla con las restricciones,

comenzando con itinerarios cortos y creciendo en tamaño.

- Cómo se hace:

- Representación del problema

- Cada nodo = un itinerario parcial (lista de actividades).

- Estado inicial = itinerario vacío.

- Operadores = añadir una nueva actividad disponible que no esté ya en el itinerario.

- Estado meta = itinerario que cumpla:

- Preferencias del usuario (gustos, horarios).

- Presupuesto ≤ límite.

- Duración ≤ tiempo disponible.

- Estructura de datos

- Cola (FIFO) para explorar primero los itinerarios más cortos.

BFS

### BFS

Camino encontrado BFS: ['Hotel', 'Museo', 'Restaurante']

# DFS

Camino encontrado DFS: ['Hotel', 'Playa', 'Parque', 'Restaurante']

# UCS

Camino encontrado UCS: ['Hotel', 'Museo', 'Parque', 'Restaurante'] Costo: 9

Sector Problema formulado como búsqueda Costos posibles

Salud Encontrar la ruta óptima para atender pacientes en casa Distancia, prioridad

Transporte Ruta más corta entre estaciones de bus Tiempo de viaje

Educación Ruta académica óptima para un estudiante Dificultad, créditos

Medioambiente Planificación de recolección de residuos en una ciudad Emisión CO₂, distancia

Finanzas Ruta más barata para distribuir dinero entre sucursales Tarifa, riesgo

# Tipos de Agentes de IA y relación con BFS, DFS y

# UCS

### Agentes Reflexivos Simples (Reflex/Rule-based agents)

- Qué hacen: reaccionan directamente a las condiciones del entorno con reglas predefinidas (ej. “si el

turista quiere playa y está libre, entonces sugiere Playa”).

- Relación con los algoritmos:

- No usan búsqueda compleja.

- Podrían usar algo muy básico como DFS truncado o una regla directa (“elige la primera opción válida”).

- Ejemplo en turismo: El agente siempre recomienda la primera actividad disponible sin considerar

combinaciones.

Agentes Basados en Modelo (Model-based agents)

- Qué hacen: mantienen un modelo interno del mundo (estado actual, restricciones de

tiempo/presupuesto).

- Relación con los algoritmos:

- Aquí encajan BFS y DFS, porque estos agentes exploran el espacio de estados (combinaciones de

itinerarios) manteniendo información de lo que ya se probó.

- Ejemplo en turismo: El agente construye itinerarios paso a paso, recordando qué

combinaciones ya intentó.

Agentes Basados en Metas (Goal-based agents)

- Qué hacen: buscan cumplir un objetivo definido (ej. “encontrar un itinerario válido que cumpla

todas las preferencias del usuario”).

- Relación con los algoritmos:

- BFS, DFS, UCS son estrategias típicas de agentes goal-based.

- UCS especialmente porque optimiza un criterio para llegar a la meta.

- Ejemplo en turismo: El agente busca cualquier combinación que cumpla con: “tiempo ≤ 6

horas y costo ≤ 30”.

Agentes Basados en Utilidad (Utility-based agents)

- Qué hacen: no solo alcanzan la meta, sino que optimizan qué tan buena es la solución

(maximizar satisfacción, minimizar costo-tiempo).

- Relación con los algoritmos:

- Aquí se relaciona UCS y también extensiones como A*, porque calculan rutas/planes según un costo o

utilidad.

- Ejemplo en turismo: El agente compara varias rutas posibles y elige la que maximice el

“placer” del usuario (ej. valor cultural + descanso – costo).

### Agentes de Aprendizaje (Learning agents)

- Qué hacen: mejoran su comportamiento con experiencia (aprenden qué itinerarios prefieren

diferentes turistas).

- Relación con los algoritmos:

- No se limitan a búsqueda estática como BFS/DFS/UCS.

- Usan machine learning (ej. reinforcement learning, recomendaciones basadas en histórico).

- Ejemplo en turismo: Con el tiempo, el agente aprende que turistas con bajo presupuesto suelen

preferir Playa + Comida local y adapta sus sugerencias.

Tipo de Agente Características Relación con Algoritmos Ejemplo en Turismo

Reflex (simple)

- Usa reglas “condición → acción” -

No considera historia ni modelo del mundo

No usa BFS/DFS/UCS, más bien decisiones directas o reglas estáticas

“Si hay sol → recomendar Playa”. “Si llueve → recomendar Museo”.

Basado en Modelo

- Mantiene un estado interno

(tiempo usado, dinero gastado, actividades ya elegidas) - Explora combinaciones posibles

BFS / DFS: prueban itinerarios posibles a partir de un modelo del entorno

Construye itinerarios paso a paso, recuerda qué ya intentó y retrocede si no cumple restricciones.

Basado en Metas (Goalbased)

- Tiene un objetivo claro (ej. cumplir

tiempo ≤ 6h y presupuesto ≤ 30) - Busca alcanzar un estado meta

BFS, DFS y UCS (dependiendo de si quiere la primera solución, una profunda o la más barata)

Busca cualquier itinerario que cumpla con las restricciones del turista.

Basado en Utilidad

- No solo cumple la meta, sino que

elige la “mejor” opción - Evalúa qué tan buena es una solución (satisfacción, costo, variedad)

UCS (Costo Uniforme) o algoritmos más avanzados como A*

Elige entre varias rutas posibles la que maximice la satisfacción (ej. cultural + relax) y minimice costo.

Agente de Aprendizaje (Learning)

- Aprende con experiencia

(retroalimentación de turistas previos) - Mejora su comportamiento con ML/RL

No limitado a BFS/DFS/UCS; usa machine learning (recomendación, RL)

Aprende que turistas con bajo presupuesto prefieren Playa + Comida local y adapta futuras recomendaciones.

ACTIVIDAD PARTE2

Cada grupo:

1. Modela el problema como grafo.

2. Aplica BFS, DFS y UCS.

3. Compara los caminos encontrados (en eficiencia,

costo, etc.).

4. Justifica cuál algoritmo es más útil en su caso.

Ejemplo: Grupo del sector transporte define estaciones como nodos, conexiones como aristas con tiempos de viaje, y compara rutas con BFS vs UCS.

TALLER