# Contexto — Guía 6: Incertidumbre y Redes Bayesianas

## Qué pide el profesor
1. **Construcción de la red:** identificar **tres variables principales** que afectan un resultado
   en el contexto del sector, dibujar la red bayesiana con sus dependencias y definir las
   **probabilidades previas y las CPTs**.
2. **Probabilidad conjunta:** calcular `P(X=positivo, Y=favorable, Z=éxito)` e interpretarla.
3. **Inferencia con evidencia parcial:** calcular `P(Resultado | X = favorable)` y explicar cómo
   cambia la expectativa al conocer la evidencia.

## Finalidad dentro del curso
Cierra el trío de la **IA clásica**: STRIPS planifica (determinista), Min-Max decide
(adversarial), Bayes **razona bajo incertidumbre**. Es el tercer método que el parcial exige integrar.

## Recursos (resumen para no releerlos) — `PLANIFIC BAYESIANO.md`
- **Red bayesiana** = DAG; nodos = variables aleatorias; arcos = dependencia probabilística;
  cada nodo trae su **CPT**.
- **Teorema de Bayes:** `P(H|E) = P(E|H)·P(H) / P(E)`.
- **Ejemplos resueltos paso a paso en el PDF** (sirven de plantilla de cálculo):
  - Gripe/Fiebre/Dolor → `P(G|F,D) ≈ 50.9 %` (prior 10 % → 51 %).
  - Lluvia/Paraguas → `P(L|P) ≈ 63.16 %`.
  - Fraude/Transacción grande/Extranjero → `P(F|T,E) ≈ 69.57 %`.
  - Batería/Coche no arranca/Luces → `P(B|C,L) ≈ 94.44 %`.
  - **Turismo (el más importante como plantilla estructural):** `Clima → Transporte → Actividad`,
    con `P(C)`, `P(T|C)` y `P(A|C,T)`; se calcula
    `P(A=Divertida | C=Bueno) = Σ_T P(A|C,T)·P(T|C) = 0.5·0.2 + 0.9·0.8 = 0.82`, frente a un
    marginal de 0.64. **Esta es la forma exacta de red que el profesor espera.**
- **Tres tipos de razonamiento:**
  - **Causal** (↓, causa→efecto): "si pasa esto, ¿qué pasará?" — predicción.
  - **Diagnóstico** (↑, efecto→causa): "si vi esto, ¿qué lo causó?" — Bayes puro.
  - **Intercausal / explaining away**: confirmar una causa **baja** la probabilidad de la otra
    (alarma del banco: robo vs fallo del sensor).
- **Comparativa final del PDF:** STRIPS = determinista; Min-Max = competitivo con rival perfecto;
  Bayes = probabilístico y actualizable con evidencia. *"Un agente real necesita las tres cosas."*

## Estado
✅ **Desarrollada** (14-sep-2026).

### Qué entregamos (`entregables/`)
| Archivo | Qué es |
|---|---|
| `Red_Bayesiana_Rendimiento.ipynb` | Notebook ejecutado (25 celdas, salidas embebidas, 0 errores). Listo para Colab |
| `explicacion_algoritmo.md` | Explicación en dos niveles: alto nivel (sin código, con analogías) y bajo nivel (función por función) |
| `red_bayesiana.png` | Diagrama del DAG con las tres CPTs anotadas |
| `bayes_bars.png` | Gráfico de barras — **también es archivo obligatorio del Parcial Práctico 1** |

### El modelo
Red `C → F`, `C → E`, `F → E` sobre el **Dominio B** (gestión de carga del atleta):
- **C** = Carga semanal (Alta 0.40 / Moderada 0.60) — es el Nivel 1 del árbol Min-Max de la guía 5.
- **F** = Fatiga (Alta/Baja) — es el Nivel 2 (MIN) del mismo árbol.
- **E** = Éxito competitivo (Éxito/Fallo).

### Resultados (verificados)
| Consulta | Valor |
|---|---|
| `P(C=Moderada, F=Baja, E=Éxito)` conjunta | **35.7 %** |
| `P(C=Alta, F=Alta, E=Éxito)` conjunta | **7.5 %** |
| `P(E=Éxito)` marginal | **57.8 %** |
| `P(E=Éxito \| C=Moderada)` causal | **73.0 %** |
| `P(E=Éxito \| C=Alta)` causal | **35.0 %** |
| `P(C=Alta \| F=Alta)` diagnóstico | **62.5 %** (prior 40 %) |
| `P(E=Éxito \| F=Alta)` ← la usa el agente | **32.5 %** |
| `P(E=Éxito \| F=Baja)` | **81.2 %** |
| *Explaining away*: `P(C=Alta \| F=Alta, V=Sí)` | **50.0 %** (baja 12.5 pts) |

### Extras que no pedía la actividad pero fortalecen la sustentación
- **Los tres tipos de razonamiento** del PDF aplicados al caso (causal, diagnóstico e intercausal).
  Para el intercausal se extiende la red con una segunda causa de la fatiga (**viaje largo**), con
  CPTs calibradas para que al marginalizarla se recupere la `P(F|C)` original — por eso el
  resultado sin evidencia de viaje da exactamente el mismo 62.5 %.
- **Comparación Min-Max vs Bayes:** Min-Max garantiza **+19**, Bayes espera **+35.1**. Ambos eligen
  carga moderada. *La diferencia es el precio del pesimismo.*

### Frase de cierre de la guía
> **Bayes es el único de los tres métodos del corte que cambia de opinión cuando llega un dato
> nuevo.** STRIPS planifica como si nada pudiera salir mal; Min-Max decide como si todo fuera a
> salir mal; Bayes reparte la creencia según la evidencia.

## Para recordar
La red de esta guía es **la misma** que usa el parcial (módulo bayesiano del agente y análisis de
sensibilidad). El código de las celdas 2, 6, 7, 8 y 9 se extrae tal cual a `bayes.py`.
`bayes_bars.png` ya está generado con el nombre exacto que exige el parcial.
