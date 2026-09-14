# Decisiones y respuestas registradas

> Bitácora de lo que Harold (o el grupo) ya respondió. **Cuando una pregunta de `preguntas.md` se
> resuelve, se borra de allí y se anota aquí**, para no volver a preguntar lo mismo.

## Organización del vault

| Fecha | Tema | Decisión | Notas |
|---|---|---|---|
| 2026-09-14 | Estructura | Cada guía lleva `contexto.md`; las no desarrolladas llevan `planeacion.md`; las dudas van a `preguntas.md` en la raíz; lo transversal va a `proyecto/` | Instrucción inicial de Harold |
| 2026-09-14 | Fuentes | Priorizar **siempre** los recursos del profesor sobre material externo, para no desviarse en la sustentación | Instrucción inicial de Harold |
| 2026-09-14 | Alcance | No desarrollar entregables todavía; solo contexto y planeación | Instrucción inicial de Harold |

## Decisiones del curso

### 📅 Fecha de entrega del parcial práctico 1 — **jueves 17 de septiembre de 2026**
*(respondido 2026-09-14)*
Con el plan hecho el lunes 14, quedan **3 días efectivos**. El cronograma está en
`guias/parcial practico 1/planeacion.md` §7, con el orden de recorte si el tiempo se acorta.

### ✅ Guía 5 — sí está completa (entregable actualizado)
*(verificado 2026-09-14)*
El entregable es `Algoritmo_Rendimiento_deportivo.ipynb` (reemplazó al notebook de huella de
carbono). Contiene Min-Max + poda α-β y STRIPS forward/backward con detección de bloqueos.
**No hay que construir esos dos métodos desde cero en el parcial**: se portan y se corrigen.
Deuda técnica concreta listada en `guias/guia 5/contexto.md`.

### ⚠️ El proyecto tiene DOS dominios
*(derivado de lo anterior, 2026-09-14)*
- **Dominio A — red de pases** (guías 3 y 4): búsqueda y heurísticas sobre la jugada POR→DL.
- **Dominio B — gestión de carga del atleta** (guías 5, 6 y parcial): Min-Max, STRIPS, Bayes.

**El parcial se construye sobre el Dominio B.** El Dominio A se menciona como antecedente pero
**no se integra** — no hay tiempo y confundiría la exposición.
Detalle en `proyecto/proyecto.md` §3.

### ✅ Se mantiene la huella de carbono metabólica (λ)
*(respondido 2026-09-14: "siempre y cuando no genere problemas/confusiones")*
**Se mantiene, y sin riesgo de confusión**, porque en la guía 5 el CO₂ ya no es un añadido sino
parte estructural del modelo:
- en Min-Max es un término de la función de utilidad (`− CO₂ × 2·λ`);
- en STRIPS es una **precondición lógica**: `co2_acumulado(alto)` bloquea el entrenamiento de alta
  intensidad hasta que se reduce. Es lo que fuerza el orden del plan.

**Condición para que siga sin confundir:** presentarlo siempre como **carga metabólica del atleta
medida por GPS/IMU**, nunca como "huella ambiental del equipo". Son cosas distintas y mezclarlas es
lo único que puede generar preguntas incómodas en la sustentación.

### ✅ Red bayesiana — variables elegidas y CONSTRUIDA
*(propuesta y desarrollada 2026-09-14)*
`C` = Carga semanal → `F` = Fatiga → `E` = Éxito competitivo. Son **las mismas variables de los
niveles 1 y 2 del árbol Min-Max**, para que los tres métodos hablen del mismo mundo.
CPTs y resultados verificados en `guias/guia 6/planeacion.md`.

### 📄 Formato de entregables: notebook + explicación en .md
*(instrucción de Harold, 2026-09-14)*
Cada entregable de código lleva **además** un archivo `.md` en `entregables/` que explica el
algoritmo **en dos niveles**: primero **alto nivel** (sin código, con analogías de la vida real) y
después **bajo nivel** (función por función). Aplicado por primera vez en la guía 6
(`explicacion_algoritmo.md`). **Repetir este formato en el parcial.**

### 🎯 Usar los algoritmos del profesor
*(instrucción de Harold, 2026-09-14)*
El profesor **revisa los algoritmos**, así que se implementan siguiendo su material: Bayes a mano
con diccionarios y el formato de resolución en cuatro pasos (Numerador / Contribución /
Denominador / Resultado), sin librerías de redes bayesianas. Misma regla para Min-Max, α-β y STRIPS.

### ✅ Formato del código del parcial: módulos `.py`
*(decidido 2026-09-14; P2 de preguntas.md)*
Se entregó como **módulos `.py` + README**, no como notebook: `python agente.py` genera los 4 PNG
y el `agent_log.txt` de una sola ejecución, que es exactamente lo que el profesor pide poder
ejecutar. Si el grupo quiere además un notebook para la demo, se hace uno que **importe** los
módulos, sin duplicar código.

### 🔑 Decisiones de diseño del parcial
*(2026-09-14)*
- **Un solo `dominio.py`** compartido por los tres métodos. Nada se define dos veces.
- **Nivel 4 del árbol Min-Max** = respuesta física del atleta (molestia muscular), con castigo
  proporcional a la exposición. Es lo que permite correr profundidades {2,3,4}.
- **Las 8 hojas base son literalmente las de la guía 5** y hay un test que lo verifica. Si
  cambiaran, todo lo ya presentado en clase dejaría de cuadrar.
- **Evaluación ingenua = solo rendimiento** (`rend × 4`). Es el contraste honesto contra la
  heurística diseñada: lo que haría un cuerpo técnico sin datos.
- **La meta conservadora de STRIPS** añade `reserva_energetica(alta)`, que exige insertar
  `Aplicar_Descarga_Extra` entre el monitoreo y la nutrición. Es lo que hace que Bayes
  **realmente** cambie el plan, y de paso genera la anomalía de Sussman.
- **31 tests de regresión** en `test_regresion.py`. Correrlos antes de tocar nada.
