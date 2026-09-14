# Contexto — Guía 1: Ecosistema de IA en el sector

> Archivo de contexto para Claude. Resume qué contiene esta guía y para qué sirve,
> para no tener que releer todos los recursos.

## Qué pide el profesor
Formar los grupos definitivos del curso, **elegir un sector** y caracterizar cómo se usa la IA en él:
- ¿Cómo se usa hoy la IA en el sector?
- ¿Qué tareas se automatizan o mejoran?
- ¿Qué problemas/retos enfrenta?
- ¿Qué tipo de IA predomina (simbólica, estadística, híbrida)?
- ¿Qué herramientas/tecnologías se usan?

**Entregables:** presentación, esquema visual / mapa mental del ecosistema, y **1 pregunta crítica abierta** para discutir en clase.

## Finalidad dentro del curso
Es la guía **fundacional**: aquí queda fijado el sector que se usará en TODAS las guías siguientes
y en el parcial. Todo lo demás (grafos, heurísticas, Min-Max, STRIPS, Bayes) se aplica sobre este sector.

## Recursos
Carpeta `recursos/` **vacía**: el profesor no dio material, era investigación libre del grupo.

## Qué entregamos (`entregables/`)
`Inteligencia-Artificial-aplicada-al-Rendimiento-Deportivo-y-Analitica-Avanzada (1).md`

- **Sector elegido: Rendimiento Deportivo y Analítica Avanzada (fútbol profesional).**
- Integrantes: Keiry Lucía Olaya Noguera, Harold Stiven Camargo Castellanos, Juan Felipe Coronel Montes.
- Usos actuales: biomecánica con visión por computador, medicina deportiva preventiva,
  táctica y análisis espacio-temporal, scouting ("Moneyball 2.0"), experiencia del fan y arbitraje.
- Retos: heterogeneidad de datos, muestra pequeña (N reducida de atletas élite), falta de
  explicabilidad ("caja negra"), privacidad de datos biométricos (GDPR/HIPAA).
- Tipo de IA: **estadística dominante** (Random Forest, XGBoost, K-Means, redes neuronales)
  + **simbólica complementaria** (reglas del juego, restricciones físicas) → paradigma **híbrido**.
- Herramientas: YOLOv8, OpenCV, MediaPipe, Scikit-Learn, XGBoost/LightGBM, wearables
  (Catapult, Kinexon, Zebra), AWS Sports Analytics, Stats Perform (Opta), Hudl.
- Pregunta crítica: responsabilidad legal/ética si un atleta juega ignorando una predicción de
  lesión al 85 %.

## Estado
✅ Desarrollada y entregada. El mapa mental se hizo en **Gamma** (gamma.app).

## Para recordar
Este documento es la **fuente de verdad del sector**. Las métricas que aparecen aquí
(riesgo de intercepción por video, carga metabólica por GPS/IMU) son las que se reutilizan como
costos y utilidades en las guías 3, 4, 5, 6 y en el parcial.
