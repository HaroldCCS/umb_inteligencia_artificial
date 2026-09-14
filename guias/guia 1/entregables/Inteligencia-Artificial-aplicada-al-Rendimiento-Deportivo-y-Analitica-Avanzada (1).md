## Inteligencia Artificial aplicada al Rendimiento Deportivo y Analítica Avanzada

Integrantes: keiry Lucia Olaya Noguera, Harold Stiven Camargo Castellanos, Juan Felipe Coronel Montes

Curso: Inteligencia Artificial


## ¿Cómo se está usando actualmente la IA en este sector?

## Optimización biomecánica y de rendimiento

Seguimiento detallado de movimientos corporales en tiempo real mediante visión por computadora sin necesidad de marcadores físicos.

## Medicina deportiva preventiva

Evaluación continua de la fatiga muscular y carga de trabajo para reducir lesiones antes de que ocurran.

## Estrategia y táctica de juego

Análisis espacio-temporal mediante modelos de predicción de eventos para ajustar formaciones y tácticas en pleno partido.

## Scouting y reclutamiento (Moneyball 2.0)

Identificación de talentos mediante la evaluación automatizada de métricas en ligas globales.

## Experiencia del fanático y arbitraje

Generación de métricas avanzadas durante transmisiones en vivo (como NFL Next Gen Stats o Statcast en la MLB) y asistencia en decisiones arbitrales.


## ¿Qué tipos de tareas se automatizan o mejoran con IA?

| Tarea Nivel de Automatización / Mejora Impacto en el Deporte |   |
| --- | --- |
| Etiquetado de video Automatización alta Reemplaza el trabajo manual de segmentación deportivo de jugadas con algoritmos de detección. Prevención de lesiones Mejora predictiva Correlaciona frecuencia cardíaca, aceleración y |   |
| calidad de sueño para alertar sobre sobrecargas. |   |
| Simulación de escenarios Mejora computacional Modela cambios de alineación, clima o táctica (counterfactual analysis) antes y durante el partido. Monitoreo de carga física Automatización media Transforma variables continuas de sensores inerciales (GPS, IMUs) en mapas de calor de esfuerzo. |   |


## ¿Qué problemas o retos enfrenta la IA en este contexto?

## Calidad y heterogeneidad de datos

Inconsistencia en la captura de métricas entre distintas competencias, ligas y sensores.

## El problema de la muestra pequeña (N reducida)

Los atletas de alto rendimiento son escasos, lo que dificulta el entrenamiento de modelos de Deep Learning profundos sin caer en sobreajuste (overfitting).

## Falta de explicabilidad ("Caja Negra")

Un cuerpo técnico no cambiará su estrategia ni sentará a una figura clave si el modelo no justifica de forma comprensible el porqué de la recomendación.

## Privacidad y propiedad de datos (GDPR / HIPAA)

Debates éticos y legales sobre quién es el dueño de la información fisiológica y biométrica recolectada de los atletas.


## ¿Qué tipo de IA predomina?

## IA Estadística (Dominante)

Algoritmos de aprendizaje supervisado (como Random Forest, XGBoost) y no supervisado (como K-Means), fundamentales para procesar grandes volúmenes de datos numéricos y continuos.

- Random Forest

- K-Means / Clustering

- Redes Neuronales (Extracción de mapas de características)

- Paradigma Híbrido: La combinación de ambos enfoques es indispensable, ya que un modelo estrictamente estadístico puede sugerir decisiones tácticamente inviables si no se filtran mediante las reglas del juego.

## IA Simbólica (Complementaria)

Sistemas basados en reglas que estructuran las normativas tácticas y los modelos de la física del movimiento.

- Reglas oficiales del deporte

- Restricciones de reglamentos y modelos físicos/biomecánicos


## ¿Qué herramientas y tecnologías se utilizan?

## Computer Vision & Tracking

YOLOv8, OpenCV, MediaPipe (para pose estimation y seguimiento espacial de balón y jugadores).

## Modelos Predictivos y de Clustering

Scikit-Learn: Algoritmos clásicos como Random Forest, K- Means, SVM.

XGBoost / LightGBM: Modelos de árboles graduados altamente eficientes para datos tabulares.

## Wearables e IoT

Sensores GPS, unidades de medida inercial (IMUs), monitores de frecuencia cardíaca (marcas como Catapult, Kinexon, Zebra).

## Plataformas Enterprise de Sport Analytics

AWS Sports Analytics (NFL/F1), Stats Perform (Opta), Hudl.

## Mapa Mental del Ecosistema de IA en Deportes

[J](https://gamma.app/?utm_source=made-with-gamma)


## Pregunta Crítica Abierta para Discusión en Clase

"Si un modelo predictivo basado en IA determina que un atleta tiene un 85% de probabilidad de sufrir una lesión si juega un partido decisivo, pero el deportista y el cuerpo técnico deciden ignorar la recomendación y jugar: ¿de quién es la responsabilidad legal y ética si la lesión efectivamente ocurre, y cómo afecta esto a los contratos profesionales impulsados por datos biométricos?"
