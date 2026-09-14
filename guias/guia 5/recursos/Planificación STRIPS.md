Búsqueda en juegos (Minimax + alfa-beta)

2. Planificación (STRIPS,

representación de conocimiento)

Redes bayesianas

# 2. Planificación

# (STRIPS y

# representación

# de

# conocimiento)

- La planificación automática responde: “¿Cómo alcanzar un

objetivo a partir de un estado inicial, usando un conjunto de acciones?”

- STRIPS (Stanford Research Institute Problem Solver) fue un

modelo pionero para representar problemas de planificación.

- Un estado: conjunto de condiciones (ejemplo: en(cocina),

limpio(mesa)).

- Una acción: tiene precondiciones (lo que debe cumplirse

para ejecutarla) y efectos (lo que cambia).

- Representación de conocimiento: usar lógica de primer orden

para describir estados, objetos y acciones. Ejemplo

- Problema: El robot está en la sala y quiere llevar un libro a la

biblioteca.

- Acción mover(robot, sala, biblioteca)

- Precondición: en(robot, sala)

- Efecto: ¬en(robot, sala), en(robot, biblioteca)

En la lógica formal clásica, si una acción cambia un aspecto del mundo (por ejemplo, el robot mueve una caja), no se asume automáticamente que el resto de las cosas permanecen iguales. Para un sistema lógico "puro", si el robot mueve la caja, habría que especificar explícitamente miles de axiomas de "no cambio":

- La mesa sigue siendo café.

- El cielo sigue siendo azul.

- La temperatura de la habitación no cambió.

- El libro sigue en el estante.

El problema es la explosión computacional: escribir y procesar todos los axiomas de lo que no sucede es imposible en entornos complejos.

### La Solución de

### STRIPS: El

### "Axioma de

### Persistencia"

STRIPS revolucionó la planificación al introducir una suposición de sentido común (llamada en inglés The STRIPS Assumption).

En lugar de listar lo que no cambia, STRIPS define que:

Solo cambia lo que está explícitamente en la lista de efectos (ADD y DELETE).

Todo lo demás se mantiene constante por defecto.

# Ejemplo:

- Acción: Pintar_Pared(Verde)

- Precondición: Tener_Pintura(Verde),

Pared_Limpia.

- Efectos:

- ADD: Pared_Color(Verde).

- DELETE: Pared_Color(Blanco).

- Bajo el modelo STRIPS, el sistema

"sabe" automáticamente que el robot sigue estando en la misma habitación y que el pincel sigue en su mano, sin que el programador tenga que escribirlo.

# Este punto es clave para entender la transición de

# la "Lógica Pura" a la "IA Práctica":

Eficiencia: Reduce drásticamente el tamaño de la base de conocimientos. El planificador solo procesa lo relevante.

Modularidad: Permite diseñar acciones de forma aislada. No necesitas saber qué otros objetos existen en el mundo para definir cómo funciona la acción Abrir_Puerta.

Limitaciones: Es importante mencionar que esta solución es una simplificación. En el mundo real, existen efectos secundarios (ramificaciones). Por ejemplo, si el robot mueve una mesa, los objetos que están encima de la mesa también se mueven, aunque no estén en la lista de efectos de la acción Mover_Mesa. (Esto se conoce como el Ramification Problem).

"¿Necesitamos decirle al robot que, tras mover la silla, el sol sigue brillando y su batería no se llenó mágicamente?" La respuesta es el Frame Problem, y STRIPS lo ignora elegantemente para poder funcionar.

### Punto de

### partida: ¿Qué

### es planificar?

“Si quiero preparar un sándwich, ¿qué pasos debo seguir y en qué orden?”

- Primero saco el pan

- Después pongo el

jamón

- Luego el queso

- Finalmente cierro el

sándwich

- Esa es la esencia de

la planificación: tener un objetivo y decidir la secuencia de pasos para alcanzarlo.

- "Al cerrar el sándwich

(Acción), el efecto es 'sándwich cerrado'. Gracias a STRIPS, no tenemos que especificar que la cocina no se quemó ni que el plato sigue siendo de cerámica; el sistema lo asume".

### El "Cómo" de la IA

Cuando hablamos de planificación en IA, la pregunta central es: “¿Qué acciones y en qué orden debo ejecutar para pasar de un estado inicial a un estado final deseado?”

En juegos (tema anterior) se trataba de elegir la mejor jugada.

En planificación, el objetivo cambia: armar un plan completo de pasos para lograr una meta.

STRIPS es como una lista de instrucciones de cocina para un robot. Le dice:

Qué necesita para poder hacer una acción (ingredientes/precondiciones)

Qué cambia después de hacerla (efectos: qué agregas y qué quitas)

Imagina un robot que quiere preparar café.

Estado inicial:

- en(cocina)

- taza(limpia)

- ¬tengo(cafe)

Objetivo:

- tengo(cafe_listo)

Acciones posibles:

- coger(taza)

- usar(cafetera)

La planificación consiste en decirle al robot qué acción va primero, luego cuál sigue, y así hasta lograr el objetivo.

# Analogía: El robot y la puerta

Imagina que tienes un robot frente a una puerta cerrada. Su objetivo es estar en la otra habitación.

Estado inicial:

- robot(frente_a_puerta)

- puerta(cerrada)

Objetivo:

- robot(dentro_habitacion)

Acciones disponibles:

- abrir_puerta

- Precondición:

puerta(cerrada)

- Efecto: puerta(abierta)

- entrar

- Precondición:

puerta(abierta) ∧ robot(frente_a_puerta)

- Efecto:

robot(dentro_habitacion)

El robot no puede entrar si no abre primero la puerta. Ese es el corazón de STRIPS: ordenar acciones porque unas dependen de otras.

STRIPS formaliza esas recetas con:

- Estados = foto del mundo actual

- Acciones = recetas con ingredientes y resultados

- Plan = secuencia de recetas para llegar al plato final

STRIPS (Stanford Research Institute Problem Solver) es un modelo de IA que responde a la pregunta: “¿Qué pasos y en qué orden debo ejecutar para ir de un estado inicial a un objetivo?” Diferencia con juegos (minimax):

- En juegos buscábamos qué jugada es la mejor.

- En planificación buscamos la secuencia de jugadas que me

llevan al objetivo.

# STRIPS

# describe los

# problemas de

# planificación

# con tres

# cosas:

Estados: Fotos del mundo en cierto momento (se describen con predicados). Ejemplo: en(robot, sala), puerta(cerrada)

Acciones: Cada acción tiene:

- Precondiciones: lo que debe cumplirse para ejecutar la

acción.

- Efectos: lo que cambia después (lista de cosas que se

agregan [ADD] y lista de cosas que se eliminan [DELETE]).

Ejemplo:

- Acción: mover(robot, sala, biblioteca)

- Precondición: en(robot, sala)

- Efectos:

- ADD → en(robot, biblioteca)

- DELETE → en(robot, sala)

Objetivo: El estado al que queremos llegar. Ejemplo: en(robot, biblioteca)

## Modelo

## STRIPS:

## Componentes

## Clave

El modelo STRIPS (Stanford Research Institute Problem Solver) describe los problemas de planificación usando tres elementos principales: a) Estados

- Representan el mundo en un momento dado.

- Se describen con predicados lógicos que son

verdaderos.

- Ejemplo:

- en(robot, sala)

- ¬en(robot, biblioteca)

- Piensa en ellos como fotografías de la realidad.

b) Acciones

- Cada acción es como una receta que permite cambiar de

un estado a otro. Tienen dos partes fundamentales:

- Precondiciones (qué debe cumplirse para que la acción

pueda ejecutarse).

- Ejemplo: para mover(robot, sala, biblioteca), la

precondición es:

- en(robot, sala)

No puedes moverte desde un lugar en el que no estás.

- Efectos (qué cambia tras ejecutar la acción).

Se dividen en dos listas:

- ADD list (lo que pasa a ser verdadero).

- en(robot, biblioteca)

- DELETE list (lo que deja de ser verdadero).

- ¬en(robot, sala)

Esto permite que el estado del mundo se actualice paso a paso.

# Ejemplo

Imaginemos un robot que debe ir de la sala a la biblioteca.

- Estado inicial: en(robot, sala)

- Objetivo: en(robot, biblioteca)

- Acción disponible:

- Acción: mover(robot, sala,

biblioteca)

- Precondiciones: en(robot, sala)

- Efectos:

- ADD → en(robot, biblioteca)

- DELETE → en(robot, sala)

El plan en este caso es sencillo: ejecutar esa acción. Pero en problemas más complejos, se encadenan múltiples acciones hasta alcanzar la meta.

Ejemplo (similar a minimax, pero con estados) Problema: El robot debe ir de la sala a la biblioteca.

- Estado inicial: en(robot, sala)

- Objetivo: en(robot, biblioteca)

- Acción:

- mover(robot, sala, biblioteca)

- Precondición: en(robot, sala)

- Efectos:

- ADD → en(robot, biblioteca)

- DELETE → en(robot, sala)

El plan resultante: [mover(robot, sala, biblioteca)] El robot ejecuta la acción, se actualizan los estados (ADD/DELETE) y llega al objetivo.

# Algoritmos

# de Búsqueda:

# Forward vs.

# Backward

# Chaining

En STRIPS, no solo definimos las acciones, sino que debemos decidir en qué dirección "pensar". Esto se conoce como búsqueda en el espacio de estados.

A. Búsqueda hacia adelante (Forward State-Space Search)

B. Búsqueda hacia atrás (Backward Chaining / Goal Regression)

## A. Búsqueda hacia adelante (Forward

## State-Space Search)

Es la forma más intuitiva: empiezas en el Estado Inicial y miras qué acciones puedes hacer ahora.

- Cómo funciona: El algoritmo revisa qué acciones tienen sus

Precondiciones satisfechas en el estado actual. Elige una, aplica los efectos (ADD/DELETE), llega a un nuevo estado y repite hasta que el estado actual coincida con la Meta.

- Problema: Es como intentar salir de un laberinto probando todos

los caminos desde la entrada. Si hay muchas acciones posibles, el "factor de ramificación" es enorme y la IA puede tardar siglos en encontrar el plan.

# B. Búsqueda hacia atrás (Backward

# Chaining / Goal Regression)

### • Esta es la técnica que hizo famoso a STRIPS por su eficiencia.

### Empiezas desde la Meta y trabajas hacia atrás.

### • Cómo funciona:

- Miras la Meta (ej: sandwich_hecho).

- Buscas qué acciones tienen sandwich_hecho en su lista de Efectos (ADD).

- Una vez encuentras la acción (ej: cerrar_pan), miras sus Precondiciones (ej:

tener_jamon_puesto).

- Ahora, esas precondiciones se convierten en tu nueva sub-meta.

- Repites el proceso hasta que las precondiciones de una acción ya estén

cumplidas en el Estado Inicial.

### • Ventaja: Solo consideras acciones que son relevantes para el

### objetivo. Ignoras acciones inútiles (como abrir_ventana) que podrías

### haber intentado en la búsqueda hacia adelante.

"Si su meta es 'Estar en el Planetario de Bogotá', pensar hacia adelante sería: salir de casa, ver si tomo bus, taxi o camino, ver qué ruta sirve... Pensar hacia atrás es: para estar en el Planetario debo tener una entrada; para tener la entrada debo estar en la taquilla; para estar en la taquilla debo haber llegado al Parque de la Independencia. ¿Cuál camino parece más directo?"

https://www.youtube.com/watch?v=D6lIJqfTlO8

Turismo con STRIPS

Imagina que diseñamos un agente de planificación turística. Su tarea es ayudar a un viajero a cumplir un itinerario, por ejemplo: visitar un museo y luego ir a la playa.

### 1. Definición del problema

Estado inicial:

- en(viajero, hotel)

- ¬visitado(museo)

- ¬visitado(playa)

Objetivo:

- visitado(museo)

- visitado(playa)

# 2. Acciones posibles (versión STRIPS)

mover(hotel, museo)

- Precondición:

en(viajero, hotel)

- Efectos:

- ADD →

en(viajero, museo)

- DEL → en(viajero,

hotel)

visitar(museo)

- Precondición:

en(viajero, museo)

- Efectos:

- ADD →

visitado(museo)

mover(museo, playa)

- Precondición:

en(viajero, museo)

- Efectos:

- ADD →

en(viajero, playa)

- DEL → en(viajero,

museo)

visitar(playa)

- Precondición:

en(viajero, playa)

- Efectos:

- ADD →

visitado(playa)

# 3. Plan

# resultante

Para alcanzar el objetivo (visitado(museo) ∧ visitado(playa)):

mover(hotel, museo)

visitar(museo) mover(museo, playa)

visitar(playa)

Al final, el estado se actualiza y cumple con el itinerario.

# STRIPS funciona

# como un GPS

# de planes:

El estado inicial es tu ubicación actual (hotel).

El objetivo es lo que quieres hacer (visitar lugares).

Las acciones son los caminos y actividades disponibles.

El plan es la ruta completa de pasos que conecta el inicio con el destino final.

# Relevancia

# de STRIPS

# para

# Agentes de

# IA

1. Agentes Inteligentes = Percepción + Decisión

+ Acción

- Un agente de IA debe:

- Percibir el mundo (su estado actual).

- Decidir qué hacer (elegir acciones y

ordenarlas).

- Actuar para alcanzar un objetivo.

STRIPS entra en la fase 2: Decisión. Es el “cerebro planificador” que conecta estado inicial → secuencia de acciones → objetivo.

## 2. STRIPS como

## el “manual de

## instrucciones”

## del agente

En lugar de improvisar, el agente tiene acciones definidas con precondiciones y efectos.

Así, puede razonar:

- “No puedo visitar la playa si primero no estoy en la

playa.”

- “No puedo moverme si no sé dónde estoy.”

STRIPS le da un lenguaje lógico para entender qué puede y no puede hacer.

# Relevancia práctica en

# escenario de turismo

Un agente turístico de IA que use STRIPS podría:

- Planear itinerarios personalizados(qué visitar primero,

después qué lugar).

- Evitar planes imposibles (no puede ir de hotel → playa sin

pasar por transporte, o si el lugar está cerrado).

- Optimizar rutas (encadenar acciones para lograr el máximo

con las restricciones del día).

- Ejemplo:

El viajero quierevisitar museo y playa en un día.

- El agente verifica qué es posible con las acciones definidas.

- Encuentra un plan válido (hotel → museo → playa).

- Si el museo está cerrado, replanifica (hotel → playa).

# Conexión

# con otros

# tipos de

# agentes IA

En juegos, vimos agentes que buscan la mejor jugada (minimax).

En planificación (STRIPS), el agente busca la secuencia de pasos correcta.

En aprendizaje, los agentes aprenden nuevas estrategias o ajustan planes.

STRIPS es como el primer paso hacia agentes que razonan a nivel de acciones complejas en el mundo real.

TURISMO STRIPS CODIGO

- 1. Representación de estados

- Se puede usar un conjunto (set) de predicados lógicos.

- Ejemplo:

- estado_inicial = {"en(viajero, hotel)", "¬visitado(museo)",

"¬visitado(playa)"}

- objetivo = {"visitado(museo)", "visitado(playa)"}

2. Representación de acciones STRIPS

Cada acción debería tener:

- Nombre

- Precondiciones

- Efectos (ADD y DELETE)

Esto se puede modelar como una clase o un diccionario. Ejemplo con clase:

- class Accion:

- def __init__(self, nombre, precondiciones, add, delete):

- self.nombre = nombre

- self.precondiciones = precondiciones

- self.add = add

- self.delete = delete

- 3. Función para aplicar acciones

- Verificar si se cumplen las precondiciones en el estado actual.

- Si sí, actualizar el estado:

- Eliminar (DELETE)

- Agregar (ADD)

- Ejemplo:

- def aplicar_accion(estado, accion):

- if accion.precondiciones.issubset(estado):

- nuevo_estado = (estado - accion.delete) | accion.add

- return nuevo_estado

- else:

- return None # acción no aplicable

4. Algoritmo de planificación simple

No es necesario implementar un planificador complejo. Para la clase basta con:

- Probar acciones en orden

- Ir actualizando el estado

- Ver si se alcanza el objetivo

Ejemplo:

- def planificar(estado_inicial, objetivo, acciones):

- estado = estado_inicial.copy()

- plan = []

- while not objetivo.issubset(estado):

- for accion in acciones:

- nuevo_estado = aplicar_accion(estado, accion)

- if nuevo_estado and not nuevo_estado == estado:

- plan.append(accion.nombre)

- estado = nuevo_estado

- break

- return plan

# Ejemplo aplicado a turismo

Definir estados y acciones: # Estado inicial y objetivo

- estado_inicial = {"en(viajero, hotel)"}

- objetivo = {"visitado(museo)", "visitado(playa)"}

# Acciones STRIPS acciones = [

- Accion("mover(hotel, museo)", {"en(viajero, hotel)"}, {"en(viajero, museo)"}, {"en(viajero, hotel)"}),

- Accion("visitar(museo)", {"en(viajero, museo)"}, {"visitado(museo)"}, set()),

- Accion("mover(museo, playa)", {"en(viajero, museo)"}, {"en(viajero, playa)"}, {"en(viajero, museo)"}),

- Accion("visitar(playa)", {"en(viajero, playa)"}, {"visitado(playa)"}, set())

- ]

Salida esperada: Plan encontrado: → mover(hotel, museo) → visitar(museo) → mover(museo, playa) → visitar(playa)

STRIPS y la búsqueda

- STRIPS no te da directamente el camino

exacto al objetivo.

- Lo que hace es definir acciones (con

precondiciones y efectos).

- El problema es: ¿qué secuencia de

acciones debo tomar para llegar desde el estado inicial al objetivo? Aquí es donde entra un algoritmo de búsqueda.

- STRIPS es el "lenguaje" (la representación del conocimiento), pero

para resolver el problema necesita un "motor" (el algoritmo de búsqueda).

- Uds ya trabajaron algoritmos de búsqueda (como A*, BFS, DFS o

búsqueda de costo uniforme) e identificaron cuáles son los más eficientes (como A*), entonces lo integran en la Parte 3 del código.

La conexión técnica: El "Espacio de Estados"

- En planificación, cada Nodo de la búsqueda no es una

coordenada en un mapa, sino un Estado Completo (el conjunto de predicados ADD/DELETE).

- Estado A (Nodo 1): {en(Aeropuerto), tiene(Dinero)}

- Acción: Tomar_Transporte

- Estado B (Nodo 2): {en(Parque), tiene(Dinero=0)}

Estado inicial: {'en(hotel)'} Objetivo: {'visitado(museo)'} Plan encontrado: ['mover(hotel, plaza)', 'mover(plaza, museo)', 'visitar(museo)']

1. Nodos (círculos grandes):

Cada nodo representa un estado del mundo, es decir, lo que sabe el agente en un momento dado.

1. El nodo verde: ['en(hotel)'] → estado inicial (el

turista empieza en el hotel).

2. El nodo azul: ['en(plaza)'] y ['en(museo)']

→ estados intermedios.

3. El nodo rojo: ['en(museo)',

'visitado(museo)'] → estado final que satisface el objetivo.

2. Aristas (flechas con etiquetas):

Cada flecha es una acción STRIPS que transforma un estado en otro.

1. mover(hotel, plaza) → permite pasar de estar

en el hotel a estar en la plaza.

2. mover(plaza, museo) → pasa de estar en la

plaza a estar en el museo.

3. visitar(museo) → agrega la condición de que el

museo está visitado, logrando el objetivo.

3. Colores:

1. Verde → Estado inicial.

2. Rojo → Estado objetivo (ya se cumplió lo que

pedimos).

3. Azul → Estados intermedios en el camino.

¿Qué significa esto para STRIPS y este escenario de turismo?

- El agenteno eligió la acción al azar, sino que

construyó un plan:

- [mover(hotel, plaza), mover(plaza,

museo), visitar(museo)]

- Este plan conecta el estado inicial con el estado

objetivo mediante acciones válidas (respetando precondiciones y aplicando efectos).

- El grafo te muestra no solo el camino correcto,

sino también cómo STRIPS modela los posibles estados.

El turista (agente) arranca en el hotel. STRIPS le dice:

1. Para lograr visitado(museo), primero debes

estar en el museo.

2. Para estar en el museo, primero debes ir a la plaza.

3. Para ir a la plaza, debes salir del hotel.

4. Finalmente, cuando llegas al museo, aplicas la

acción de visitarlo y alcanzas el objetivo.

ESTO ES FORW O BACKW?

# 1. Definición

# del Problema

# (The Setup)

Estado Meta (G):

dentro(Turista, Planetario) ticket(Validado)

Estado Inicial (S0):

en(Turista, Aeropuerto) tiene(Turista, Dinero) abierto(Planetario)

Objetos: Turista, Aeropuerto, Parque_Independencia, Taquilla, Ticket, Dinero.

## 2. Definición de

## Acciones

## (Operadores

## STRIPS)

### Para que el plan funcione, necesitamos estas 4

### acciones lógicas:

### Acción: Tomar_Transporte(origen, destino)

- Precondiciones: en(Turista, origen), tiene(Turista, Dinero)

- Efecto ADD: en(Turista, destino)

- Effecto DELETE: en(Turista, origen), tiene(Turista, Dinero)

### Acción: Comprar_Ticket

- Precondiciones: en(Turista, Taquilla), abierto(Planetario)

- Efecto ADD: posee(Turista, Ticket)

- Efecto DELETE: (Ninguno, o podrías borrar dinero si no se

borró antes)

2. Definición de

Acciones (Operadores STRIPS)

### Acción: Caminar(de, a)

- Precondiciones: en(Turista, de)

- Efecto ADD: en(Turista, a)

- Efecto DELETE: en(Turista, de)

### Acción: Ingresar_al_Planetario

- Precondiciones: en(Turista, Taquilla),

posee(Turista, Ticket)

- Efecto ADD: dentro(Turista, Planetario),

ticket(Validado)

- Efecto DELETE: en(Turista, Taquilla)

# 3. Fase

# Backward

# (Regresión de

# Metas)

Este es el razonamiento que deben hacer para construir el plan de atrás hacia adelante.

- Meta Final: dentro(Turista, Planetario) y ticket(Validado).

- ¿Qué acción da ese efecto? → Ingresar_al_Planetario.

- Nuevas Sub-metas (Precondiciones de la acción anterior):

Necesito estar en(Turista, Taquilla) y posee(Turista, Ticket).

- ¿Cómo obtengo el Ticket? → AcciónComprar_Ticket.

- Nuevas Sub-metas: Necesito estar en(Turista, Taquilla) (ya la

tenía) y que el Planetario esté abierto (esto es verdad en S0).

- ¿Cómo llego a la Taquilla? → Acción

Caminar(Parque_Independencia, Taquilla).

- Sub-meta: Estar en(Turista, Parque_Independencia).

- ¿Cómo llego al Parque? → Acción

Tomar_Transporte(Aeropuerto, Parque_Independencia).

- Sub-meta final: Estar en(Turista, Aeropuerto) y tiene(Turista,

Dinero).

- ¡ÉXITO! Ambas condiciones están en el Estado Inicial.

# 4. El Plan

# Final

# (Secuencia

# Ejecutable)

Una vez realizado el razonamiento backward, el plan se entrega en orden cronológico (Forward) para su ejecución:

- Paso 1: Tomar_Transporte(Aeropuerto,

Parque_Independencia)

- Paso 2: Caminar(Parque_Independencia,

Taquilla)

- Paso 3: Comprar_Ticket

- Paso 4: Ingresar_al_Planetario

Cuándo aplicar Búsqueda hacia Adelante (Forward Search)

Usar esta opción si su sector tiene las siguientes características:

- Estado Inicial muy claro, pero Meta difusa: Por ejemplo, si el objetivo

es "maximizar la eficiencia" o "recolectar la mayor cantidad de recursos", pero no hay un solo estado final específico.

- Factor de Ramificación bajo al inicio: Hay pocas acciones posibles

que se pueden hacer desde el principio.

- Conexión con Algoritmos de Búsqueda: Si planean usar A* con una

heurística de distancia (como la distancia de Manhattan o línea recta), el forward es más natural porque vas "midiendo" cuánto te acercas al objetivo en cada paso.

Cuándo aplicar Búsqueda hacia Atrás (Backward / Goal Regression)

- Meta muy específica, pero Estado Inicial complejo: Saben exactamente qué

tiene que ser verdad al final (ej. documento_firmado Y pago_realizado), pero el inicio tiene demasiadas variables irrelevantes.

- Muchos "Caminos Muertos": Si en su sector hay muchas acciones posibles

que no sirven para nada (ej. un robot en una casa que puede prender la TV, abrir la nevera, o limpiar el piso, pero su meta es solo "abrir la puerta principal").

- Eficiencia Crítica: La búsqueda hacia atrás solo considera acciones que son

relevantes (aquellas cuyo efecto ADD cumple una de las condiciones de la meta). Esto "poda" el árbol de búsqueda automáticamente.

El "Test" para su Código

- ¿Cuántas acciones puedo realizar en el Estado Inicial?

- Si son 2 o 3 → Forward es viable.

- Si son 50 → Forward va a ser muy lento.

- ¿Cuántas acciones diferentes terminan cumpliendo mi Meta?

- Si solo 1 o 2 acciones logran el efecto final → Backward es

extremadamente eficiente porque el algoritmo "sabe" por dónde empezar.

Relación con lo que ya saben (Minimax)

- Minimax es como el Forward Search: Miras el tablero actual y

proyectas hacia adelante ("si yo muevo aquí, él mueve allá").

- Backward Search es como resolver un Puzzle: Miras la imagen

completa de la caja (la meta) y vas encajando las piezas basándote en cómo deberían verse al final.

- Si implementan Forward, su función sucesora debe buscar acciones

cuyas Precondiciones se cumplan.

- Si implementan Backward, su función sucesora debe buscar acciones

cuyos Efectos ADD coincidan con la meta actual.

## La Anomalía

## de Sussman

## (Limitaciones

## de STRIPS)

- La Anomalía de Sussman es un

problema clásico en el "Mundo de los Bloques" que demostró que los planificadores lineales (como el STRIPS original) no siempre pueden encontrar la solución más eficiente, o incluso ninguna solución, si intentan alcanzar las metas una por una.

https://www.youtube.com/watch?v=uh4x1NtMUnE

### El Escenario

Imagina tres bloques (A, B, C) y una mesa.

Estado Inicial: El bloque C está sobre la mesa, el bloque A está sobre la mesa y el bloque B está sobre el bloque C.

Estado Meta: Una torre con A arriba, B en el medio y C en la base (A sobre B, B sobre C).

# El Conflicto (Por qué es

# una "Anomalía")

Un planificador lineal como STRIPS intentará resolver una sub-meta a la vez:

- Sub-meta 1: Poner B sobre C. Resulta que

esto ya está hecho en el estado inicial. El planificador pasa a la siguiente.

- Sub-meta 2: Poner A sobre B. Para hacer

esto, el robot debe recoger A. Pero para que el plan sea válido al final, ¡no puede poner A sobre B sin antes haber desarmado lo que ya tenía (porque B está debajo de algo o necesita moverse)!

El problema real: Si el planificador alcanza la Meta 1 primero, puede que bloquee la posibilidad de alcanzar la Meta 2. Si intenta arreglar la Meta 2, deshace la Meta 1. Esto se llama interferencia de metas.

"Es como si quisieras ponerte los calcetines y los zapatos. Meta A: Ponerse zapatos. Meta B: Ponerse calcetines. Si actúas como un planificador lineal tonto y decides cumplir la Meta A primero, te pones los zapatos. Cuando intentas cumplir la Meta B, te das cuenta de que tienes que deshacer la Meta A para poder continuar. STRIPS original sufría de esto porque no veía el panorama completo, solo una meta a la vez".

### PDDL: Planning Domain

### Definition Language

Un Lenguaje Estándar para la Planificación Automatizada Automatizada en IA

# PDDL: El

# Estándar

# Moderno

- PDDL se creó en 1998 para

estandarizar cómo se le presentan los problemas a los planificadores. La gran innovación es que separa el "Mundo" (las reglas) del "Problema" (la situación específica).

STRIPS: El Antecesor de la Planificación Moderna Moderna

- *Origen:** Desarrollado en 1971 para el robot

Shakey en SRI International.

- *Concepto:** Primer lenguaje formal para

representar estados, metas y acciones.

- *Estructura:** Basado en listas de precondiciones,

precondiciones, adiciones y eliminaciones.

- *Limitación:** Sintaxis rígida y dificultad para

escalar a problemas complejos.

STRIPS sentó las bases de la planificación en IA, definiendo cómo una máquina puede razonar sobre el cambio en el mundo.

# Estructura

# de PDDL

Se divide en dos archivos de texto:

- El Dominio (Domain): Aquí se define la

"física" de tu universo.

- Predicados: ¿Qué cosas pueden ser

ciertas? (ej: robot-en ?lugar, puertaabierta).

- Acciones: Las reglas de STRIPS

(Precondiciones, ADD, DELETE).

- El Problema (Problem): Aquí se define la

"instancia" particular.

- Objetos: ¿Qué elementos hay? (ej:

robot1, sala_de_computo, pasillo).

- Estado Inicial: ¿Cómo empieza todo? (ej:

robot-en sala_de_computo).

- Objetivo (Goal): ¿A dónde queremos

llegar? (ej: robot-en pasillo).

PDDL como Evolución y Estandarización de STRIPS

HERENCIA PDDL adopta la lógica de acciones de STRIPS (Precondiciones → Efectos) como su núcleo fundamental.

ESTANDARIZACIÓN PDDL nació para unificar las diversas variantes de STRIPS que existían en los años 90 en un solo estándar. COMPATIBILIDAD El requisito `:strips` en PDDL indica que el dominio dominio usa la lógica básica de STRIPS, asegurando asegurando retrocompatibilidad.

MEJORA PDDL añade tipos, jerarquías, cuantificadores y, en versiones posteriores, tiempo y recursos finitos.

Archivo de Dominio

Define tipos de objetos. Establece predicados (propiedades). Especifica acciones (operadores), precondiciones y efectos.

Archivo de Problema

Define objetos específicos. Establece el estado inicial del mundo. Define el estado objetivo (meta) a alcanzar.

Para que visualizar la separación entre Dominio y Problema, miremos esta comparación:

- "Imaginen que el Dominio son las leyes de tránsito de

Bogotá (lo que está permitido hacer en la calle). Esas leyes no cambian. El Problema es tu viaje específico de hoy: sales de la Universidad, hay un trancón en la Séptima y quieres llegar a tu casa. El planificador toma las 'reglas' (Dominio) y tu 'situación actual' (Problema) para darte la ruta".

# Ejemplo: El Mundo de los Bloques

### Archivo de Dominio

(define (domain blocks-world) (:requirements:strips:typing) (:types block) (:predicates (on?x?y - block) (ontable?x - block) (clear?x - block) ) (:action pick-up :parameters (?x - block) :precondition (and (clear?x) (ontable?x)) :effect (and (not (ontable?x)) (holding?x)) ) )

### Archivo de Problema

(define (problem stack-blocks) (:domain blocks-world) (:objects A B C - block) (:init (ontable A) (ontable B) (ontable C) (clear A) (clear B) (clear C) (handempty) ) (:goal (and (on A B) (on B C)) ) )

Aplicaciones Reales de PDDL

Robótica de Almacenes Coordinación de flotas de robots móviles para optimizar el movimiento de paquetes y evitar colisiones en centros logísticos como los de Amazon.

Exploración Espacial Planificación de actividades científicas para rovers de la NASA (Curiosity, Perseverance), gestionando ventanas de tiempo y energía solar.

Ciberseguridad Modelado de ataques de red para identificar rutas críticas y vulnerabilidades, permitiendo la generación automática de planes de defensa.

Gestión de Desastres Coordinación dinámica de drones y equipos de rescate para tareas de búsqueda, entrega de suministros y transporte de heridos.

# ¿Por qué es mejor que el STRIPS puro?

Soporta tipos: Puedes decir que un objeto es un estudiante y otro es un profesor, y que ciertas acciones solo las hace el profesor.

Acciones con parámetros: En lugar de escribir una acción para cada habitación, escribes una acción genérica Mover(?de, ?a) y la IA la adapta.

## Conclusión sobre

## la relevancia de

## STRIPS en Agentes

## de IA

- El modelo STRIPS (Stanford Research

Institute Problem Solver) es fundamental en el desarrollo de agentes de inteligencia artificial porque ofrece un marco formal para la planificación automática. A diferencia de algoritmos de búsqueda ciega, STRIPS introduce la noción de estados, precondiciones y efectos, lo que permite a un agente razonar de manera simbólica sobre cómo sus acciones transforman el mundo.

# Conclusión sobre

# la relevancia de

# STRIPS en Agentes

# de IA

Su importancia radica en que:

- Permite a los agentes generar planes

secuenciales que conducen desde un estado inicial a una meta, lo que es esencial en contextos de autonomía.

- Abstrae problemas complejos en acciones

lógicas modulares, facilitando su representación y resolución.

- Sentó las bases de muchos planificadores

modernos en robótica, logística, videojuegos e IA cognitiva.

- En síntesis, STRIPS es para la planificación

en IA lo que Minimax es para la toma de decisiones en juegos adversariales: un modelo pionero que, aunque hoy se complemente con técnicas más avanzadas, sigue siendo clave para entender cómo un agente puede pensar en el futuro y decidir qué hacer paso a paso.

https://www.youtube.com/watch?v=SforPdrZEOo

ACTIVIDAD 2

"Muchachos, en la Parte 3 del código, no van a dejar que el agente elija acciones al azar. Van a implementar el algoritmo de búsqueda que identificaron como el más eficiente (ej. A*). Su código debe:

- Tomar el Estado Inicialcomo el nodo raíz.

- Usar las acciones de STRIPS para generar los nodos hijos (sucesores).

- Usar una función de costo para encontrar la secuencia de acciones más corta hacia

la Meta.

- El 'Output' de su código debe ser la lista ordenada de pasos (el Plan) que el agente

debe ejecutar."*

# Esto es lo valioso

- Al unir Búsqueda + STRIPS, están

construyendo un Agente Inteligente Completo.

- Con Minimax, aprendieron a buscar

en un entorno donde hay un oponente (adversarial).

- Con STRIPS + Búsqueda, están

aprendiendo a buscar en un entorno donde el reto es la complejidad de la tarea y la gestión de recursos.