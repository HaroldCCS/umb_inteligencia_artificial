# Preguntas abiertas para Harold

> Bloqueantes y decisiones que necesito confirmar. **Cuando respondes una, la borro de aquí y la
> registro en `proyecto/decisiones.md`.**
> 📅 Contexto: el parcial se entrega el **jueves 17 de septiembre**. Quedan 3 días.

_Resueltas y archivadas el 14-sep: fecha de entrega · estado real de la guía 5 · si se mantiene el
factor λ de huella de carbono. Ver `proyecto/decisiones.md`._

---

## 🔴 BLOQUEANTE

### P1. ¿Las CPTs de la red bayesiana les cuadran futbolísticamente?
Es lo único que bloquea empezar a programar hoy mismo. La red es
**Carga semanal (C) → Fatiga (F) → Éxito competitivo (E)** — a propósito, las **mismas variables de
los niveles 1 y 2 del árbol Min-Max** de la guía 5, para que los tres métodos hablen del mismo mundo.

| CPT | Valores propuestos |
|---|---|
| `P(C=Alta)` | 0.40 |
| `P(F=Alta \| C=Alta)` | 0.75 |
| `P(F=Alta \| C=Moderada)` | 0.30 |
| `P(E=Éxito \| C=Alta, F=Alta)` | 0.25 |
| `P(E=Éxito \| C=Alta, F=Baja)` | 0.65 |
| `P(E=Éxito \| C=Mod, F=Alta)` | 0.45 |
| `P(E=Éxito \| C=Mod, F=Baja)` | 0.85 |

Están elegidos para que el **orden** coincida con el de las utilidades de la guía 5
(`CM_FB` la mejor, `CA_FA` la peor), así que no son números sueltos.

- ¿Les parecen razonables, o el grupo ya había pensado otras variables en clase?
- Si les sirven, **respondo "ok" y arranco**: eso cierra también la guía 6.

**Respuesta:**

---

## 🟡 DECISIONES DE DISEÑO (tengo un default; confírmalo o cámbialo)

### P2. ¿Script `.py` o notebook para el parcial?
Mi propuesta: **módulos `.py`** (`dominio`, `bayes`, `strips`, `minmax`, `agente`) + README,
porque genera los 4 PNG y el `agent_log.txt` con un solo `python agente.py`, que es exactamente lo
que el profesor pide poder ejecutar. Si quieren notebook para la demo, lo hago **además**,
importando los módulos (sin duplicar código).

- **(a)** Solo módulos `.py` + README ← *mi recomendación*
- **(b)** `.py` + notebook de demo
- **(c)** Solo notebook (como vienen trabajando las guías)

**Respuesta:**

---

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
