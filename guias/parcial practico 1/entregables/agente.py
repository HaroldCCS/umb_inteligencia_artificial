# -*- coding: utf-8 -*-
"""
agente.py — Agente integrador
==============================
Parcial Practico 1 — Inteligencia Artificial Clasica

Une los tres metodos en un solo flujo:

    observe  ->  posterior  ->  plan  ->  decision  ->  accion
    (sensores)   (Bayes)       (STRIPS)   (Min-Max)

La bisagra es el UMBRAL: si la probabilidad de exito que estima la
red bayesiana cae por debajo, el agente cambia la META de STRIPS y
por tanto el plan que propone. Eso es lo que convierte tres modulos
sueltos en un agente.

Ejecutar:  python agente.py
Genera:    agent_log.txt, agent_summary.png
           (y, de paso, los otros tres PNG)
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

import dominio as D
import bayes
import minmax
import strips


# ═══════════════════════════════════════════════════════════════════
# 1. EL CICLO DEL AGENTE
# ═══════════════════════════════════════════════════════════════════

def observar():
    """
    PERCEPCION. En un sistema real esto leeria los sensores del
    atleta (HRV, sueno, carga GPS/IMU de Kinexon).

    Aqui se simula la lectura del miercoles previo al partido:
    los biomarcadores salen alterados -> fatiga alta.
    """
    return {"F": "Alta",
            "fuente": "HRV baja + sueno fragmentado (Kinexon, miercoles)"}


def ejecutar(evidencia=None, profundidad=D.PROFUNDIDAD,
             p_c=None, escenario=D.ESCENARIO_BASE,
             verbose=True, escribir_log=True):
    """
    Corre el ciclo completo del agente y devuelve un diccionario
    con todo lo que ocurrio (para las figuras y los experimentos).
    """
    if escribir_log:
        D.limpiar_log()
    registrar = D.log if verbose else (lambda *a, **k: None)

    evidencia = evidencia or observar()

    registrar("=" * 68)
    registrar(" AGENTE INTEGRADOR — IA CLASICA — PARCIAL PRACTICO 1")
    registrar(" Sector: rendimiento deportivo / gestion de carga del atleta")
    registrar("=" * 68)

    # ── 1. OBSERVE ────────────────────────────────────────────────
    registrar(f"[OBSERVE  ] Evidencia recibida: F = {evidencia['F']} "
              f"(fatiga)")
    registrar(f"[OBSERVE  ] Fuente: {evidencia.get('fuente', 'sensores')}")

    # ── 2. POSTERIOR ──────────────────────────────────────────────
    post = bayes.inferir(evidencia, p_c)
    registrar("")
    registrar(f"[POSTERIOR] P(C=Alta | F={evidencia['F']})  = "
              f"{post['diagnostico']:.4f}   (prior {post['prior_carga']:.3f})")
    registrar(f"[POSTERIOR] P(E=Exito | F={evidencia['F']}) = "
              f"{post['exito']:.4f}   (marginal {post['exito_marginal']:.4f})")
    registrar(f"[POSTERIOR] Umbral de decision = {D.UMBRAL_EXITO:.3f}")

    conservador = post["exito"] < D.UMBRAL_EXITO
    veredicto = ("POR DEBAJO del umbral -> META CONSERVADORA" if conservador
                 else "POR ENCIMA del umbral -> meta estandar")
    registrar(f"[POSTERIOR] {veredicto}")

    # ── 3. PLAN (STRIPS + A*) ─────────────────────────────────────
    meta = strips.META_CONSERVADORA if conservador else strips.META_BASE
    plan = strips.planificar_astar(strips.ESTADO_INICIAL, meta,
                                   strips.ACCIONES)

    registrar("")
    nombre_meta = "conservadora" if conservador else "estandar"
    registrar(f"[PLAN     ] Meta STRIPS ({nombre_meta}):")
    for p in sorted(meta):
        registrar(f"[PLAN     ]     · {p}")
    registrar(f"[PLAN     ] Motor de busqueda: A* sobre el espacio de estados")
    for i, a in enumerate(plan["plan"], 1):
        registrar(f"[PLAN     ]   {i}. {a.nombre.replace('_',' '):36} "
                  f"CO2 {a.co2_costo}")
    registrar(f"[PLAN     ] CO2 metabolico total: {plan['costo']} kg CO2eq "
              f"| estados expandidos: {plan['expandidos']}")

    # ── 4. DECISION (Min-Max + alfa-beta + heuristica) ────────────
    dec = minmax.decidir(profundidad=profundidad, poda=True,
                         heuristica=True, delta=escenario)

    registrar("")
    registrar(f"[DECISION ] Min-Max (profundidad {profundidad}, alfa-beta, "
              f"heuristica disenada)")
    registrar(f"[DECISION ] Rama escogida : {dec['rama']}")
    registrar(f"[DECISION ] Valor garantizado: {dec['valor']:+.1f}")
    registrar(f"[DECISION ] Nodos expandidos: {dec['nodos']} | "
              f"podas: {dec['podas']} | tiempo: {dec['tiempo_ms']:.3f} ms")

    # Contraste Min-Max (garantizado) vs Bayes (esperado)
    esperado = {}
    for c in bayes.VALORES_C:
        u_max = {f: max(D.utilidad_vector(D.vector_estado((c, f, d), escenario))
                        for d in D.OPC_DECISION)
                 for f in bayes.VALORES_F}
        esperado[c] = sum(bayes.P_F_dado_C[c][f] * u_max[f]
                          for f in bayes.VALORES_F)
    mejor_esperado = max(esperado, key=esperado.get)

    registrar("")
    registrar(f"[CONTRASTE] Utilidad esperada ponderada por Bayes:")
    for c, v in esperado.items():
        registrar(f"[CONTRASTE]     Carga {c:9} -> {v:+6.1f}")
    registrar(f"[CONTRASTE] Bayes elegiria: Carga {mejor_esperado} "
              f"({esperado[mejor_esperado]:+.1f})")
    coinciden = mejor_esperado == dec["decision"]
    veredicto_c = ("COINCIDE con Min-Max: decision robusta." if coinciden
                   else "NO COINCIDE: la decision es una apuesta.")
    registrar(f"[CONTRASTE] {veredicto_c}")

    # ── 5. ACCION ─────────────────────────────────────────────────
    carga, fatiga, uso = dec["ruta"][0], dec["ruta"][1], dec["ruta"][2]
    registrar("")
    registrar(f"[ACCION   ] Recomendacion al cuerpo tecnico:")
    registrar(f"[ACCION   ]   · Carga semanal: {carga.upper()}")
    registrar(f"[ACCION   ]   · Uso del jugador el fin de semana: "
              f"{uso.replace('_',' ').upper()}")
    registrar(f"[ACCION   ]   · Ejecutar el plan de {len(plan['plan'])} "
              f"pasos ({plan['costo']} kg CO2eq)")
    registrar(f"[ACCION   ]   · Asumiendo la peor respuesta del organismo "
              f"(fatiga {fatiga.lower()})")
    registrar("")
    registrar(f"[ETICA    ] Esto es una RECOMENDACION, no un veredicto. "
              f"La decision")
    registrar(f"[ETICA    ] final es del cuerpo medico (human-in-command), "
              f"segun el")
    registrar(f"[ETICA    ] Marco Etico para la IA en Colombia (2021).")
    registrar("=" * 68)

    if escribir_log:
        ruta = D.guardar_log()
        print(f"\n>> Registro guardado en {ruta}")

    return {
        "evidencia": evidencia, "posterior": post, "conservador": conservador,
        "meta": meta, "plan": plan, "decision": dec,
        "esperado": esperado, "coinciden": coinciden,
    }


# ═══════════════════════════════════════════════════════════════════
# 2. FIGURA RESUMEN — agent_summary.png
# ═══════════════════════════════════════════════════════════════════

def dibujar_resumen(res, archivo="agent_summary.png"):
    """
    Sintesis del agente en una sola figura, como exige el enunciado:

      1. El plan de STRIPS (mini-grafo).
      2. La probabilidad de exito bayesiana (mini-barras + numero).
      3. La decision final de Min-Max (texto grande).
    """
    post = res["posterior"]
    plan = res["plan"]["plan"]
    dec = res["decision"]

    fig = plt.figure(figsize=(17.5, 9.5))
    gs = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.0],
                          height_ratios=[1.0, 0.85],
                          hspace=0.30, wspace=0.16,
                          left=0.035, right=0.975, top=0.86, bottom=0.05)

    # ── (1) PLAN STRIPS — columna izquierda completa ──────────────
    ax1 = fig.add_subplot(gs[:, 0])
    ax1.set_title("1.  PLAN PROPUESTO   (STRIPS + A*)",
                  fontsize=13, fontweight="bold", color=D.AZUL, loc="left",
                  pad=12)

    n = len(plan)
    for i, a in enumerate(plan):
        y = n - i - 1
        caja = FancyBboxPatch((0.06, y - 0.30), 0.80, 0.60,
                              boxstyle="round,pad=0.02",
                              facecolor=D.AZUL if a.co2_costo < 5 else D.ROJO,
                              edgecolor="white", linewidth=2)
        ax1.add_patch(caja)
        ax1.text(0.12, y, f"{i+1}.", fontsize=13, fontweight="bold",
                 color="white", va="center")
        ax1.text(0.20, y + 0.09, a.nombre.replace("_", " "), fontsize=11,
                 fontweight="bold", color="white", va="center")
        ax1.text(0.20, y - 0.13, f"CO2 = {a.co2_costo} kg CO2eq",
                 fontsize=8.5, color="#EAF2F8", va="center")
        if i < n - 1:
            ax1.add_patch(FancyArrowPatch(
                (0.46, y - 0.32), (0.46, y - 0.70),
                arrowstyle="-|>", mutation_scale=17,
                color=D.GRIS, linewidth=2))

    etq_meta = "CONSERVADORA" if res["conservador"] else "estandar"
    extra_meta = " + reserva energetica" if res["conservador"] else ""
    ax1.text(0.06, -0.95,
             f"Estado inicial:  atleta fatigado, CO2 acumulado alto\n"
             f"Meta ({etq_meta}):  listo para competir{extra_meta}\n"
             f"CO2 total del plan: {res['plan']['costo']} kg CO2eq   |   "
             f"estados expandidos por A*: {res['plan']['expandidos']}",
             fontsize=9.5, va="top", family="monospace",
             bbox=dict(boxstyle="round,pad=0.5", facecolor="#F4F6F7",
                       edgecolor=D.GRIS))

    ax1.set_xlim(0, 1)
    ax1.set_ylim(-1.75, n - 0.3)
    ax1.axis("off")

    # ── (2) PROBABILIDAD BAYESIANA — arriba derecha ───────────────
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_title("2.  PROBABILIDAD DE EXITO   (Red Bayesiana)",
                  fontsize=13, fontweight="bold", color=D.AZUL, loc="left",
                  pad=12)

    etiquetas = ["Sin evidencia", f"Con evidencia\n{post['evidencia']}"]
    valores = [post["exito_marginal"] * 100, post["exito"] * 100]
    colores = [D.GRIS, D.NARANJA if res["conservador"] else D.VERDE]
    barras = ax2.bar(etiquetas, valores, color=colores, width=0.5,
                     edgecolor="white", linewidth=2)
    for b, v in zip(barras, valores):
        ax2.annotate(f"{v:.1f} %",
                     (b.get_x() + b.get_width() / 2, b.get_height()),
                     ha="center", va="bottom", xytext=(0, 4),
                     textcoords="offset points", fontsize=11,
                     fontweight="bold", color=D.AZUL)
    ax2.axhline(D.UMBRAL_EXITO * 100, color=D.ROJO, ls=":", lw=2)
    ax2.annotate(f"umbral {D.UMBRAL_EXITO*100:.0f} %",
                 xy=(1.42, D.UMBRAL_EXITO * 100 + 2), ha="right",
                 fontsize=8.5, color=D.ROJO, style="italic")
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("P(E = Exito)  [%]", fontsize=10, fontweight="bold")
    ax2.grid(axis="y", alpha=0.3)
    ax2.set_axisbelow(True)

    # Numero destacado
    ax2.text(0.97, 0.93, f"{post['exito']*100:.1f} %",
             transform=ax2.transAxes, fontsize=40, fontweight="bold",
             color=D.NARANJA if res["conservador"] else D.VERDE,
             ha="right", va="top")
    ax2.text(0.97, 0.60,
             f"P(C=Alta | F=Alta) = {post['diagnostico']*100:.1f} %\n"
             f"(prior {post['prior_carga']*100:.0f} %)",
             transform=ax2.transAxes, fontsize=9, color="#5D6D7E",
             ha="right", va="top", family="monospace")

    # ── (3) DECISION MIN-MAX — abajo derecha ──────────────────────
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_title("3.  DECISION FINAL   (Min-Max + poda alfa-beta)",
                  fontsize=13, fontweight="bold", color=D.AZUL, loc="left",
                  pad=12)

    ax3.add_patch(FancyBboxPatch((0.02, 0.42), 0.96, 0.46,
                                 boxstyle="round,pad=0.02",
                                 facecolor=D.ROJO, edgecolor="white",
                                 linewidth=3))
    carga, fatiga, uso = dec["ruta"][0], dec["ruta"][1], dec["ruta"][2]
    ax3.text(0.50, 0.73, f"CARGA {carga.upper()}", fontsize=23,
             fontweight="bold", color="white", ha="center", va="center")
    ax3.text(0.50, 0.54, f"→  {uso.replace('_',' ').upper()}", fontsize=19,
             fontweight="bold", color="#FADBD8", ha="center", va="center")

    ax3.text(0.02, 0.30,
             f"Rama escogida:  {dec['rama'].replace('_',' ')}\n"
             f"Valor garantizado (Min-Max) : {dec['valor']:+.0f}\n"
             f"Valor esperado   (Bayes)    : "
             f"{res['esperado'][dec['decision']]:+.1f}\n"
             f"Nodos expandidos: {dec['nodos']}   podas: {dec['podas']}   "
             f"tiempo: {dec['tiempo_ms']:.2f} ms",
             fontsize=9.5, va="top", family="monospace")

    ax3.text(0.02, 0.02,
             ("Min-Max y Bayes COINCIDEN: decision robusta."
              if res["coinciden"] else
              "Min-Max y Bayes DIFIEREN: la decision es una apuesta."),
             fontsize=10, fontweight="bold",
             color=D.VERDE if res["coinciden"] else D.ROJO, va="bottom")

    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)
    ax3.axis("off")

    # ── Titulo general ────────────────────────────────────────────
    fig.suptitle(
        "AGENTE INTEGRADOR — sintesis de una ejecucion\n"
        f"observe ({post['evidencia']})  ->  posterior  ->  plan  ->  "
        f"decision  ->  accion",
        fontsize=16, fontweight="bold", color=D.AZUL, y=0.965)

    plt.savefig(archivo, dpi=130, bbox_inches="tight")
    plt.close()
    return archivo


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    resultado = ejecutar()

    # Las cuatro visualizaciones obligatorias
    f1 = bayes.dibujar_barras()
    f2 = strips.dibujar_grafo(resultado["plan"], strips.ESTADO_INICIAL,
                              resultado["meta"])
    f3, _, _ = minmax.dibujar_arbol()
    f4 = dibujar_resumen(resultado)

    print(">> Figuras generadas:")
    for f in (f3, f2, f1, f4):
        print(f"     {f}")
