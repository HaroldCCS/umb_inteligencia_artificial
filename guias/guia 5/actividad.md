(no buscar en internet los links en esta actividad, los pdf estan en la carpeta "recursos")

Aplicando Min_Max:

  1)  Definir los "Jugadores": Cada grupo debe identificar quién es MAX y quién es MIN en su contexto. Por ejemplo:  
    Salud: MAX es el equipo médico que busca la recuperación del paciente; MIN es la enfermedad que "responde" al tratamiento.  
Banca: MAX es el banco que busca rentabilidad; MIN es el riesgo de impago del cliente.

2) Crear un Árbol de Decisión: Dibujar un árbol simple con 2 o 3 niveles de decisiones. Por ejemplo, en turismo:  
 Nivel 1 (MAX - Turista): Elegir Transporte (Bus Eléctrico vs. Avión).  
Nivel 2 (MIN - Impacto): El entorno "responde" con un nivel de huella de carbono.  
 Nivel 3 (MAX - Turista): Elegir Alojamiento (Eco-hotel vs. Hotel de cadena).

3) Diseñar la Función de Utilidad: Aquí deben usar los indicadores del sector. En lugar de +10 o -10, el valor final será una fórmula simple basada en métricas reales.

    Ejemplo en Turismo: Utilidad = (Apoyo local * 5) - (Huella de CO₂ * 2) - (Generación de residuos * 1). Esto hace el concepto mucho más tangible

[PLANIFICACION-MAX MIN.pdf](https://umb.instructure.com/courses/81693/files/16078753?wrap=1 "PLANIFICACION-MAX MIN.pdf")[Download PLANIFICACION-MAX MIN.pdf](https://umb.instructure.com/courses/81693/files/16078753/download?download_frd=1)

**Aplicar Strips:**  
  
  
Diseñar y validar un plan de acciones para un problema de su sector, comparando la lógica de "empuje" (forward) con la de "atracción" (backward).1. Construcción del Plan Maestro  
Cada grupo debe definir su **Estado Inicial** y su **Estado Meta**. A partir de ahí, deben desarrollar el plan en dos direcciones:

- **Fase A (Búsqueda Forward):** "Si estoy aquí, ¿qué puedo hacer?".
- Partiendo del estado inicial, listen las acciones en orden cronológico (Op1​,Op2​...).
- Justifiquen cada paso: "¿Se cumplen las precondiciones con lo que tengo en este momento?".

**Fase B (Búsqueda Backward / Regresión de Metas):** "Para lograr esto, ¿qué debió pasar antes?".

- Empiecen por la Meta. Busquen la acción cuyo efecto **ADD** coincida con la meta.
- Identifiquen las precondiciones de esa acción; ahora esas son sus "sub-metas".
- Repitan el proceso hacia atrás hasta llegar a las condiciones del estado inicial.

2. Detección de Bloqueos e Interferencias  
Revisen ambos caminos (Forward y Backward) para encontrar errores:

- **Inconsistencia:** ¿Hay alguna acción en el camino _forward_ que borre (DELETE) algo que la búsqueda _backward_ identificó como necesario para el paso final? (Aquí detectarían una posible **Anomalía de Sussman**).
- **Acciones Huérfanas:** ¿Hay alguna acción en su plan que no aporta nada a los efectos necesarios para la meta?

3. Visualización en Grafo Espejo  
Dibujen un diagrama que muestre los estados, pero marquen la dirección del pensamiento:

- **Nodos:** Representan los estados (conjunto de predicados).
- **Aristas (Flechas):** Representan las acciones.
- **Instrucción:** Usen flechas de un color (ej. Azul) para el camino que trazaron desde el inicio, y flechas de otro color (ej. Rojo) para el razonamiento que hicieron desde la meta. El punto donde ambos colores se encuentran es la confirmación de que el plan es sólido.

[Planificación STRIPS.pdf](https://umb.instructure.com/courses/81693/files/16079227?wrap=1 "Planificación STRIPS.pdf")[Download Planificación STRIPS.pdf](https://umb.instructure.com/courses/81693/files/16079227/download?download_frd=1)