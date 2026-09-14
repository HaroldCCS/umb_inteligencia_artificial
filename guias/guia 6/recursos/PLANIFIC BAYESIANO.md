Búsqueda en juegos (Minimax + alfa-beta)

Planificación (STRIPS, representación de conocimiento)

Incertidumbre y redes bayesianas

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

# Redes

# Bayesianas

# en IA

# Clásica

En IA clásica, el conocimiento se representaba de manera determinista: “Si A, entonces B”.

Sin embargo, en el mundo real hay incertidumbre:

Los sensores pueden fallar.

Los datos pueden estar incompletos o ruidosos.

Para abordar esto, se utilizan modelos probabilísticos.

Uno de los más importantes: Redes Bayesianas.

En la IA clásica, todo era “blanco o negro”: Si tienes gripe → entonces tienes fiebre.

- Pero en la vida real:

- A veces tienes gripe sin fiebre.

- A veces tienes fiebre sin gripe (por otra causa).

- Entonces necesitamos manejar la incertidumbre.

Ahí entran las Redes Bayesianas: son como mapas de causas y efectos, pero con probabilidades.

## ¿Cómo se ven?

Son como un grafo con flechas:

- Los nodos son variables (ej. Gripe, Fiebre, Dolor de cabeza).

- Las flechas significan “influye en”.

Ejemplo: Gripe / \ Fiebre DolorCabeza

- Gripe puede causar Fiebre y Dolor de cabeza.

https://www.youtube.com/watch?v=RvxjyKIKI5s

## El corazón: las Tablas de Probabilidad

## Condicional (CPTs)

- Cada nodo trae consigo una mini-tabla de probabilidades que

responde:

- “Si pasa X, ¿qué tan probable es Y?”

Ejemplo:

- P(Fiebre | Gripe) = 0.9 → si tienes gripe, casi siempre hay fiebre.

- P(Fiebre | ¬Gripe) = 0.1 → si no tienes gripe, rara vez hay fiebre.

- Estas CPTs son lo que hace que la red piense en probabilidades

en lugar de reglas fijas.

## Analogía

- Pensemos en una aplicación de

detectives:

- Cada pista (fiebre, dolor de

cabeza, tos) no asegura nada sola.

- Pero combinadas y con

probabilidades previas, la red te dice qué tan fuerte es la sospecha de “culpable” (la gripe, en este caso).

# ¿Por qué es útil?

Porque en el mundo real:

- Los sensores fallan (un detector de humo puede activarse sin fuego).

- Los datos están incompletos (no siempre sabes todo de un paciente).

- La realidad es incierta .

- Las redes bayesianas permiten razonar aunque falten piezas o haya

ruido en la información. Así que: Una Red Bayesiana es un mapa de variables con flechas y tablas de probabilidadesque te ayuda a responder: “Dada la evidencia, ¿qué tan probable es que ocurra algo?”

# Conceptos

# Clave

Red Bayesiana (RB): Un grafo dirigido acíclico (DAG) que modela dependencias probabilísticas entre variables.

- Elementos principales:

- Nodos → representan variables aleatorias (ej.

Fiebre, Gripe).

- Arcos → representan relaciones de dependencia

probabilística.

- CPT (Tabla de Probabilidades Condicionales) →

define cómo un nodo depende de sus padres.

- Fundamento matemático:

Se basa en el Teorema de Bayes:

- 𝑃 𝐻 ∣ 𝐸 =

𝑃 𝐸∣𝐻 ⋅𝑃 𝐻 𝑃 𝐸

- Donde:

- 𝐻= hipótesis (ej. tener gripe).

- 𝐸= evidencia (ej. tener fiebre y dolor de cabeza).

# ¿Qué significa "definir las CPT"?

Las CPT son las Tablas de Probabilidad Condicional que acompañan a cada nodo en una red bayesiana.

- Cada nodo de la red tiene una probabilidad que depende de sus "padres" (las variables de

las que depende).

- La CPT responde: “¿Qué probabilidad tiene esta variable de tomar cierto valor dado que sus

padres tienen ciertos valores?”. Ejemplo (clima): Nodo = Paraguas. Padre = Lluvia. CPT:

- P(Paraguas=Sí | Lluvia=Sí) = 0.8

- P(Paraguas=Sí | Lluvia=No) = 0.2

- Aquí estamos diciendo:

- Si llueve, hay 80% de probabilidad de que la gente lleve paraguas.

- Si no llueve, igual hay 20% (porque algunos son precavidos o se equivocan).

https://www.youtube.com/watch?v=LhmuUGyzToY

# ¿Cómo aplicarlo en

# distintos sectores?

1. Salud

- Nodo: Enfermedad.

- Hijos: Síntomas.

- CPT: Probabilidades de que un síntoma

aparezca dado que el paciente tenga o no la enfermedad. Ejemplo:

- P(Fiebre=Sí | Gripe=Sí) = 0.8

- P(Fiebre=Sí | Gripe=No) = 0.2

Esto modela que la fiebre es más probable si hay gripe, pero puede aparecer por otras razones.

2. Educación

- Nodo: Estudia.

- Hijos: Aprueba.

- CPT: Probabilidad de aprobar según si

estudia o no. Ejemplo:

- P(Aprueba=Sí | Estudia=Sí) = 0.9

- P(Aprueba=Sí | Estudia=No) = 0.3

Aquí la CPT captura que estudiar aumenta mucho la probabilidad de aprobar.

3. Medio ambiente

- Nodo: Contaminación alta.

- Hijos: Enfermedades respiratorias, Calidad

del aire.

- CPT: Probabilidades de síntomas o impactos

dados los niveles de contaminación. Ejemplo:

- P(Asma=Sí | Contaminación=Alta) = 0.6

- P(Asma=Sí | Contaminación=Baja) = 0.1

Esto refleja el impacto directo de la contaminación en la salud.

Tablas de probabilidad condicionales (CPT):

- P(Gripe):

- P(Gripe = sí) = 0.1

- P(Gripe = no) = 0.9

- P(Fiebre | Gripe):

- P(Fiebre = sí | Gripe = sí) = 0.8

- P(Fiebre = sí | Gripe = no) = 0.2

- P(Dolor | Gripe):

- P(Dolor = sí | Gripe = sí) = 0.7

- P(Dolor = sí | Gripe = no) = 0.3

Pregunta: ¿Cuál es la probabilidad de tener gripe sabiendo que hay fiebre y dolor de cabeza?

- 𝑃 𝐺 ∣ 𝐹 ∧ 𝐷

Ejemplo: Diagnóstico Médico

Variables: 𝐺= Gripe (sí/no). 𝐹= Fiebre (sí/no). 𝐷= Dolor de cabeza (sí/no). Dependencias: Fiebre depende de Gripe. Dolor de cabeza depende de Gripe.

Resolución Paso a Paso Aplicamos Bayes:

- 𝑃 𝐺 ∣ 𝐹𝐷 =

𝑃 𝐹 𝐷 ∣ 𝐺 ⋅𝑃 𝐺 𝑃 𝐹 𝐷 Numerador:

- 𝑃 𝐹 𝐷 ∣ 𝐺 = 𝑃 𝐹 ∣ 𝐺 ⋅ 𝑃 𝐷 ∣ 𝐺 (

independencia condicional en la red).

- Para 𝐺 = 𝑠ı

ˊ :0.8 ⋅ 0.7 = 0.56.

- Multiplicamos por 𝑃 𝐺 = 𝑠ı

ˊ = 0.1: →0.056.

- Para 𝐺 = 𝑛𝑜: 0.2 ⋅ 0.3 = 0.06.

- Multiplicamos por 𝑃 𝐺 = 𝑛𝑜 = 0.9:

→0.054. Denominador:

- 𝑃 𝐹 𝐷 = 0.056 + 0.054 = 0.11

- Resultado:

- 𝑃 𝐺 = 𝑠ı

ˊ ∣ 𝐹𝐷 =

0. 056

0. 11

≈ 0.509 Con fiebre y dolor de cabeza, la probabilidad de tener gripe es ~51%.

Resolución Paso a Paso

- Aplicamos Bayes:

- 𝑃 𝐺 ∣ 𝐹𝐷 =

𝑃 𝐹 𝐷 ∣ 𝐺 ⋅𝑃 𝐺 𝑃 𝐹 𝐷

- Numerador:

- 𝑃 𝐹 𝐷 ∣ 𝐺 = 𝑃 𝐹 ∣ 𝐺 ⋅ 𝑃 𝐷 ∣ 𝐺 (

independencia condicional en la red).

- Para 𝐺 = 𝑠ı

ˊ :0.8 ⋅ 0.7 = 0.56.

- Multiplicamos por 𝑃 𝐺 = 𝑠ı

ˊ = 0.1: →0.056.

- Para 𝐺 = 𝑛𝑜: 0.2 ⋅ 0.3 = 0.06.

- Multiplicamos por 𝑃 𝐺 = 𝑛𝑜 = 0.9:

→0.054.

- Denominador:

- 𝑃 𝐹 𝐷 = 0.056 + 0.054 = 0.11

- Resultado:

- 𝑃 𝐺 = 𝑠ı

ˊ ∣ 𝐹𝐷 =

0. 056

0. 11

≈ 0.509 Con fiebre y dolor de cabeza, la probabilidad de tener gripe es ~51%.

### Es como decir:

### •“Si hay fiebre y dolor, hay dos posibles

### explicaciones: gripe o no gripe.”

### •“Pesamos cuál de esas explicaciones es

### más probable según los datos.”

### •“Al final, con esa evidencia, la gripe pasa de

### ser 10% (probabilidad inicial) a un 51%

### (probabilidad actualizada).”

## Ejemplo 1:

## Diagnóstico

## médico

- Variables:

- 𝐺= Gripe (sí/no)

- 𝐹= Fiebre (sí/no)

- 𝐷= Dolor de cabeza (sí/no)

- Pregunta: ¿Cuál es la probabilidad de

tener gripe si el paciente presenta fiebre y dolor de cabeza?

- Resultado: ~51%

Variables: G = Gripe (sí/no) F = Fiebre (sí/no) D = Dolor de cabeza (sí/no) CPTs (ejemplo): P(G=Sí) = 0.1 → P(G=No) = 0.9 P(F=Sí | G=Sí) = 0.8; P(F=Sí | G=No) = 0.2 P(D=Sí | G=Sí) = 0.7; P(D=Sí | G=No) = 0.3 Queremos: P(G=Sí | F=Sí ∧ D=Sí)

- Paso 1 — Numerador

𝑃 𝐹 𝐷 ∣ 𝐺 = Sı ˊ ⋅ 𝑃 𝐺 = Sı ˊ

=𝑃 𝐹 ∣ 𝐺 = Sı ˊ ⋅ 𝑃 𝐷 ∣ 𝐺 = Sı ˊ ⋅ 𝑃 𝐺 = Sı ˊ (independencia condicional)

- Cálculo dígito a dígito:

- 𝑃 𝐹 ∣ 𝐺 = Sı

ˊ = 0.8

- 𝑃 𝐷 ∣ 𝐺 = Sı

ˊ = 0.7 Multiplicación: 0.8 × 0.7 = 0.56. Multiplicamos por el prior: 0.56 × 0.1 = 0.056.

- Paso 2 — Contribución de G=No

𝑃 𝐹 𝐷 ∣ 𝐺 = No ⋅ 𝑃 𝐺 = No =0.2 × 0.3 × 0.9 Primero 0.2 × 0.3 = 0.06. Luego 0.06 × 0.9 = 0.054.

- Paso 3 — Denominador

𝑃 𝐹 𝐷 = 0.056 + 0.054 = 0.110

- Paso 4 — Resultado

𝑃 𝐺 = Sı ˊ ∣ 𝐹𝐷 = 0.056/0.110 División: 0.056/0.110 ≈ 0.5090909

- Respuesta: ≈ 0.5091 → ~50.9%

# Ejemplo 2:

# Clima y

# paraguas

- Variables:

- 𝐿= Lluvia (sí/no)

- 𝑁= Nubes (sí/no)

- 𝑃= Llevar paraguas (sí/no)

- Dependencias:

- Lluvia causa Nubes.

- Lluvia influye en si llevas paraguas.

- Ejercicio para estudiantes:

- Dar probabilidades:

- P(Lluvia = sí) = 0.3

- P(Nubes = sí | Lluvia = sí) = 0.9

- P(Nubes = sí | Lluvia = no) = 0.4

- P(Paraguas = sí | Lluvia = sí) = 0.8

- P(Paraguas = sí | Lluvia = no) = 0.2

Pregunta: Si ves a alguien con paraguas, ¿cuál es la probabilidad de que esté lloviendo? Se calcula con Bayes, igual que en el ejemplo médico.

Variables: L = Lluvia (sí/no) P = Llevar paraguas (sí/no) CPTs: P(L=Sí) =0.3 → P(L=No)=0.7 P(P=Sí | L=Sí) = 0.8 P(P=Sí | L=No) = 0.2

- Queremos: P(L=Sí | P=Sí) — si ves a alguien con paraguas, ¿está lloviendo?

- Paso 1 — Numerador

𝑃 𝑃 = 𝑆ı ˊ ∣ 𝐿 = 𝑆ı ˊ ⋅ 𝑃 𝐿 = 𝑆ı ˊ = 0.8 × 0.3

0. 8 × 0.3 = 0.24

- Paso 2 — Contribución L=No

𝑃 𝑃 = 𝑆ı ˊ ∣ 𝐿 = 𝑁𝑜 ⋅ 𝑃 𝐿 = 𝑁𝑜 = 0.2 × 0.7

0. 2 × 0.7 = 0.14

- Paso 3 — Denominador

𝑃 𝑃 = 𝑆ı ˊ = 0.24 + 0.14 = 0.38

- Paso 4 — Resultado

𝑃 𝐿 = 𝑆ı ˊ ∣ 𝑃 = 𝑆ı ˊ = 0.24/0.38 División: 0.24/0.38 = 24/38 = 12/19 ≈ 0.6315789

- Respuesta: ≈ 0.6316 → ~63.16%

# Ejemplo 3:

# Detección

# de fraude

# bancario

Variables:

- 𝐹= Fraude (sí/no)

- 𝑇= Transacción grande (sí/no)

- 𝐸= Transacción desde el extranjero (sí/no)

Dependencias:

- Fraude influye en si la transacción es grande.

- Fraude influye en si ocurre en el extranjero.

Probabilidades de ejemplo:

- P(Fraude = sí) = 0.02

- P(T = sí | Fraude = sí) = 0.8

- P(T = sí | Fraude = no) = 0.1

- P(E = sí | Fraude = sí) = 0.7

- P(E = sí | Fraude = no) = 0.05

Pregunta: Si una transacción es grande y desde el extranjero, ¿cuál es la probabilidad de que sea fraude?

Variables: F = Fraude (sí/no) T = Transacción grande (sí/no) E = Transacción desde el extranjero (sí/no) CPTs (ejemplo): P(F=Sí) = 0.02 → P(F=No)=0.98 P(T=Sí | F=Sí) = 0.8; P(T=Sí | F=No)=0.1 P(E=Sí | F=Sí) = 0.7; P(E=Sí | F=No)=0.05

- Queremos: P(F=Sí | T=Sí ∧ E=Sí)

- Asunción: T y E son condicionalmente independientes dado F.

- Paso 1 — Numerador (F=Sí)

𝑃 𝑇 𝐸 ∣ 𝐹 = Sı ˊ ⋅ 𝑃 𝐹 = Sı ˊ

=𝑃 𝑇 ∣ 𝐹 = Sı ˊ ⋅ 𝑃 𝐸 ∣ 𝐹 = Sı ˊ ⋅ 𝑃 𝐹 = Sı ˊ

=0.8 × 0.7 × 0.02

- Cálculos:

- 0.8 × 0.7 = 0.56

- 0.56 × 0.02 = 0.0112

Paso 2 — Numerador (F=No)

0. 1 × 0.05 × 0.98

- 0.1 × 0.05 = 0.005

- 0.005 × 0.98 = 0.0049

- Paso 3 — Denominador

0. 0112 + 0.0049 = 0.0161

- Paso 4 — Resultado

𝑃 𝐹 = Sı ˊ ∣ 𝑇𝐸 = 0.0112/0.0161 Convertimos a fracción: 0.0112/0.0161 = 112/161 ≈ 0.69565217

- Respuesta: ≈ 0.6957 → ~69.57%

## Ejemplo 4:

## Mecánica de

## un coche

Variables:

- 𝐵= Batería descargada (sí/no)

- 𝐶= Coche no arranca (sí/no)

- 𝐿= Luces no prenden (sí/no)

Dependencias:

- Si la batería está descargada → el coche no

arranca y las luces no prenden. Pregunta: Si el coche no arranca y las luces no prenden, ¿cuál es la probabilidad de que la batería esté descargada?

- Variables:

B = Batería descargada (sí/no) C = Coche no arranca (sí/no) L = Luces no prenden (sí/no)

- CPTs (ejemplo):

P(B=Sí) = 0.10 → P(B=No)=0.90 P(C=Sí | B=Sí) = 0.9; P(C=Sí | B=No) = 0.1 P(L=Sí | B=Sí) = 0.85; P(L=Sí | B=No) = 0.05

- Queremos: P(B=Sí | C=Sí ∧ L=Sí) — si no arranca y las luces no prenden, ¿es la

batería?

- Paso 1 — Numerador (B=Sí)

0. 9 × 0.85 × 0.10

- 0.9 × 0.85 = 0.765

- 0.765 × 0.10 = 0.0765

- Paso 2 — Contribución (B=No)

0. 1 × 0.05 × 0.90

- 0.1 × 0.05 = 0.005

- 0.005 × 0.90 = 0.0045

- Paso 3 — Denominador

0. 0765 + 0.0045 = 0.0810

- Paso 4 — Resultado

𝑃 𝐵 = 𝑆ı ˊ ∣ 𝐶𝐿 = 0.0765/0.0810 División: 0.0765/0.0810 = 765/810 = 153/162 ≈ 0.9444444

- Respuesta: ≈ 0.9444 → ~94.44%

# TIPOS RAZONAMIENTO

Razonamiento Causal (Predicción)

Razonamiento Diagnóstico

Razonamiento Intercausal (Explaining Away)

1. Razonamiento Causal (Predicción)

- Es el razonamiento "hacia adelante" (top-down). Va desde las causas

hacia los efectos. En una Red Bayesiana, esto sigue la dirección de las flechas.

- Lógica: Si sabemos que la causa ha ocurrido, ¿qué tan probable es

que veamos el efecto?

- Utilidad: Sirve para hacer predicciones o simulaciones de escenarios.

- Ejemplo: Si un grupo está trabajando en un sector de Mantenimiento

Industrial, el razonamiento causal sería: "Si sabemos que la máquina tiene 10 años de uso (Causa), ¿cuál es la probabilidad de que falle mañana (Efecto)?".

- Matemáticamente: Se calcula como P(Efecto∣Causa).

2. Razonamiento Diagnóstico

- Es el razonamiento "hacia atrás" (bottom-up). Va desde los efectos

observados hacia las causas probables. Va en sentido contrario a las flechas.

- Lógica: Si observamos un síntoma o evidencia, ¿cuál es la causa más

probable que lo originó?

- Utilidad: Es el corazón de los sistemas de diagnóstico (médico,

técnico, financiero).

- Ejemplo: En un sector de Ciberseguridad, si se observa un tráfico de

red inusualmente alto (Efecto/Evidencia), el razonamiento diagnóstico sería: "¿Cuál es la probabilidad de que esto sea un ataque DDoS (Causa)?".

- Matemáticamente: Se usa el Teorema de Bayes para obtener

P(Causa∣Evidencia).

3. Razonamiento Intercausal (Explaining Away)

- Este es el más interesante y "humano" de los tres. Ocurre cuando un efecto tiene

dos o más causas posibles que compiten entre sí.

- El concepto: Cuando confirmas una de las causas, la probabilidad de la otra causa

disminuye automáticamente. Una causa "explica y descarta" (explains away) a la otra.

- Por qué es útil para tus grupos: Les ayuda a entender cómo un sistema inteligente

descarta hipótesis falsas cuando encuentra una explicación suficiente.

- Ejemplo Detallado:

- Imagina que el efecto es "La alarma de un banco suena".

- Hay dos causas posibles: "Intento de Robo" o "Fallo del Sensor".

- Si la alarma suena, la probabilidad de ambas causas sube.

- Pero, si el guardia revisa la bitácora y ve que el sensor tiene un reporte de error técnico

(confirmamos "Fallo del Sensor"), la probabilidad de "Intento de Robo" baja drásticamente. El fallo técnico ha "explicado" por qué suena la alarma, descartando la otra hipótesis.

Tipo de Razonamiento Dirección Pregunta Clave

Causal ↓ (Causa a Efecto( "Si pasa esto, ¿qué pasará?"

Diagnóstico ↑ (Efecto a Causa( "Si vi esto, ¿qué lo causó?"

Intercausal (Entre Causas) "¿Esta evidencia descarta la otra posibilidad?"

### Caso de Turismo

Para el sector turismo: un grupo está analizando por qué un[Tour a Monserrate] (Efecto) tiene una [Baja Reserva]. Las causas pueden ser [Clima Lluvioso] o [Subida de Precios].

A. Razonamiento Causal (Hacia adelante)

- Escenario: La agencia ve el pronóstico del tiempo y sabe que mañana

habrá Tormenta Eléctrica (Causa).

- Razonamiento: "Como va a llover, la probabilidad de que las reservas

del tour de mañana caigan es del 90%".

- Uso: Sirve para que la agencia se prepare y ofrezca una alternativa bajo

techo proactivamente.

Razonamiento Diagnóstico (Hacia atrás)

- Escenario: La agencia nota que hoy hubo Muy Pocas Reservas

(Efecto/Evidencia).

- Razonamiento: "¿Por qué no vendimos? ¿Será que el precio está

muy alto para el mercado o será que el clima desmotivó a la gente?".

- Uso: Ayuda a entender el origen de un problema de negocio ya

ocurrido.

Razonamiento Intercausal (Descarte)

- Escenario: Tenemos Pocas Reservas. El gerente está

preocupado pensando que el nuevo Aumento de Precios espantó a los clientes.

- Evidencia nueva: De repente, ven las noticias y muestran que

hubo un Cierre de la Vía por un derrumbe debido a lluvias fuertes.

- Razonamiento: "Ah, el cierre de la vía explica por qué no hay

gente. Entonces, es probable que nuestro aumento de precios no sea el culpable principal". La causa "Cierre de vía" explica la baja demanda y quita peso a la hipótesis del "Precio alto".

CASO SECTOR

3 CPTs del modelo:

1. P(Clima)

2. P(Transporte | Clima)

3. P(Actividad | Clima, Transporte)

1. Distribución inicial (no depende de nadie)

CPT trivial porque solo depende de sí misma: Interpreta: P(Clima = Malo) = 0.3, P(Clima = Bueno) = 0.7

2. Transporte condicionado al Clima

CPT de Transporte:

- Si Clima = Malo: P(Difícil)=0.6, P(Fácil)=0.4

- Si Clima = Bueno: P(Difícil)=0.2, P(Fácil)=0.8

Esto es justo una tabla de probabilidad condicional (CPT): P(Transporte | Clima).

3. Actividad condicionada a Clima y Transporte

Este es el CPT de Actividad: Clima=Malo, Transporte=Difícil → P(No divertida)=0.9, P(Divertida)=0.1 Clima=Malo, Transporte=Fácil → P(No divertida)=0.6, P(Divertida)=0.4 Clima=Bueno, Transporte=Difícil → P(No divertida)=0.5, P(Divertida)=0.5 Clima=Bueno, Transporte=Fácil → P(No divertida)=0.1, P(Divertida)=0.9 Esto es la tabla P(Actividad | Clima, Transporte).

Pregunta: 𝑃 Actividad = Divertida | Clima = Bueno

Paso 1. Fórmula de Bayes

𝑃 𝐴 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 𝑃 𝐶 = 𝐵𝑢𝑒𝑛𝑜 ∣ 𝐴 ⋅ 𝑃 𝐴 𝑃 𝐶 = 𝐵𝑢𝑒𝑛𝑜 Pero en una red bayesiana es más cómodo usar la regla de la probabilidad total, porque ya tenemos las CPTs.

Paso 2. Usando las CPTs

𝑃 𝐴 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = ෍ 𝑇 𝑃 𝐴 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 ⋅ 𝑃 𝑇 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜

Paso 3. Sustitución De nuestras tablas:

- P(Transporte | Clima=Bueno) = [Difícil=0.2, Fácil=0.8]

- P(Actividad | Clima=Bueno, Transporte=Difícil) = [No=0.5, Sí=0.5]

- P(Actividad | Clima=Bueno, Transporte=Fácil) = [No=0.1, Sí=0.9]

Entonces: 𝑃 𝐴 = Divertida ∣ 𝐶 = Bueno = 0.5 0.2 + 0.9 0.8 = 0.1 + 0.72 = 0.82 Y lo mismo para No divertida (queda 0.18).

¿Dónde entra Bayes?

- La red guarda CPTs (condicionales), que son expresiones

de Bayes.

- Cada consulta 𝑃 𝐻 ∣ 𝐸 se resuelve aplicando

repetidamente la regla de Bayes y la probabilidad total.

- Lo que hicimos manualmente con los for en el código es

en realidad desplegar la fórmula de Bayes.

En resumen:

- Cuando preguntas por una probabilidad condicional con

evidencia, como 𝑃 𝐴 ∣ 𝐶,estás aplicando el Teorema de Bayes.

- Aquí esta usando las tablas y sumando sobre las variables

ocultas (transporte).

Interpretación de resultados

1. Distribución marginal P(Actividad):

1. No divertida = 0.36 (36%)

2. Divertida = 0.64 (64%)

2. Si no sabemos nada sobre el clima ni transporte, hay un

64% de probabilidad de que la actividad sea divertida. Esto es la visión global del modelo. 2.

3. Distribución condicional P(Actividad | Clima=Bueno):

2. No divertida = 0.18 (18%)

3. Divertida = 0.82 (82%)

4. Cuando el clima es bueno, la probabilidad de que la

actividad sea divertida sube mucho (del 64% al 82%). Esto muestra cómo la evidencia cambia nuestra creencia: un día soleado hace que casi siempre la actividad turística sea positiva.

Guía paso a paso: Redes Bayesianas en Turismo

1. Identificar las CPTs (tablas de probabilidad condicional)

- Clima (C):

- 𝑃 𝐶 = 𝑀𝑎𝑙𝑜 = 0.3,𝑃 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.7

- Transporte (T) | Clima:

- 𝑃 𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝑀𝑎𝑙𝑜 = 0.6,𝑃 𝑇 = 𝐹𝑎 ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝑀𝑎𝑙𝑜 = 0.4

- 𝑃 𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.2,𝑃 𝑇 = 𝐹𝑎 ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.8

- Actividad (A) | Clima, Transporte:

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝑀𝑎𝑙𝑜𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙 = 0.1,𝑃 𝐴 = 𝑁𝑜 ∣ 𝐶 = 𝑀𝑎𝑙𝑜𝑇 = 𝐷𝑖𝑓ı ˊ 𝑐𝑖𝑙 = 0.9

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝑀𝑎𝑙𝑜𝑇 = 𝐹𝑎

ˊ 𝑐𝑖𝑙 = 0.4,𝑃 𝐴 = 𝑁𝑜 ∣ 𝐶 = 𝑀𝑎𝑙𝑜𝑇 = 𝐹𝑎 ˊ 𝑐𝑖𝑙 = 0.6

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙 = 0.5,𝑃 𝐴 = 𝑁𝑜 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐷𝑖𝑓ı ˊ 𝑐𝑖𝑙 = 0.5

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐹𝑎

ˊ 𝑐𝑖𝑙 = 0.9,𝑃 𝐴 = 𝑁𝑜 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐹𝑎 ˊ 𝑐𝑖𝑙 = 0.1

2. Fórmula de probabilidad condicional (Bayes)

- Queremos:

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜

- Por la regla de la probabilidad total:

- 𝑃 𝐴 ∣ 𝐶 = σ𝑇 𝑃 𝐴 ∣ 𝐶𝑇 ⋅ 𝑃 𝑇 ∣ 𝐶

•

3. Sustitución con los valores

- Para 𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙:

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐷𝑖𝑓ı

ˊ 𝑐𝑖𝑙 ⋅ 𝑃 𝑇 = 𝐷𝑖𝑓ı ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.5 ⋅ 0.2 = 0.1

- Para 𝑇 = 𝐹𝑎

ˊ 𝑐𝑖𝑙:

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜𝑇 = 𝐹𝑎

ˊ 𝑐𝑖𝑙 ⋅ 𝑃 𝑇 = 𝐹𝑎 ˊ 𝑐𝑖𝑙 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.9 ⋅ 0.8 = 0.72

4. Resultado final

- 𝑃 𝐴 = 𝐷𝑖𝑣𝑒𝑟𝑡𝑖𝑑𝑎 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 0.1 + 0.72 = 0.82

Y para completar:

- 𝑃 𝐴 = 𝑁𝑜 ∣ 𝐶 = 𝐵𝑢𝑒𝑛𝑜 = 1 − 0.82 = 0.18

Interpretación

- Si no sabemos nada, la actividad es divertida en un 64% de los casos

(resultado marginal).

- Si sabemos que el clima es bueno, la probabilidad sube a 82%.

- Esto muestra cómo la evidencia cambia nuestra creencia → ¡eso es el

Teorema de Bayes en acción!

## Relevancia de las

## Redes Bayesianas

## en Agentes de IA

IA ≠ todo es seguro, siempre hay incertidumbre

- STRIPS planifica pasos, pero asume

que todo es determinista (si digo“ir al museo”, llego siempre).

- Minimax decide la mejor jugada, pero

también supone que el rival jugará siempre de forma óptima.

- En el mundo real, no todo es 100%

seguro: puede llover, fallar un transporte, o un cliente cambiar de opinión.

- Ahí entran las Bayesianas: permiten

que el agente razone en escenarios inciertos.

# Relevancia de las

# Redes Bayesianas

# en Agentes de IA

- Probabilidades como creencias del

agente

- El agente no sabe con certeza si habrá tráfico,

pero cree que hay un 70% de probabilidad.

- Estas creencias se actualizan cuando

aparece evidencia nueva.

- Así, el agente no se queda estático, sino que

va aprendiendo sobre la marcha.

- Uso en la práctica de los agentes

- Diagnóstico:“¿Qué tan probable es que un

turista disfrute el viaje si está lloviendo?”

- Predicción:“Si hay muchas reservas, ¿qué

probabilidad hay de que el hotel se llene?”

- Decisión bajo incertidumbre: combina con

utilidades → el agente no solo predice, también elige la mejor acción dado el riesgo.

# Relevancia de las

# Redes Bayesianas

# en Agentes de IA

Comparación con STRIPS y Minimax

- STRIPS = planificación determinista.

- Minimax = decisión en entornos competitivos.

- Bayes = razonamiento probabilístico en entornos

inciertos. Un agente real necesita las tres cosas: planificar, decidir y adaptarse a la incertidumbre. •

### Ejemplo turístico simplificado

- Variable:“Clima”(Soleado/Lluvia).

- Variable:“Actividad”(Excursión/Hotel).

- Red Bayesiana:

- Si hace sol → excursión probable.

- Si llueve → excursión baja, hotel alta.

- El agente usa Bayes:

- Antes de viajar:“50% sol, 50% lluvia”.

- Recibe evidencia:“Predicción del clima: 80%

sol”.

- Actualiza: ahora cree que la excursión es más

recomendable.

### Relevancia de las

### Redes Bayesianas

### en Agentes de IA

- STRIPS: el agente planifica como si

todo fuera seguro.

- Minimax: el agente decide en un

entorno de competencia.

- Bayesiano: el agente razona con

probabilidades, como lo haría un humano frente a la duda. Juntos, cubren: planificación + decisión estratégica + razonamiento en incertidumbre, los tres pilares de un agente más “inteligente”.

Enfoque / Método Tipo de Razonamiento Supuesto del Mundo Ejemplo Turístico Limitación Relevancia en IA

STRIPS (Planificación)

Determinista → plan paso a paso

Todo ocurre como se planifica (sin fallos)

Planear: “Ir al museo → luego al restaurante → después al hotel”

No maneja cambios inesperados (lluvia, tráfico)

Base para la planificación automática en agentes

Minimax (Decisión en juegos)

Competitivo → mejor jugada contra oponente

El rival siempre juega lo mejor posible

Elegir la mejor ruta turística compitiendo con otra agencia

Supone rival “perfecto”, no hay incertidumbre de azar

Base de la toma de decisiones estratégica

Redes Bayesianas (Razonamiento Probabilístico)

Probabilístico → creencias y actualización con evidencia

El mundo es incierto, todo tiene probabilidad

“Si llueve (30%), es mejor quedarse en el hotel; si hace sol (70%), excursión”

Requiere datos probabilísticos y puede ser costoso

Base del razonamiento bajo incertidumbre en IA

# ACTIVIDAD

1. Construcción de la red

Cada grupo debe: Identificar tres variables principales que afectan un resultado en su contexto. Dibujar la red bayesiana indicando las dependencias entre esas variables. Definir las probabilidades previas y condicionales (CPTs).

2. Probabilidad conjunta

Calcular la probabilidad conjunta de un escenario específico, por ejemplo: 𝑃 𝑋 = positivo 𝑌 = favorable 𝑍 = e ˊ xito Interpretar qué significa ese resultado en su contexto.

3. Inferencia con evidencia parcial

Calcular la probabilidad de un evento final dado un factor conocido, por ejemplo: 𝑃 Resultado ∣ 𝑋 = favorable Explicar cómo cambia la expectativa al conocer la evidencia.