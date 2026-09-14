INTELIGENCIA ARTIFICIAL

Búsqueda en juegos (Minimax + alfa-beta)

Planificación (STRIPS, representación de conocimiento)

Incertidumbre y redes bayesianas

# 1. Búsqueda

# en juegos

# (Minimax +

# poda alfa-

# beta)

Los juegos de dos jugadores adversarios (como ajedrez, damas o tres en raya) se pueden modelar como un árbol de estados:

- Cada nodo es un estado del juego.

- Cada arista es una jugada posible.

- El algoritmo Minimaxasume que:

- Un jugador (MAX) quiere maximizar su utilidad (ganar).

- El otro (MIN) quiere minimizar la utilidad de MAX (evitar

perder).

- Lapoda alfa-beta mejora Minimax: reduce el número de nodos

evaluados descartando ramas que no afectan la decisión final.

Ejemplo sencillo

- Juego: Tres en raya.

- Estado: faltan 2 jugadas y es turno de MAX.

- Minimax evalúa todas las posibilidades hasta el final.

- Alfa-beta descarta ramas donde ya sabemos que MIN o MAX

tienen una opción mejor.

# 2.

# Planificación

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

# 3.

# Incertidumbre

# y Redes

# Bayesianas

- En IA clásica, el conocimiento es determinista (“si pasa

A, entonces B”).

- En el mundo real hay incertidumbre: los sensores

fallan, los datos son incompletos.

- Las redes bayesianas permiten modelar esta

incertidumbre:

- Son grafos dirigidos acíclicos.

- Los nodos representan variables aleatorias.

- Los arcos representan dependencias

probabilísticas.

- Cada nodo tiene una tabla de probabilidad

condicional (CPT).

- Ejemplo

- Diagnóstico médico:

- Variable Fiebre depende de Gripe.

- Variable Dolor cabeza depende de Gripe.

- Se puede calcular: P(Gripe | Fiebre ∧ Dolor cabeza)

con teorema de Bayes.

Búsqueda en juegos (Minimax + poda alfa-beta)

# Concepto

# Central: El

# Adversario

# Racional

- El algoritmo Minimax se

basa en modelar un juego como un árbol de decisiones. La idea fundamental es que hay dos tipos de jugadores:

- MAX: Nuestro agente, que

siempre intentará maximizar su puntuación (ganar).

- MIN: El oponente, que

siempre intentará minimizar la puntuación de MAX (hacernos perder).

- "Yo muevo para ponerme

en la mejor posición posible, asumiendo que mi rival responderá con la jugada que sea peor para mí".

# 1. Búsqueda en juegos (Minimax + poda alfa-

# beta)

Paso 1. Concepto general

Minimax: dos jugadores con intereses opuestos toman decisiones sobre un conjunto de jugadas posibles.

Alfa-beta: optimización que evita evaluar movimientos que no cambiarán el resultado.

En turismo lo podemos reinterpretar:

MAX → representa al turista responsable, que quiere maximizar la experiencia positiva y el impacto sostenible.

MIN→ representa al impacto negativo ambiental, que “responde” a cada decisión tratando deminimizar la sostenibilidad.

Cada “jugada” es una decisión de viaje: elegir transporte, alojamiento, actividades, etc.

## Personajes del Juego:

- Tú (el Turista Inteligente): Eres el jugador MAX. Tu único objetivo

es MAXIMIZAR tu puntuación final. Una puntuación alta significa un viaje increíble y sostenible.

- El Impacto Ambiental (El Oponente): Es el jugador MIN. Su

único objetivo es MINIMIZAR tu puntuación. Representa los peores escenarios, como la contaminación, el gasto de recursos o una mala experiencia. Siempre asumiremos que este "oponente" es muy listo y siempre escogerá la opción que sea peor para ti.

# Paso 2.

# Representación

# en árbol de

# juego

- Unárbol de decisión turística con dos jugadores:

- Nivel MAX (turista): elige acción → Transporte ecológico (bus, bici,

caminar) o transporte contaminante (carro, avión).

- Nivel MIN (impacto ambiental): responde con efectos → mayor

huella de carbono, basura, desgaste de recursos.

Ejemplo

Estado inicial: turista planea visitar un páramo.

- Opciones:

- Ir en bus eléctrico (MAX) → menor huella.

- Ir en carro particular (MAX) → mayor huella.

- El “adversario” (MIN) responde:

- Si hay bus → impacto bajo.

- Si hay carro → impacto alto.

- El algoritmo calcula hasta el final de la secuencia de decisiones y

sugiere la opción que maximiza sostenibilidad.

- A es el nodo raíz, el jugador MAX

quiere maximizar el valor. Los hijos (B y C) son MIN, quieren minimizar. Las hojas (D, E, F, G) tienen valores fijos.

# Recorrido con Minimax + poda alfa-beta

Inicio en A (MAX): α = -∞, β = +∞.

- Explora rama B (MIN).

- Explora D = +3 → MIN elige provisionalmente 3.

- Explora E = +5 → MIN elige min(3,5)=3.

- B devuelve 3 a A.

- Ahora α=3.

- Explora rama C (MIN).

- Explora F = +2. Como MIN devuelve provisionalmente 2, y α=3,

Aquí ya entra la poda alfa-beta: como MIN no puede devolver nada mayor que 2, y 2 < 3, no es necesario revisar G.

- Se poda la rama G.

- C devuelve 2.

- MAX elige entre 3 (B) y 2 (C) → elige 3.

- Resultado: la mejor jugada es elegir la rama izquierda (B), con valor 3.

El mejor valor encontrado es: 3

# Paso 3.

# Evaluación

# (función de

# utilidad)

Asignamos valores a los resultados:

+10 → turismo sostenible (huella baja, apoyo a comunidad local).

0 → impacto medio (huella moderada).

- 10 → turismo no sostenible (huella alta, contaminación).

El Minimax buscará el recorrido de decisiones convalor máximo, considerando siempre que el adversario (impacto ambiental) “recorta” opciones.

# ¿Qué es una función de utilidad?

- Imagina que tienes que elegir entre varias opciones (ir en bus, avión,

elegir un hotel, hacer una actividad).

- Cada opción te da una consecuencia diferente (más caro, más ecológico,

más divertido, más cansado…).

- La función de utilidad es una forma de ponerle un número a cada

consecuencia para poder compararlas.

- En otras palabras:

La utilidad es como una calificación numérica que resume qué tan buena o mala es una decisión para ti.

Ejemplo sencillo (vida diaria)

- Comer hamburguesa → utilidad = +8 (muy rico, pero no tan sano).

- Comer ensalada → utilidad = +6 (sano, pero no tan rico).

- Comer pizza → utilidad = +9 (delicioso, pero más caro).

La función de utilidad convierte estas elecciones subjetivas en números comparables. Así, el algoritmo puede decidir objetivamente: la pizza (+9) es mejor que la ensalada (+6).

Para mi caso de turismo

- Sostenibilidad (ecológico vs. contaminante).

- Costo (bus barato vs. avión caro).

- Experiencia del turista (senderismo enriquecedor vs. mototour dañino).

y asignamos números como:

- "Senderismo con bus y eco-hotel" → +10 (lo mejor en experiencia, barato y

ecológico).

- "Mototour con avión y hotel cadena" → –10 (lo peor: caro, contamina y poca

experiencia positiva).

# Entonces…

- La utilidad es simplemente un número que representa lo bueno o malo

de una decisión.

- Sirve como puntuación final para que el algoritmo Minimax con poda

alfa-beta pueda decidir cuál camino es mejor, en vez de quedarse atrapado en descripciones cualitativas. Elijan qué factores son importantes en su sector (ej: en salud = riesgo del paciente, en banca = ganancia/riesgo financiero, en educación = aprendizaje/calidad). Denle un número a cada resultado según esos factores. Usen esos números como la función de utilidad en el árbol de decisiones.

# Paso 3.

# Evaluación

# (función de

# utilidad)

Asignamos valores a los resultados:

+10 → turismo sostenible (huella baja, apoyo a comunidad local).

0 → impacto medio (huella moderada).

- 10 → turismo no sostenible (huella alta,

contaminación).

El Minimax buscará el recorrido de decisiones con valor máximo, considerando siempre que el adversario (impacto ambiental) “recorta” opciones.

# Paso 4. Poda

# alfa-beta

En un árbol grande (muchas decisiones de transporte, comida, alojamiento, actividades):

La poda alfa-beta elimina ramas que claramente llevan a peores resultados sostenibles.

Ejemplo: si ya sabemos que una decisión lleva a

- 10, no necesitamos

explorar más ramas de ese camino.

- Cuando usamos Minimax (el algoritmo de búsqueda en

juegos/decisiones), hay que revisar todas las posibles jugadas/resultados. ¡Pero eso es carísimo! El árbol puede tener miles de opciones.

La idea de la poda alfa-beta

- La poda alfa-beta es como decir:

- "Si ya sé que este camino nunca será mejor que otro que ya

encontré, ni me molesto en revisarlo."

- Es como ahorrar tiempo dejando de revisar opciones que no

tienen ninguna posibilidad de ser la mejor.

Imagina que vas a comprar una camiseta:

- Ves una tienda y encuentras una camiseta

bonita por $50.000. → Guardas ese precio en tu cabeza.

- En la siguiente tienda, ves que las camisetas

empiezan en $100.000. → Automáticamente dices: “Ya no vale la pena revisar más aquí” porque ya encontraste una mejor opción más barata. Eso es exactamente lo que hace la poda alfabeta: descarta ramas enteras que no mejorarán la decisión.

# Lo de “alfa” y “beta”

- Alfa (α): el mejor valor seguro que puede tener el jugador que maximiza

hasta ahora. (Ej: el mejor precio/barato encontrado).

- Beta (β): el mejor valor seguro que puede tener el jugador que minimiza

hasta ahora. (Ej: el peor precio/caro encontrado).

- Si en algún momento α ≥ β, significa:

“Lo que queda por mirar ya no puede mejorar el resultado, así que podo (corto) esas ramas.” En el caso de turismo

- Revisamos primero la opción "Bus + Eco-hotel + Senderismo" → utilidad +10.

- Luego, vamos a revisar "Bus + Eco-hotel + Mototour".

Pero como ya vimos un camino de +10, y sabemos que Mototour suele dar peores resultados… Cortamos ahí mismo sin evaluar todo, porque no podrá superar el +10.

- Eso ahorra cálculos y acelera la decisión.

Es como si tuvieras un árbol de decisiones con 100 ramas. Con Minimax normal → revisas las 100. Con poda alfa-beta → tal vez solo necesites mirar 40, porque las otras 60 ya sabes que no sirven.

Es un atajo inteligente para no perder tiempo evaluando lo que ya sabemos que no va a ser la mejor opción.

# Árbol de turismo simplificado

- Transporte:

- Bus eléctrico

- Avión

- Hotel:

- Eco-hotel

- Cadena hotelera

- Actividad:

- Senderismo

- Mototour

- Con las utilidades que ya definimos (recuerdo algunos):

- Senderismo (Bus-Eco) = +10

- Mototour (Bus-Cadena) = –2

- Senderismo (Avión-Cadena) = –6

- Mototour (Avión-Cadena) = –10

Paso a paso con poda alfa-beta Inicio en la raíz (el turista decide transporte). Tenemos que revisar las ramas para encontrar la mejor utilidad posible. •

- Rama 1: Bus eléctrico

- Entramos a la opción Bus eléctrico.

- Eco-hotel (dentro de Bus)

- Revisamos Senderismo (Bus-Eco) → utilidad = +10.

Guardamos:"Mejor valor actual (alfa) = +10".

- Luego viene Mototour (Bus-Eco).

Pero… como ya tenemos +10, y este tipo de actividad suele dar menos… ¡Podamos esta rama! No la revisamos más.

- Cadena hotelera (dentro de Bus)

- Revisamos Senderismo (Bus-Cadena) → utilidad = +3.

- Revisamos Mototour (Bus-Cadena) → utilidad = –2.

- El mejor valor en esta rama sigue siendo +10 (del Eco-hotel).

- Con esto, el Bus eléctrico ya nos dio un valor óptimo de +10.

- Rama 2: Avión

- Ahora pasamos al Avión.

- Eco-hotel (dentro de Avión)

- Revisamos Senderismo (Avión-Eco) → utilidad = –

3.

- El turista ya piensa: "Con el Bus ya tenía +10, aquí

voy en negativo…". Entonces, cuando llegamos a Mototour (Avión- Eco), sabemos que no vale la pena revisar más. ¡Poda aquí también!

- Cadena hotelera (dentro de Avión)

- Revisamos Senderismo (Avión-Cadena) → utilidad

= –6.

- Como ya sabemos que el Bus da +10, cualquier

cosa que salga negativa con Avión no puede competir. Se podan las opciones restantes (incluido Mototour).

- Resultado final

- Mejor opción encontrada:

Bus eléctrico + Eco-hotel + Senderismo → +10

- Podas realizadas:

- "Mototour (Bus-Eco)"

- "Mototour (Avión-Eco)"

- "Mototour (Avión-Cadena)"

Analogía

- Es como si al planear un viaje:

- Ya encuentras una opción súper buena y barata en el bus + eco-hotel.

- Entonces, cuando llegas a mirar vuelos caros o actividades que

contaminan… Ni te gastas tiempo, porque ya sabes que no superan tu mejor hallazgo.

1. Nodos azules → representan las decisiones y resultados

(transporte, hotel, actividad).

1. Ejemplo: Bus eléctrico, Eco-hotel (Bus),

Senderismo (Bus-Eco) con utilidad = 10.

2. Nodos en rojo → son los podados.

1. Significa que el algoritmo ni siquiera los evaluó,

porque ya sabía que no podían superar la mejor opción encontrada.

3. Valores en los nodos hoja → son las utilidades que

asignamos.

1. Ejemplo: Senderismo (Bus-Eco) = 10 (mejor

resultado).

2. Mototour (Avión-Cadena) = -10 (peor

resultado).

4. Estructura del árbol →

1. Raíz = Inicio.

2. Primer nivel = transporte (Bus eléctrico,

Avión).

3. Segundo nivel = hoteles.

4. Tercer nivel = actividades con su utilidad.

- El turista parte en Inicio.

- Si sigue la rama Bus eléctrico →

Eco-hotel (Bus) → Senderismo, llega al mejor valor: 10.

- Cuando explora ramas del avión,

rápidamente se descartan (poda) porque ya no superan el valor encontrado con el bus.

Esto demuestra gráficamente que la poda alfa-beta evita revisar caminos inútiles y acelera la decisión.

# Cómo adaptar

# Minimax + Alfa-

# Beta a cada

# sector

1. Identificar los jugadores

- En juegos es MAX vs MIN.

- En contextos aplicados, los jugadores

representanfuerzas opuestas.

- Turismo: Turista responsable (MAX) vs

Impacto ambiental (MIN).

- Salud: Médico (MAX) vs Enfermedad (MIN).

- Comercio electrónico:Cliente (MAX) vs

Competencia o fraude (MIN).

- Banca: Banco que quiere maximizar

retorno (MAX) vs Riesgo de impago (MIN).

2. Definir estados y acciones

- Cada nodo = un estado posible.

- Cada arista = una acción o decisión.

- Ejemplos:

- Turismo: transporte, alojamiento,

actividad.

- Salud: tratamiento A o B, cirugía vs

medicación.

- Educación: estudiar tema 1 vs tema 2,

reforzar lectura vs matemáticas.

3. Diseñar la función de utilidad (score)

- Aquí está la clave: ¿qué significa “ganar” o

“perder” en cada sector?

- Turismo: sostenibilidad, huella de carbono,

apoyo local.

- Salud: recuperación del paciente, efectos

secundarios.

- Banca: rentabilidad, riesgo.

- Educación: aprendizaje, motivación, retención

del estudiante.

- Marketing: ventas, satisfacción del cliente,

fidelidad.

4. Incorporar métricas y herramientas reales

Cada grupo puede apoyarse en métricas específicas del sector. Turismo

- Indicadores de turismo sostenible(UNWTO, PNUMA, Global

Sustainable Tourism Council)

- Huella de carbono (kg CO₂ por turista).

- Apoyo a la economía local (% gasto en negocios locales).

- Generación de residuos sólidos.

Salud

- Calidad de vida del paciente (QALY – Quality Adjusted Life Years).

- Probabilidad de éxito del tratamiento.

- Costo-efectividad.

Banca

- Tasa de interés.

- Riesgo de incumplimiento (default probability).

- Retorno sobre inversión (ROI).

Comercio electrónico / Marketing

- Conversion Rate (CR).

- Customer Lifetime Value (CLV).

- Nivel de satisfacción del cliente (NPS – Net Promoter Score).

Educación

- Tasa de retención.

- Promedio de notas en evaluaciones.

- Nivel de participación.

CASO SECTOR

## 1. Definir el

## juego en su

## sector

Identificar MAX (el que quiere ganar o mejorar).

Identificar MIN (el que se opone o reduce ese beneficio).

Ejemplo en salud: MAX = médico/paciente, MIN = enfermedad.

# 2. Plantear el árbol de decisiones

Estados iniciales: situación de partida.

Acciones posibles: qué opciones tiene el jugador MAX.

Respuestas: cómo actúa el “adversario” (jugador MIN).

Ejemplo en banca: estado inicial = cliente pide un préstamo; acciones = aprobar o rechazar; respuestas = pagar o incumplir.

3. Construir

la función de utilidad (score)

### 4. Fuentes de indicadores (internacionales o locales)

Buscar estándares oficiales (ONU, OMS, ISO, OECD, ministerios locales).

Usar papers o reportescon métricas conocidas.

O, si no encuentran, plantear sus propios indicadores justificados (ejemplo: “consideramos que una tasa de abandono > 20% es negativa para educación”).

EJEMPLO

# 1. Definición de

# jugadores

- MAX → Turista responsable (quiere

maximizar la experiencia y minimizar su huella).

- MIN → Impacto ambiental negativo

(contaminación, sobrecarga de recursos). Esto permitió modelar el turismo como un “juego de fuerzas opuestas”:

- El turista toma decisiones.

- El impacto ambiental responde reduciendo

la sostenibilidad de esas decisiones.

# 2. Árbol de

# decisiones

- Se diseñó un árbol pequeño con 3 tipos de

decisiones:

- Transporte: bus eléctrico vs avión.

- Alojamiento: eco-hotel local vs cadena

internacional.

- Actividad: senderismo guiado vs mototour.

- Cada combinación lleva a un resultado final

(una hoja del árbol).

# 3. Indicadores

# de

# sostenibilidad

# turística

- Con base enreferencias reales de organismos

internacionales (Global Sustainable Tourism Council – GSTC, PNUMA/ONU Medio Ambiente, y OMT – Organización Mundial del Turismo). Ellos miden la sostenibilidad turística en varios ejes, de los cuales se toman 3 muy claros:

- Huella de carbono

- Ejemplo: transporte en avión ≈ mucho CO₂, transporte en

bus eléctrico ≈ bajo CO₂.

- Fuente: metodologías de cálculo de huella de carbono

(GHG Protocol, MyClimate).

- Apoyo a la economía local

- Ejemplo: hospedarse en eco-hotel local → ingresos para

comunidad.

- Hospedarse en cadena internacional → fuga de divisas,

menor beneficio local.

- Fuente: indicadores GSTC sobre impacto económico

local.

- Generación de residuos/impacto en ecosistema

- Ejemplo: senderismo guiado (bajo impacto), mototour

(contaminación acústica, basura, erosión).

- Fuente: PNUMA, guías de turismo sostenible.

# 4. Función de

# utilidad

# (puntajes)

Con esos indicadores se asignó un valor a cada hoja del árbol:

- Muy sostenible (+10) → transporte limpio +

eco-hotel + actividad baja en impacto.

- Medio (+5 a +3) → opciones mixtas (ej: bus +

hotel cadena + senderismo).

- Negativo (–2 a –10) → transporte

contaminante + hotel cadena + actividad de alto impacto. Ejemplo:

- (bus, eco-hotel, senderismo) → +10 (baja

huella, apoya economía local, bajo impacto).

- (avión, hotel cadena, mototour) → –10 (alta

huella, poco apoyo local, alto impacto).

# 5. Aplicación de

# Minimax + alfa-

# beta

- El turista (MAX) buscará la ruta con el

mayor puntaje de sostenibilidad.

- El impacto ambiental (MIN)“recorta” las

opciones que producen más daño.

- La poda alfa-beta permite no evaluar ramas

que ya sabemos que llevan a puntajes muy bajos.

# EJEMPLO

- El viajero empieza en Inicio.

- Puede elegir transporte:bus eléctrico o avión.

- Luego selecciona hospedaje:eco-hotel o hotel de cadena.

- Finalmente, cada ruta lleva a un estado final con un valor de utilidad que combina emisiones de CO₂, costos y

experiencia.

Ejemplo de interpretación: Ir en bus eléctrico → eco-hotel da +85, la mejor opción (alta sostenibilidad, bajo CO₂, buena experiencia). Ir en avión → hotel de cadena da +20, la peor opción (alta huella, poca sostenibilidad).

EJEMPLO

1. Un agente de IA, ¿qué es?

- Es un “ente” que percibe su entorno (entrada, datos, estado

actual) y toma decisiones (acciones) para lograr un objetivo.

- En nuestro caso de turismo:

- Entorno → los destinos, costos, satisfacción de los usuarios.

- Acciones → recomendar un destino, ajustar precios, mostrar

combos.

- Objetivo → maximizar satisfacción del turista y ganancia de la

agencia.

2. Funciones de utilidad → Cómo mide lo que le conviene

- El agente necesita un criterio para valorar cada situación.

- Lafunción de utilidad es esa regla:

- En turismo: Utilidad = Satisfacción del cliente – Costo del

paquete.

- En juegos: +1 si gano, -1 si pierdo.

- Sin utilidad, el agente no puede comparar opciones → se queda

“ciego”.

3. Minimax → Decisión en entornos adversarios

- Cuando hay otro jugador (o factor externo que “compite”), el agente

usa minimax:

- Max: busca la mejor jugada para sí mismo.

- Min: asume que el oponente intentará reducir su utilidad.

- En turismo, el “oponente” podría ser:

- Competencia que baja precios.

- Condiciones externas como clima o presupuesto del turista.

4. Poda Alfa-Beta → Agente más eficiente

- Un agente que explore todo sería lento e ineficiente.

- La poda alfa-beta le permite descartar ramas que seguro no van a

mejorar la decisión final.

- Así:

- Ahorra tiempo.

- Puede analizar más escenarios en el mismo tiempo.

- Ejemplo turismo: si ya encontré un destino barato y muy atractivo, no

necesito analizar en detalle destinos que son mucho más caros y con baja satisfacción.

# En conclusión →

# Todo agente de IA

# aplica esto

Percibir → Evaluar → Decidir → Actuar es el ciclo básico de un agente.

- Función de utilidad = cómo mide el valor de las

opciones.

- Minimax / Alfa-Beta = cómo decide en escenarios

de competencia o limitaciones.

- Esto mismo se aplica en:

- Agentes de recomendación (turismo, Netflix,

Amazon).

- Agentes en videojuegos (enemigos que juegan

contra ti).

- Agentes financieros (decidir inversiones bajo

riesgo).

# ACTIVIDAD 1

- 1) Definir los "Jugadores": Cada grupo debe identificar quién es

MAX y quién es MIN en su contexto. Por ejemplo:

- Salud: MAX es el equipo médico que busca la recuperación

del paciente; MIN es la enfermedad que "responde" al tratamiento.

- Banca: MAX es el banco que busca rentabilidad; MIN es el

riesgo de impago del cliente.

- 2) Crear un Árbol de Decisión: Dibujar un árbol simple con 2 o 3

niveles de decisiones. Por ejemplo, en turismo:

- Nivel 1 (MAX - Turista): Elegir Transporte (Bus Eléctrico vs.

Avión).

- Nivel 2 (MIN - Impacto): El entorno "responde" con un nivel de

huella de carbono.

- Nivel 3 (MAX - Turista): Elegir Alojamiento (Eco-hotel vs. Hotel

de cadena).

- 3) Diseñar la Función de Utilidad: Aquí deben usar los

indicadores del sector. En lugar de +10 o -10, el valor final será una fórmula simple basada en métricas reales.

- Ejemplo en Turismo: Utilidad = (Apoyo local * 5) - (Huella de

CO₂ * 2) - (Generación de residuos * 1). Esto hace el concepto mucho más tangible