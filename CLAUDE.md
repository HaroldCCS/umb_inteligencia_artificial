# Instrucciones de trabajo — Vault de Inteligencia Artificial

Este vault (Obsidian) es el espacio de trabajo del curso **Inteligencia Artificial** de Harold
Camargo y su grupo. Este archivo es mi manual de operación: cómo está organizado todo, qué escribo
yo, y cómo trabajo.

---

## 1. Lo primero que leo, siempre

1. **`proyecto/proyecto.md`** — ficha maestra: sector, integrantes, modelo técnico canónico
   (grafo, métricas, heurística, parámetros), resultados ya obtenidos y postura ética del grupo.
   **Es la fuente de verdad.** Si una guía contradice este archivo, gana este archivo.
2. **`proyecto/decisiones.md`** — bitácora de lo que Harold ya respondió. **Leerlo antes de
   preguntar cualquier cosa**: si la respuesta está ahí, ya no se pregunta.
3. **`preguntas.md`** (raíz) — dudas abiertas que bloquean el trabajo.
4. El **`contexto.md`** de la guía en la que esté trabajando.

Con esos cuatro archivos tengo el contexto completo sin releer los recursos del profesor.

---

## 2. Estructura de carpetas

```
inteligencia_artificial/
├── CLAUDE.md              ← este archivo
├── preguntas.md           ← dudas abiertas para Harold
├── proyecto/
│   ├── proyecto.md        ← ficha maestra del proyecto de grupo
│   └── decisiones.md      ← bitácora de respuestas y decisiones tomadas
└── guias/
    ├── guia 1/ … guia 6/
    └── parcial practico 1/
```

Cada guía (y el parcial) tiene:

| Elemento | Qué es | Quién lo escribe |
|---|---|---|
| `actividad.md` | Indicaciones del profesor | **El profesor** — no tocar |
| `recursos/` | Material del profesor: algoritmos, PDFs convertidos, leyes, lecturas, notebooks base | **El profesor** — no tocar |
| `entregables/` | Lo que produce el grupo: notebooks, documentos, presentaciones | El grupo (y yo, cuando me lo piden) |
| `contexto.md` | **Lo escribo yo.** Resumen de qué contiene la guía y para qué sirve | Yo |
| `planeacion.md` | **Lo escribo yo.** Solo en guías sin desarrollar: qué hay que hacer y cómo | Yo |

---

## 3. Los archivos que yo mantengo

### `contexto.md` (uno por guía)
Existe para que en futuras conversaciones **no tenga que releer todos los recursos**: con leer el
`contexto.md` me basta. Debe contener:
- Qué pide el profesor (resumen fiel del `actividad.md`).
- Finalidad de la guía dentro del curso.
- **Resumen utilizable de cada recurso** — los conceptos, fórmulas, ejemplos numéricos y frases
  clave que necesitaría citar, no solo "trata sobre X".
- Qué entregó el grupo y los resultados concretos (cifras, rutas, conclusiones).
- Estado: ✅ entregada / ⚠️ parcial / 🔴 pendiente.
- Enlaces con las otras guías y con el proyecto.

### `planeacion.md` (solo guías sin desarrollar)
Plan de ataque **basado en el contenido del profesor y en la idea de nuestro proyecto**:
decisiones de diseño justificadas, números ya calculados donde se pueda, estructura de archivos,
orden de trabajo y trampas a evitar. No es el entregable: es el mapa para construirlo.

### `preguntas.md` (raíz)
Dudas que me bloquean o decisiones que son de Harold, no mías. Organizadas por severidad
(🔴 bloqueante / 🟡 decisión de diseño con default propuesto / 🟢 menor).
**Ciclo de vida obligatorio:**
1. Escribo la pregunta con mi recomendación cuando la tenga.
2. Harold responde (en el archivo o en el chat).
3. **Borro la pregunta de `preguntas.md`** y **registro la respuesta en `proyecto/decisiones.md`**
   (y, si cambia el modelo, actualizo también `proyecto/proyecto.md` y el `contexto.md` afectado).
4. A partir de ahí eso **ya lo sé por defecto**: no se vuelve a preguntar.

Si `preguntas.md` queda vacío, lo dejo con el encabezado y una nota de "sin preguntas abiertas".

### `proyecto/proyecto.md`
Todo lo transversal del proyecto de grupo. Se actualiza cuando cambia el modelo, aparecen
resultados nuevos o se toma una decisión de diseño. Es lo que aplico en todas las guías.

---

## 4. Cómo trabajo

- **Los recursos del profesor mandan.** Uso en la mayor medida posible los algoritmos, ejemplos,
  estructuras y vocabulario que él entregó. El objetivo es que en la sustentación no nos desviemos
  del enfoque del curso. Material externo solo si hace falta y señalándolo como tal.
- **Todo se conecta con el proyecto.** El sector es fútbol profesional / rendimiento deportivo.
  Cada guía es un método nuevo aplicado **al mismo problema**: la salida de balón desde la
  portería hasta el delantero.
- **Un solo modelo.** No redefinir el grafo, las métricas ni los parámetros en cada entregable:
  se importan de lo ya establecido en `proyecto/proyecto.md`. Cambiarlos rompe la coherencia con
  todo lo ya presentado.
- **Verificar los números.** Cualquier cifra que escriba (probabilidades, costos, utilidades) la
  calculo de verdad antes de ponerla, y dejo el cálculo reproducible.
- **Español**, siempre. Estilo de los notebooks: modelo → cálculo → **lectura del resultado en
  lenguaje del sector**. Ninguna tabla se queda sin su interpretación futbolística.
- **No desarrollo entregables si no me lo piden.** Planear y documentar ≠ producir el entregable.
- Al terminar un bloque de trabajo, aviso qué hice y **si hay bloqueantes**.

---

## 5. Convenciones técnicas

- Librerías: `networkx`, `matplotlib`, `pandas`, `heapq`, `collections`. Sin dependencias nuevas
  (nada de `pgmpy` ni planificadores PDDL externos: el profesor quiere ver el razonamiento a mano).
- Paleta fija: `ROJO='#EE2A49'`, `AZUL='#3E4B5B'`, `CLARO='#D8D8D8'`, `FONDO='#EDEDED'`,
  `VERDE='#2ECC71'`.
- Parámetros ajustables (`λ`, `w`, umbrales, priors) como constantes al inicio del archivo, con
  nota de "cambia esto y re-ejecuta: todo se recalcula solo".
- Presentaciones: el grupo usa **Gamma** (gamma.app).
- Nombres de archivo exigidos por el profesor (p. ej. los PNG del parcial) se respetan **al pie de
  la letra**, sin subcarpetas.
