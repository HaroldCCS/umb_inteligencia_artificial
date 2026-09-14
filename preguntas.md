# Preguntas abiertas para Harold

> Bloqueantes y decisiones que necesito confirmar. **Cuando respondes una, la borro de aquí y la
> registro en `proyecto/decisiones.md`.**
> 📅 Contexto: el parcial se entrega el **jueves 17 de septiembre**. Quedan 3 días.

_Resueltas y archivadas el 14-sep: fecha de entrega · estado real de la guía 5 · factor λ ·
variables de la red bayesiana · formato del código del parcial. Ver `proyecto/decisiones.md`._

✅ **Guía 6 entregada** y ✅ **código del parcial completo** (14-sep).
Lo que queda abierto es la **presentación** y el reparto de la exposición.

---

## 🟢 PARA REVISAR (no bloquea, ya está implementado)

### P1. ¿Te cuadran las CPTs de la red bayesiana?
La guía 6 ya está construida con estos valores. **No bloquean nada**: viven en la celda 2 del
notebook, se cambian en una línea y todo se recalcula solo (tablas, las 4 inferencias, las 2
figuras y la comparación con Min-Max).

| CPT | Valor usado | Lectura |
|---|---|---|
| `P(C=Alta)` | 0.40 | 4 de cada 10 semanas se aplica carga alta |
| `P(F=Alta \| C=Alta)` | 0.75 | Con carga alta llega fatigado 3 de cada 4 veces |
| `P(F=Alta \| C=Moderada)` | 0.30 | Con carga moderada, 3 de cada 10 |
| `P(E=Éxito \| Alta, Alta)` | 0.25 | |
| `P(E=Éxito \| Alta, Baja)` | 0.65 | |
| `P(E=Éxito \| Mod, Alta)` | 0.45 | |
| `P(E=Éxito \| Mod, Baja)` | 0.85 | |

Están elegidos para que el **orden** coincida con las utilidades de la guía 5 (`Mod+Baja` la mejor,
`Alta+Alta` la peor), así que no son números sueltos. Si Keiry o Juan Felipe tienen otra intuición
futbolística, dímelo y los ajusto — es cuestión de minutos.

**Respuesta:**

---

## 🟡 DECISIONES DE DISEÑO (tengo un default; confírmalo o cámbialo)

### P3. ¿La presentación conceptual se hace en Gamma otra vez?
Las guías 1 y 2 se presentaron en **Gamma**. Si es así, dejo el contenido estructurado en markdown
listo para pegar. Si prefieren PowerPoint o PDF, lo genero directamente.

**Respuesta:**

---

### P4. ¿Quién expone qué en los 5 minutos?
Hay guion minuto a minuto en `guias/parcial practico 1/planeacion.md` §8
(Min-Max / STRIPS / Bayes / agente / cierre). Si me dices quién toma cada bloque, preparo las notas
de cada quien.

**Respuesta:**

---

### P5. ¿Corrijo el notebook de la guía 5 o lo dejo como está?
Encontré cinco cosas menores (detalle en `guias/guia 5/contexto.md`):
1. `ruta_optima` guarda **un solo nodo** en vez de la rama completa → el resumen imprime solo
   "Carga_Moderada".
2. El conteo de nodos podados es aproximado.
3. Los comentarios de valores en la celda 4 están desactualizados (dicen −29, −3, +6, +36, +37;
   los reales son −27, −1, +4, +42, +41).
4. `busqueda_forward` devuelve 4 elementos si falla y 5 si tiene éxito → revienta al desempaquetar.
5. La conclusión del experimento λ confunde **mejor hoja** con **decisión Min-Max**.

Los puntos 1 y 2 **hay que arreglarlos igual** para el parcial (se califican). La pregunta es si
además **actualizo el notebook de la guía 5** (por si el profesor lo revisa) o lo dejo tal cual
porque ya se entregó.

- **(a)** Arreglar solo en el parcial ← *más seguro si ya se entregó*
- **(b)** Arreglar también el notebook de la guía 5

**Respuesta:**

---

## 🟢 MENOR (puedo decidirlo yo si no contestas)

### P6. El notebook de la guía 3 está incompleto en disco
Le faltan las celdas con `grafo`, `bfs`, `dfs`, `ucs`. ¿Lo reconstruyo y lo dejo ejecutable, o lo
dejamos así porque ya se presentó? Dado el tiempo, mi recomendación es **dejarlo** y volver
después del parcial.

**Respuesta:**
