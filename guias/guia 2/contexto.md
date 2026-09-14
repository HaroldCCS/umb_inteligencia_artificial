# Contexto — Guía 2: Ética y riesgos de la IA en el sector

## Qué pide el profesor
`actividad.md` solo dice "revisar recursos". El taller real está en
`recursos/Actividades_Etica_y_Riesgos_IA_por_Sector.md`, que propone **4 actividades** (se elige/combinan):

1. **Juicio ético simulado** — caso ficticio pero realista, con roles (juez, defensa, acusación,
   observador) y veredicto. Entregable: mapa visual.
2. **Mapa de riesgos éticos** (ethical threat modeling) — tabla: componente de IA, riesgo ético,
   personas afectadas, gravedad, mitigación. Categorías mínimas: sesgo, falta de explicabilidad,
   daño social, uso indebido, dependencia excesiva.
3. **"Si la IA se equivoca…"** — peor error ético posible del sector, por qué ocurrió, qué decisión
   automatizada lo causó, por qué no se detectó, y **3 barreras éticas**. Entregable: árbol
   causa–consecuencia.
4. **Canvas ético de IA** — una página con objetivo, beneficiarios, perjudicados, datos sensibles,
   riesgos, nivel de autonomía y punto obligatorio de intervención humana.

## Finalidad dentro del curso
Es la guía **normativa/ética**. Aporta el marco legal colombiano y los criterios de supervisión
humana que deben citarse cuando el agente del parcial "decide" algo que afecta a personas.

## Recursos (lo que hay que saber sin releerlos)
- **`Marco-Etico-IA-Colombia-2021.md`** (Presidencia de la República, 2021) — principios:
  No Discriminación, Inclusión, Transparencia, Responsabilidad. Herramientas concretas:
  **limpieza de datos** antes del entrenamiento, **Registro Ético de Algoritmos**,
  **Evaluación de Algoritmos**, y **niveles de control humano proporcionales al riesgo**
  (*human-in-the-loop*, *human-over-the-loop*, *human-in-command*).
- **`CONPES_GENTE_4144.md`** — CONPES 4144 de 2025, Política Nacional de IA: gestión de riesgos
  y **gobernanza del ciclo de vida** de los sistemas de IA.
- **`articles-425888_recurso_1.md`** — documento largo de política pública de IA (MinTIC). Fuente
  de citas normativas.

## Qué entregamos (`entregables/`)
`IA-en-los-Deportes-Olimpicos (1).md` — se desarrolló la **actividad 3 ("Si la IA se equivoca…")**:

- **Caso:** un Comité Olímpico Nacional usa IA para rankear atletas y recomendar quién clasifica.
- **Fallo:** impacto dispar — puntúa más bajo a atletas de regiones con poca financiación; el
  acceso a instalaciones élite queda codificado como si fuera potencial deportivo.
- **5 sesgos:** histórico, de representación, de variable proxy, de medición, de automatización.
- **Por qué no se detectó:** sin auditoría de datos, sin métricas de equidad, sin explicabilidad,
  sin registro público, sin canal de apelación.
- **3 barreras:** supervisión humana (panel decide, IA solo recomienda), auditoría de datos y
  sesgo (pre y post despliegue), transparencia + derecho de apelación.
- **Árbol causa–consecuencia** con efecto de retroalimentación (el resultado sesgado entrena al
  siguiente modelo).
- Referencias externas usadas: Fujitsu Judging Support System (gimnasia, París 2024) y
  **Olympic AI Agenda** del COI (abril 2024).

## Estado
✅ Desarrollada y entregada (presentación en Gamma, contenido bilingüe ES/EN).

## Para recordar
Frase-tesis del grupo: **"La IA debe asistir las decisiones deportivas, nunca absorber la
responsabilidad humana."** Es el argumento ético que cierra cualquier presentación del curso,
incluido el parcial: el agente táctico **recomienda**, el cuerpo técnico **decide**.
