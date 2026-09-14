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
🔴 **No desarrollada.** Carpeta `entregables/` vacía.
👉 Ver `planeacion.md` en esta misma carpeta (versión 2, dominio de gestión de carga).

## Para recordar
La red que se construya aquí es **la misma** que se usa en el parcial (módulo bayesiano del agente
y análisis de sensibilidad). No inventar dos modelos distintos.
