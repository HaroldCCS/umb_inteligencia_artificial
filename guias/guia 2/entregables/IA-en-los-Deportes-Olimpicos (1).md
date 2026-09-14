# IA en los Deportes

# Olímpicos

¿Qué pasaría si la IA comete un error crítico?

Análisis de un fallo crítico en un sistema de selección de atletas | A critical failure analysis

SCENARIO

# The Critical Error

### Biased Athlete Selection

A National Olympic Committee deploys an AI system to rank athletes and recommend who advances to Olympic qualification. The model is trained on a decade of historical performance, injury and funding records.

THE FAILURE

### What went wrong

The model produces systematically lower scores for athletes from underfunded regions and programmes.

Access to elite facilities is encoded in the data as if it were athletic potential.

The result is disparate impact: equal talent, unequal recommendation.

Excluded athletes never learn which variables decided their case.

This is not a bug in the code. It is an ethical failure in the design of the system — and it costs an athlete a career, not a metric point.

# ¿Por qué la IA llegó a este error?

Cinco fuentes de sesgo, en orden de aparición

### 1

Sesgo histórico

Los datos reflejan desigualdades reales de inversión y acceso, no capacidad deportiva.

### 2

Sesgo de representación

Ciertos grupos y disciplinas aparecen con muy pocos casos en el entrenamiento.

### 3

Sesgo de variable proxy

Horas de gimnasio o marca del equipamiento funcionan como sustituto encubierto del nivel socioeconómico.

### 4

Sesgo de medición

Sensores y test físicos calibrados sobre poblaciones poco diversas.

### 5

Sesgo de automatización

El evaluador humano tiende a confirmar la recomendación de la máquina.

Resultados discriminat orios

Modelo injusto Datos sesgados

Marco Ético para la IA en Colombia (Presidencia de la República, 2021): propone la herramienta de "limpieza de datos" y el principio de No Discriminación: los datos deben analizarse antes del entrenamiento para identificar y mitigar sesgos.

# The Automated Decision

### Where Judgement Is Transferred

Performance Analysis Normalize and evaluate results

Ranked Shortlist Order candidates by score

Athlete Data Collect bios, metrics, history

Qualification Recommend ation Provide final selection advice

AI Score Generate risk and performance score

Critical point: The ethical problem is not the score. It is the moment the recommendation stops being an input and becomes the verdict.

### Three levels of human control

Colombia's Ethical Framework requires the level of human control to be proportional to the risk. Deciding who competes at the Olympic Games is a high-risk decision — it demands the strongest level, not the cheapest one.

### Human-in-the-loop

A person validates every individual case before it takes effect.

### Human-over-the-loop

A person monitors the system and can intervene or override.

### Human-in-command

A person retains legal and ethical accountability for the outcome.

# ¿Por qué no se detectó el error a tiempo?

### La falla no fue del algoritmo, fue del control

No hubo auditoría de los datos de entrenamiento antes del despliegue.

No se definieron métricas de equidad (paridad demográfica, igualdad de oportunidad) como criterio de aprobación.

El modelo no era explicable: nadie podía reconstruir por qué un atleta bajaba en el ranking.

No existía registro público del algoritmo ni revisión independiente externa.

Los evaluadores confiaron en la recomendación por sesgo de automatización.

Los atletas no tenían un canal real de apelación ni derecho a explicación.

Alta automatización + baja supervisión = fallo invisible hasta que ya es irreversible.

El Marco Ético colombiano contempla el Registro Ético de Algoritmos y la Evaluación de Algoritmos como mecanismos de monitoreo posterior al despliegue.

El CONPES 4144 de 2025 (Política Nacional de Inteligencia Artificial) refuerza la gestión de riesgos y la gobernanza del ciclo de vida de los sistemas de IA.

# Three Ethical Barriers

### From Principle to Mechanism

01

### Human Oversight

Principle: A qualified human panel issues the final qualification decision.

Enforcement: The AI output is recorded as a recommendation with a confidence range; overrides are documented and reviewed.

02

### Data & Bias Auditing

Principle: Training data and model outputs are tested for discrimination before and after deployment.

Enforcement: Pre-deployment fairness testing across protected groups, plus periodic re-auditing and drift monitoring.

03

### Transparency & Right to

### Appeal

Principle: Athletes must understand the criteria and be able to contest them.

Enforcement: Plain-language explanation of decisive variables, a published algorithm registry entry, and an independent appeal body with the power to reverse.

Sport already knows how to do this. The Fujitsu Judging Support System used in artistic gymnastics — including at Paris 2024 — gives judges a 3D-modelled reference, but the human judge still signs the score. AI assists; the human answers for it.

# Árbol de Causa y Consecuencia

BLOQUE 1 — CAUSAS

## 1

### Datos poco diversos

Sesgos históricos incorporados desde el origen.

## 2

### Variables proxy no detectadas

Indicadores socioeconómicos disfrazados de métricas deportivas.

## 3

### Modelo de IA sesgado

Optimiza un patrón injusto a escala.

Fallo crítico: La IA excluye injustamente a atletas calificados.

BLOQUE 3 — CONSECUENCIAS

### Consecuencias individuales

Pérdida irreversible de la oportunidad de competir.

Daño a la carrera deportiva y al proyecto de vida.

Discriminación sin posibilidad de defensa.

### Consecuencias institucionales

Selección olímpica ilegítima y cuestionable.

Pérdida de confianza pública en el comité y en la tecnología.

Exposición a litigios y a sanciones disciplinarias deportivas.

Efecto de retroalimentación: el resultado sesgado se convierte en el dato de entrenamiento del próximo modelo.

El Marco Ético colombiano exige datos representativos y mecanismos activos para identificar y corregir discriminaciones, bajo los principios de No Discriminación e Inclusión.

# Final Reflection — Assistance, Not

# Substitution

# AI should assist sporting

# decisions. It should never absorb

# human responsibility.

### FAIR

Tested for disparate impact before anyone is ranked.

### TRANSPARENT

The criteria are knowable by the person they affect.

### AUDITABLE

Registered, logged and reviewable by an independent party.

### HUMAN-SUPERVISED

A named person is accountable for the final call.

The IOC launched its Olympic AI Agenda in April 2024, positioning AI as a complement to human experience rather than a replacement for it — including AI systems deployed to protect athletes from online abuse.

Conclusion: The goal is not to stop using AI in sport. It is to ensure that when the system is wrong, there is still a human who is answerable — and an athlete who can appeal.