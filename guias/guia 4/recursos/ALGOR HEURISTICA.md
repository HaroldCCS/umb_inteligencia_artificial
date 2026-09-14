### ALGORITMOS HEURISTICA

INTELIGENCIA ARTIFICAL

## Algoritmos de Búsqueda

## Heurística en Agentes de IA

- Cuando hablamos de agentes inteligentes que

resuelven problemas, necesitamos algoritmos de búsqueda en grafos o árboles de estados. Aquí entran los algoritmos que usan heurísticas: una estimación de qué tan cerca estamos de la meta.

- Una heurística es como una pista o intuición

que le dice al algoritmo qué tan cerca está un nodo del objetivo. No es una respuesta exacta, sino una estimación que ayuda a tomar mejores decisiones.

https://www.youtube.com/watch?v=4U52GHZS04Q

# ¿Por qué se necesita?

- Sin heurística, un algoritmo como BFS o DFS explora muchos nodos sin saber

cuál es mejor.

- Con heurística, el algoritmo puede priorizar los caminos que parecen más

prometedores, reduciendo tiempo y esfuerzo.

Imaginemos que estamos en una ciudad buscando una pizzería (el objetivo).

- Sin heurística: revisas TODAS las calles una por una hasta

encontrar la pizzería.

- Con heurística: usas Google Maps que te dice “parece que

está a 3 km en esa dirección”, así avanzas hacia el objetivo más rápido.

# 1. Greedy Best-First

# Search (GBFS)

Idea central:

- Selecciona siempre el nodo con menor heurística h(n) (es decir, el que

parece estar más cerca de la meta).

- Ignora el costo recorrido g(n).

Ejemplo: Imaginemos un agente que quiere llegar a la ciudad B desde la ciudad A. La heurística h(n) puede ser la distancia en línea recta.

- Greedy escogería siempre el camino que “parece más corto” hacia la

meta, aunque a veces se meta en atajos falsos.

Ventaja: muy rápido, poco cómputo. Desventaja: no garantiza encontrar el camino más barato (no es óptimo).

La lógica: "Ojos que no ven, corazón que no siente"

el algoritmo Greedy ignora por completo el pasado (g).

Su fórmula es simplemente: f(n)=h(n)

Esto significa que al algoritmo no le importa cuánto ha caminado ni cuánto ha gastado. Solo le importa una cosa: "¿Qué tan cerca se ve la meta desde aquí?". Elige siempre el camino que parece más directo a la meta en ese instante, como si tuviera visión de túnel.

Ejemplo: El "Atajo" Peligroso

- Imaginar que estás en Monserrate y quieres llegar

rápido a tu casa.

- El pensamiento Greedy: "Veo mi casa allá abajo, voy a

bajar saltando por el barranco porque es la línea más recta".

- El problema: El algoritmo no mide el "costo" (g). No se

da cuenta de que bajar por el barranco es peligroso o imposible. Solo ve que la distancia visual disminuye.

- A en cambio:* Diría "Aunque la casa se ve ahí mismo, el

costo de bajar por el barranco es infinito o mortal, mejor tomo el sendero aunque parezca que me alejo un poco al principio".

Escenarios de "Costo" en modo Greedy

- En Tiempo (Tráfico): Un algoritmo Greedy te metería

por una calle que está justo frente a tu destino, aunque esa calle esté totalmente bloqueada por un camión, simplemente porque "estás a 10 metros".

- En Energía (Videojuegos): El personaje intentaría

atravesar un muro de fuego solo porque el tesoro está detrás, sin importar que pierda toda su vida en un segundo. No calcula el gasto de energía acumulado.

- En Dinero: Comprarías la herramienta más barata

hoy para un proyecto, sin importar que se rompa mañana y te toque comprar otra más cara (no calculas el costo a largo plazo).

# 2. A* (A estrella)

Idea central:

- Usa una combinación:

### f(n)=g(n)+h(n)

donde:

- g(n): costo real recorrido hasta el nodo.

- h(n): costo estimado hasta la meta.

Así, A* equilibra:

- mirar lo que ya gastamos (g)

- y lo que falta (h).

Propiedad clave:

- Si la heurística h es admisible (nunca sobrestima el costo

real) y consistente, entonces:

- Completo → siempre encuentra solución si existe.

- Óptimo → encuentra la mejor solución (mínimo costo).

Es el algoritmo estrella de la IA clásica porque combina rapidez y calidad de soluciones.

- Imaginar que estás en medio de una montaña y quieres llegar a un

refugio. Para decidir por qué camino ir, evalúas dos cosas:

- g(n) (El pasado): ¿Cuánto camino ya he recorrido y qué tan

cansado estoy? (Costo real).

- h(n) (El futuro): Mirando hacia el horizonte, ¿qué tan lejos se ve el

refugio en línea recta? (Costo estimado/Heurística).

- El algoritmo simplemente suma ambas: f(n)=g(n)+h(n). La ruta con

el número más bajo es la que elige seguir.

Ejemplo: El Videojuego Imagina un personaje en un calabozo (un tablero de cuadros). El personaje quiere llegar a una moneda.

Obstáculo: Hay un muro en el medio. Cálculo de A:* El algoritmo empieza a probar cuadros. Si un cuadro lo aleja de la moneda (sube h), lo descarta. Si un cuadro lo obliga a dar una vuelta muy larga (sube g), busca otra opción.

¿Por qué es el "Algoritmo Estrella"? (Las propiedades)

- Admisible (No ser optimista de más): La

heurística h nunca debe decir que falta menos de lo que realmente falta. Si el GPS te dice que llegas en 5 minutos pero en realidad faltan 20, el algoritmo se rompe. Es mejor ser conservador.

- Completo: Si hay una salida, por más escondida

que esté, A* la va a encontrar. No se queda "trabado" en un callejón sin salida infinito.

- Óptimo: No solo encuentra la salida, encuentra la

mejor (la más barata/rápida).

https://www.youtube.com/watch?v=1gszEk8rUS4&t=111s

# IDA* (Iterative Deepening A*)

A veces A* es demasiado pesado en memoria (guarda muchos nodos en cola de prioridad). Entonces aparecen variantes:

IDA* (Iterative Deepening A*)

Combina A* con búsqueda iterativa en profundidad.

- Usa como límite creciente el valor de f(n).

- Consume muchísima menos memoria.

- Ideal para problemas de espacios de estados enormes

- Este es el A* pero en versión "ahorro de recursos". El

A* normal es genial, pero tiene un defecto: tiene mucha memoria y en mapas gigantes se puede quedar sin RAM (se "ataca" de información).

- La lógica: Funciona por capas de costo. Se pone un

"límite" de presupuesto. Si no encuentra la meta con ese presupuesto, lo aumenta un poquito y vuelve a empezar.

- Imagina que buscas tus llaves en casa.

- Capa 1: Primero buscas solo en los lugares que están

a 1 metro de ti. ¿No están?

- Capa 2: Ahora buscas en todo lo que esté a 3 metros.

¿Tampoco?

- Capa 3: Subes el límite a 5 metros.

- Resultado: Encuentras las llaves gastando el mínimo

de "memoria" (no tienes que recordar toda la casa a la vez, solo la zona donde estás buscando ahora).

Escenario de "Búsqueda de Archivos" (Sistemas)

- Imagina que buscas un archivo específico en un servidor

gigante con miles de carpetas.

- Capa 1: El algoritmo busca en las carpetas raíz (las más

cercanas).

- Capa 2: Si no lo encuentra, aumenta el "umbral de

profundidad" y busca en las subcarpetas.

- La clave: A diferencia de una búsqueda simple, IDA* usa

una heurística. Si "cree" que el archivo está en la carpeta "Proyectos" porque el nombre coincide, priorizará esa rama antes de gastar presupuesto en otras, pero siempre respetando el límite de profundidad actual.

Escenario del "Presupuesto de Gasolina" (Logística)

- Imagina que un dron debe entregar un paquete en una

zona rural desconocida de Cundinamarca.

- Capa 1 (Presupuesto f=10): El dron vuela solo hasta

donde le alcancen 10 unidades de energía. Si no ve el objetivo, regresa al punto de inicio.

- Capa 2 (Presupuesto f=20): Ahora sale con permiso de

gastar 20 unidades. Explora más lejos usando la lógica de A* (distancia recorrida + estimación).

- Por qué sirve: Si el dron tiene poca memoria interna para

guardar el mapa de toda la región, solo guarda los datos de la "capa" que está explorando en ese momento.

# A con peso (Weighted A)**

Este es el A* pero "con afán". Es un punto medio entre el A* perfecto y el Greedy rápido.

- La lógica: Le damos más importancia a la meta

que al camino recorrido. La fórmula cambia a: f(n)=g(n)+W×h(n)

- (donde W es un peso mayor a 1).

Es como si le dijeras al algoritmo: "Me importa el costo, pero me importa más llegar rápido. Si encuentras una ruta que es un poquito más cara pero mucho más directa, tómala".

# A con peso (Weighted A)**

### f(n)=g(n)+w⋅h(n),w>1

Se le da más importancia a la heurística (multiplicando por un factor w).

- Si w = 1, es A* clásico.

- Si w > 1, se acelera porque confía más en la heurística.

- Pero ya no garantiza la solución óptima (se vuelve subóptimo controlado).

Útil cuando:

- Prefieres soluciones rápidas y “suficientemente buenas” en vez de óptimas.

- Ejemplo: un GPS que no necesita la ruta perfecta, solo una que sea muy buena y

calculada en segundos.

Ejemplos de Costo:

- Drones de Emergencia: Si un dron lleva un

desfibrilador, no le importa gastar un 10% más de batería (g) si eso significa llegar mucho más rápido (h) al paciente.

- Diseño de Apps: Un algoritmo que sugiere una

ruta de usuario. No busca la perfección absoluta, sino una que sea "suficientemente buena" para que la app no se quede cargando 10 segundos calculando la ruta ideal.

# RBFS (Recursive Best-First Search)

- Versión recursiva de A*.

- Mantiene en memoria solo un camino + heurísticos alternativos

(como un “backup” para retroceder si hace falta).

- También ahorra memoria.

- Puede rehacer cálculos al retroceder, pero práctico en espacios

grandes.

"El explorador con mala memoria"

- Si el A* normal recuerda todos los caminos que ha visto (lo que llena

la RAM), el RBFS solo recuerda el camino que está recorriendo en este momento y el segundo mejor camino que dejó atrás.

- ¿Cómo funciona? Avanza por la mejor ruta posible. Pero, mientras

camina, mantiene un ojo en "el plan B".

- El giro: Si el camino actual se vuelve más caro que el "plan B" que

dejó guardado, el algoritmo borra de su memoria todo lo que acaba de hacer y se devuelve a probar la otra opción.

- Lo bueno: Antes de borrar el camino malo, anota cuánto costaba

para no volver a cometer el mismo error tan fácilmente.

Ejemplos de "Costo" para el RBFS

A. Escenario de la "Cita en un Restaurante"

- Imagina que estás buscando un restaurante nuevo en Chapinero.

- Ruta A: Crees que es por la Carrera 13. Empiezas a caminar.

- Plan B: Crees que la segunda opción es la Caracas.

- Costo: Si la Carrera 13 se pone muy empinada o llena de gente (sube el costo g), y de repente parece que

te va a tomar 20 minutos más, te detienes. Olvidas los detalles de las tiendas que viste en la 13, te devuelves a donde empezaste y pruebas la Caracas.

B. Escenario de "Búsqueda de Tesoros" (Videojuegos)

- Imagina un personaje en un calabozo con dos pasillos:

- Pasillo Izquierdo: Parece más corto (h bajo).

- Pasillo Derecho: Parece un poco más largo.

El personaje entra al izquierdo. A medida que avanza, encuentra monstruos (g sube). En el momento en que el pasillo izquierdo se vuelve "más pesado" que lo que prometía el derecho, el personaje se teletransporta al inicio para ir por el derecho. No guarda el mapa del pasillo izquierdo, solo recuerda que "por ahí estaba difícil".

Greedy: “elige siempre la calle que parece más cerca del centro según el letrero, aunque pueda estar tapada”.

A*: “mira tanto lo que ya caminaste como lo que falta: balancea ambas cosas”.

IDA* y RBFS: “viajar con mapa de bolsillo, no con un atlas enorme: sacrificas cálculos repetidos pero ahorras memoria”.

A con peso*: “si tienes prisa, confías más en el GPS que en tu experiencia: llegas más rápido, aunque no siempre por la ruta óptima”.

Algoritmo Fórmula de Decisión "Personalidad" ¿Cuándo usarlo? Consumo de Memoria

A (A-Estrella)* f(n)=g(n)+h(n) El Equilibrado: Mira el pasado y el futuro.

Cuando quieres la ruta más corta y tienes buena RAM.

Alto: Recuerda todo el mapa explorado.

Greedy (GBFS) f(n)=h(n) El Impaciente: Solo le importa llegar rápido.

Para prototipos rápidos donde no hay obstáculos complejos.

Bajo/Medio: Solo sigue la meta.

IDA* f(n)=g(n)+h(n) (por capas)

El Ahorrador: Trabaja por presupuesto.

En dispositivos con muy poca memoria o mapas infinitos.

Muy Bajo: Solo guarda la ruta actual.

Weighted A* f(n)=g(n)+W×h(n) El que tiene afán: Prioriza llegar sobre el costo.

Cuando una solución "suficientemente buena" es mejor que la perfecta.

Alto: Similar al A* tradicional.

RBFS f(n) con "Plan B" guardado

El Indeciso: Se devuelve si el camino se pone feo.

Búsqueda óptima con memoria limitada (más inteligente que IDA*).

Bajo: Solo guarda el mejor y segundo mejor camino.

Algoritmo Rapidez Óptimo Memoria Uso típico

Greedy Best- First Muy alta No Baja Aproximaciones rápidas

A* Alta Sí Alta Planificación precisa

IDA* Media Sí Muy baja Espacios enormes

RBFS Media Sí Baja Alternativa recursiva a IDA*

A* con peso Muy alta No (subóptimo) Alta Aplicaciones en tiempo real

# Ejemplo: Buscar el camino más barato

# de S (Start) a G (Goal)

Imaginemos este grafo de ciudades con costos reales (g) en las aristas y una heurística (h) que es la distancia en línea recta a la meta G.

- Costos de aristas (g): números en las líneas.

- Heurística h(n): distancia estimada a G:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

Datos del problema Nodos: S, A, B, C, G

Costos de aristas: (S- A)=4, (S-B)=2, (A-B)=5, (A-C)=6, (B-G)=3, (C- G)=7

Heurística: h(S)=7, h(A)=6, h(B)=2, h(C)=3, h(G)=0

1. Greedy Best-First Search

Selecciona siempre el nodo con menor h(n).

1. Empieza en S (h=7).

2. Vecinos: A(h=6), B(h=2). → Escoge B.

3. Desde B → vecinos: G(h=0), A(h=6). →

Escoge G. Llega rápido a G con camino S → B → G. Costo real = 2 + 3 = 5 (no es óptimo).

- Costos de aristas (g): números en las líneas.

- Heurística h(n): distancia estimada a G:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

Explicación paso a paso:

1. Inicio en S

- h(S) = 7.

- No hay costo acumulado porque aún no hemos avanzado.

2. Expande S

- Vecinos:

- A con h(A) = 6

- B con h(B) = 2

- Escoge B porque su heurística (2) es menor que la de A (6).

3. Expande B

- Vecinos:

- G con h(G) = 0

- A con h(A) = 6

- Escoge G porque tiene h = 0 (es el objetivo).

4. Camino encontrado:

S → B → G

- Costo real: 2 (S→B) + 3 (B→G) = 5.

- Heurística h(n): distancia estimada:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

2. A* Search

Evalúa f(n) = g(n) + h(n).

1. En S, f(S) = 0+7=7.

2. Expande S:

- A: g=4, h=6 → f=10

- B: g=2, h=2 → f=4 → escoge B.

3. Expande B:

- G: g=5, h=0 → f=5

- A: g=7, h=6 → f=13

→ Escoge G. Camino: S → B → G. Costo = 5 (óptimo en este caso).

- Costos de aristas (g): números en las líneas.

- Heurística h(n): distancia estimada a G:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

Conceptos clave

- g(n) → Costo real acumulado desde el inicio (S) hasta el nodo n.

- h(n) → Costo heurístico estimado desde n hasta la meta (G).

- f(n) = g(n) + h(n) → Estimación total del costo pasando por n (es lo que A* usa para

decidir qué expandir).

- El objetivo: escoger el nodo con menor f(n) en cada paso.

- Nodos: S, A, B, C, G

- Costos de aristas: (S-A)=4, (S-B)=2, (A-B)=5, (A-C)=6, (B-G)=3, (C-G)=7

- Heurística:

h(S)=7, h(A)=6, h(B)=2, h(C)=3, h(G)=0

- 1. Empieza en S

- g(S)=0 (no hemos recorrido nada).

- h(S)=7 (estimación a G).

- f(S)= g+h = 0+7 = 7.

- Se expande S (porque es el único).

- 2. Desde S, genera hijos A y B

- Para A:

- g(A)=4 (costo real desde S→A).

- h(A)=6.

- f(A)=4+6=10.

- Para B:

- g(B)=2.

- h(B)=2.

- f(B)=2+2=4.

- Escogemos B porque f(B)=4 es el menor.

- 3. Expande B

- Hijos: G y A.

- Para G:

- g(G)=g(B)+costo(B→G)=2+3=5.

- h(G)=0.

- f(G)=5+0=5.

- Para A (por B):

- g(A)=g(B)+costo(B→A)=2+5=7.

- h(A)=6.

- f(A)=7+6=13.

- Escogemos G porque f(G)=5 es menor que el resto.

Camino óptimo

- Ruta: S → B → G

- Costo real: g(G)=5 (óptimo).

g(n) = lo que realmente has recorrido. h(n) = lo que falta según estimación (heurística). f(n) = mezcla de ambos: lo que llevas + lo que falta estimado. A* siempre expande el nodo con el menor f(n) en la frontera.

3. A* con peso (w=2)

f(n) = g(n) + 2·h(n) (confía más en la heurística).

1. S: f=0+2·7=14.

2. Expande:

- A: f=4+12=16

- B: f=2+4=6 → escoge B.

3. En B:

- G: f=5+0=5 → escoge G.

Camino S → B → G. Es rápido pero si hubiera un atajo engañoso, podría perder la óptimalidad.

- Costos de aristas (g): números en las líneas.

- Heurística h(n): distancia estimada a G:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

- Más peso a h(n) significa que confía más en la estimación que en el costo

real.

- Esto hace que el algoritmo explore más como Greedy, porque la heurística

manda, pero sin ignorar g(n) por completo.

- Resultado: va más rápido, pero puede dejar de ser óptimo.

Ejemplo paso a paso Inicio en S

- g(S) = 0

- h(S) = 7

- f(S) = 0 + 2×7 = 14

2. Expandir S (vecinos)

- A: g = 4, h = 6 → f = 4 + 2×6 = 16

- B: g = 2, h = 2 → f = 2 + 2×2 = 6

- Escoge B (menor f).

3. Expandir B

- G: g = 5, h = 0 → f = 5 + 2×0 = 5

- Escoge G.

Camino encontrado: S → B → G Costo real: 2 + 3 = 5 (igual que A*, pero eso fue suerte).

- Costos de aristas (g): números en las líneas.

- Heurística h(n): distancia estimada:

- h(S)=7

- h(A)=6

- h(B)=2

- h(C)=3

- h(G)=0

4. IDA*

Haría lo mismo que A*, pero en vez de expandir todo, lo hace por niveles de f(n) creciente.

- Primero busca con límite f=7, luego f=10, etc.

Encuentra el mismo camino que A*. Usa menos memoria, aunque repite exploraciones.

5. RBFS

Similar a A*, pero solo guarda el camino actual y el siguiente mejor.

- Seguiría la misma lógica que A*, pero

retrocedería si el camino elegido empeora. Encuentra el mismo camino que A*. Consume menos memoria.

# Escenario: Ruta turística en la ciudad

- Supongamos que el mapa de sitios turísticos es así:

- Inicio: Plaza Mayor (S)

- Meta: Catedral (G)

- Costos reales (g): tiempo en minutos caminando.

Heurística (h): distancia estimada en línea recta (en minutos).

Sitio h(n) a Catedral Plaza Mayor (S) 10 Museo Arte 6 Parque Central 4 Mirador 3 Catedral (G) 0

Antes (DFS y BFS)

- DFS: podría recorrer todo antes de llegar a Catedral → ineficiente.

- BFS: encuentra la ruta con menos saltos (no necesariamente la

más corta en tiempo). Ejemplo:

# Grafo del caso turístico

- Inicio: Plaza Mayor (S)

- Meta: Catedral (G)

- Costos (g): en aristas.

- Heurística h(n):

- Plaza = 10

- Museo = 6

- Parque = 4

- Mirador = 3

- Catedral = 0

# Greedy Best-First

- Solo mira h(n):

- S(h=10) → vecinos: Museo(6), Parque(4) → elige

Parque.

- Parque(h=4) → vecinos: Catedral(0), Museo(6) →

elige Catedral. Ruta: Plaza → Parque → Catedral (Costo: 6 min). Fue buena porque la heurística es coherente, pero si hubiera un camino más barato por otro lado, Greedy podría fallar.

Sitio h(n) a Catedral Plaza Mayor (S) 10 Museo Arte 6 Parque Central 4 Mirador 3 Catedral (G) 0

# Greedy Best-First Search paso a paso

- Regla: escoger siempre el nodo con menor h(n).

- Cola de prioridad (ordenada por h):

- Inicial: [Plaza(10)]

1. Expandir Plaza (10)→

Vecinos:Museo(6)Parque(4)Cola: [Parque(4), Museo(6)]

2. Expandir Parque (4)→

Vecinos:Catedral(0)Museo(6)Cola: [Catedral(0), Museo(6), Museo(6)]

3. Expandir Catedral (0) → ¡Meta alcanzada!

- Ruta: Plaza → Parque → Catedral

- Costo real: 2 + 4 = 6 min

A*

- f(n) = g(n)+h(n):

- S: f=0+10=10

- Museo: g=4, f=4+6=10

- Parque: g=2, f=2+4=6 → elige Parque.

- Desde Parque: Catedral: g=6, f=6+0=6 → llega.

Ruta: Plaza → Parque → Catedral (Costo óptimo: 6 min).

Sitio h(n) a Catedral Plaza Mayor (S) 10 Museo Arte 6 Parque Central 4 Mirador 3 Catedral (G) 0

# A Search paso a paso*

Regla: escoger nodo con menor f(n)=g+h.

Inicial:

Plaza: g=0, h=10, f=10 Cola: [Plaza(10)]

1. Expandir Plaza

Vecinos:

Museo: g=4, h=6 → f=10

Parque: g=2, h=4 → f=6 Cola: [Parque(6), Museo(10)]

2. Expandir Parque (f=6)

Vecinos:

Catedral: g=6, h=0 → f=6

Museo: g=9, h=6 → f=15 Cola: [Catedral(6), Museo(10), Museo(15)]

3. Expandir Catedral (f=6) → ¡Meta alcanzada!

Ruta: Plaza → Parque → Catedral Costo óptimo: 6 min

A con peso (w=2)*

- f(n)=g+2*h:

- Plaza: 0+20=20

- Parque: 2+8=10

- Museo: 4+12=16 → elige Parque primero (igual

que Greedy). Ruta igual que Greedy y A*, pero si había un atajo más largo, podría equivocarse.

Sitio h(n) a Catedral Plaza Mayor (S) 10 Museo Arte 6 Parque Central 4 Mirador 3 Catedral (G) 0

# IDA* y RBFS

- Igual que A*, pero más eficientes en memoria para grandes grafos

(no aplica mucho aquí porque el mapa es pequeño).

- Conceptualmente, sigue encontrando el mismo camino.

- Greedy: ignora costo real, por

eso puede equivocarse si hay caminos más caros con buen h.

- A*: considera costo real y

estimado, por eso es óptimo (si h es admisible).

- Visualiza la cola de prioridad:

es la clave para entender la diferencia.

# ¿Por qué es

# clave

# visualizar la

# cola de

# prioridad?

En BFS y DFS, los nodos se exploran en orden FIFO (cola) o LIFO (pila). En A* y Greedy, no. Ellos usan una Priority Queue:

Greedy Best-First Search: ordena por h(n) (heurística → el más prometedor según estimación).

A*: ordena por f(n) = g(n) + h(n) (costo real + estimación).

Esto cambia todo, porque:

El algoritmo no expande en orden de llegada.

Puede saltar nodos intermedios si encuentra otro más prometedor.

Imaginemos la cola como una lista ordenada por prioridad. Cada vez que generamos sucesores, los insertamos según su f(n) o h(n). Ejemplo en turismo (A desde Plaza a Mirador):*

- Inicio: Plaza → f = 0 + h(Plaza)

- Se expanden los vecinos:

- Museo: f = 2 + h(Museo)

- Parque: f = 3 + h(Parque)

- La cola se ordena: primero el menor f.

Visualización:

Luego, si agregamos Catedral:

- Nodos:

Plaza, Museo, Parque, Mirador, Catedral

- Conexiones y costos: •Heurística (distancia en línea recta hacia

Catedral):

# RUTAS

# ENCONTRADAS

# POR CADA

# ALGORITMO

Greedy Search: Plaza → Parque → Mirador → Catedral A* Search: Plaza → Museo → Mirador → Catedral Weighted A*: Plaza → Parque → Mirador → Catedral IDA* Search: Plaza → Museo → Mirador → Catedral RBFS Search: Plaza → Museo → Mirador → Catedral

Greedy Search: Plaza → Parque → Mirador → Catedral

A* Search: Plaza → Museo → Mirador → Catedral

Weighted A*: Plaza → Parque → Mirador → Catedral

IDA* Search: Plaza → Museo → Mirador → Catedral

RBFS: Plaza → Museo → Mirador → Catedral

Algoritmo Usa g(n)? Usa h(n)? Óptimo? Memoria Velocidad

Greedy Best- First No Sí No Baja Muy rápida

A* Sí Sí Sí Alta (mantiene nodos en memoria)

Lento en grafos grandes

IDA* Sí Sí Sí Muy baja (profundidad iterativa)

Más lento que A* pero manejable

RBFS Sí Sí Sí Baja (usa recursión)

Similar a A* pero menos memoria

A con peso* Sí Sí (ponderada) No (subóptimo controlado) Media Más rápido que A*

# Cómo diseñar

# buenas

# heurísticas

¿Qué es una heurística?

En estos algoritmos (Greedy, A*), la heurística h(n) estima el costo desde el nodo actual n hasta el objetivo, sin realizar la búsqueda completa. El objetivo es orientar la exploración para que no sea ciega como BFS/DFS, sino guiada hacia la meta.

# Cómo diseñar buenas heurísticas

Debemos comprender que la heurística define la eficiencia y corrección del algoritmo.

Conceptos clave:

- Admisible: Nunca sobreestima el costo real (garantiza optimalidad en A*).

- Consistente (monotónica): Cumple h(n) ≤ c(n, a, n’) + h(n’), evita reexplorar nodos.

Ejemplo en caso turístico:

- Heurística básica: Distancia en línea recta (Euclidiana) al destino.

- Mejor heurística: Distancia en línea recta + penalización por zonas congestionadas (si

hay tráfico o calles cerradas).

- Heurística no admisible (ejemplo malo): Distancia en línea recta / 2 (porque subestima

el costo real, no siempre será óptima).

# Características de una buena heurística

Una heurística debe cumplir al menos estos principios:

1. Admisible (para A)*

- Nunca sobrestimar el costo real hacia la meta.

- Ejemplo: Si la distancia real en carretera es 8 km, una heurística de 5 km (línea

recta) es admisible.

2. Consistente (monótona)

- h(n) ≤ cost(n,a,n') + h(n')

- Significa que, al moverse al siguiente nodo, la heurística no da saltos extraños.

- Esto ayuda a que A* no reprocese nodos.

3. Eficiente de calcular

- Debe ser rápida. No tiene sentido gastar más tiempo calculando h(n) que

explorando el grafo.

4. Relevante al dominio

- Debe usar información significativa del problema.

- Ejemplo: en turismo, usar distancia geográfica; en logística, tiempo estimado.

# Tener en cuenta lo siguiente:

1. Admisibilidad

- Definición: Una heurística es admisible si nunca sobreestima el costo real para

llegar al objetivo.

- Por qué es importante: Garantiza que algoritmos como A* encuentren la

solución óptima.

- Ejemplo en turismo: Si tu heurística es la distancia aérea (en línea recta) entre

un sitio turístico actual y el destino, esto nunca será mayor que la distancia real por carreteras.

2. Consistencia (Monotonicidad)

- Definición: Para todo nodo n y su sucesor n' con costo c, debe

cumplirse: h(n)≤c(n,n′)+h(n′)

- Por qué es importante: Asegura que los valores f(n) no disminuyan,

evitando reexpansiones innecesarias.

- Ejemplo en turismo: Si moverse de Plaza Mayor a un parque cuesta 2,

la heurística desde Plaza Mayor no debería superar la heurística desde el parque + 2.

donde:

- h(n) = heurística en el nodo actual n.

- c(n, n’) = costo real de ir de n a un sucesor n’.

- h(n’) = heurística del nodo sucesor n’.

# Ejemplo

- Nodo actual: A

- Sucesor: B

- Costo real entre ellos: c(A, B) = 3

- h(A) = 8

- h(B) = 5

Aplicamos la regla:

- h(A)≤c(A,B)+h(B)

- 8≤3+5 -> 8≤8 (es consistente)

Si fuera:

- h(A) = 10

- h(B) = 5

- 10≤3+5 -> 10≤8 (NO consistente)

- Esto significa que la heurística en A

era demasiado grande comparada con el camino pasando por B.

Si tu predicción de distancia desde A es 10, pero si das un paso a B cuesta 3 y desde B predices 5, entonces tu predicción inicial (10) no tiene sentido porque podías haber dicho 3 + 5 = 8.

Ejemplo :

- Imagina que buscas en un mapa:

- Nodo n: Bogotá

- Sucesor n’: Tunja

- Meta: Bucaramanga

- Si la heurística h(Bogotaˊ)= 400 km (estimado a Bucaramanga),

y c(Bogotaˊ,Tunja)= 150 km, y h(Tunja)= 250 km (de Tunja a Bucaramanga),

Entonces:

- h(Bogotaˊ)=400≤150+250=400 Se cumple → heurística consistente.

- Si en cambio hubiéramos puesto h(Bogotaˊ)=450 entonces:

- 450≰400 No consistente → puede romper la optimalidad de A*.

# Pasos para

# diseñar la

# heurística

a) Identificar el criterio principal del problema

- ¿Minimizar distancia? ¿tiempo? ¿costo

monetario? ¿impacto ambiental?

b) Determinar una medida que sea fácil de estimar y correlacionada con el objetivo real

- Ejemplo: Línea recta en mapas → correlaciona

bien con distancia real.

c) Asegurar que no sobreestime (si usamos A)*

- Mejor subestimar que sobreestimar.

d) Normalizar si hay varias variables

- Si hay más de un factor (ej. tiempo y costo), usar

ponderación.

Sector Objetivo Heurística posible (h(n))

Turismo Llegar al punto turístico más rápido Distancia en línea recta al destino (Euclidiana)

Logística Entregar pedidos en menor tiempo Tiempo estimado = Distancia en línea recta / velocidad promedio

Salud Hospital más cercano Distancia geográfica o tiempo promedio considerando tráfico

E-commerce Minimizar costo de envío Distancia al almacén más cercano (proxy del costo)

Energía Conectar nodos con menor pérdida Diferencia de voltaje estimada entre nodos

“Cuando hablamos de agentes de IA, podemos tener agentes clásicos que piensan en grafos y reglas, o agentes modernos que piensan en probabilidades y datos. Ambos son agentes, pero con cerebros diferentes. Hoy en la industria incluso se combinan: un LLM entiende la orden, y un planificador clásico decide cómo cumplirla.”

Ejemplo para un proyecto

- Un agente explorador en un laberinto:

- Clásico: usa A* para encontrar la ruta

más corta a la salida.

- LLM (API): recibe la instrucción en

lenguaje natural (“quiero ir por el camino más seguro, no el más corto”).

- Híbrido: el LLM traduce esa orden en un

criterio, y el planificador clásico la ejecuta en el grafo.

TALLER HEURISTICOS