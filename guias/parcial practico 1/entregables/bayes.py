# -*- coding: utf-8 -*-
"""
bayes.py — Red Bayesiana del agente
====================================
Parcial Practico 1 — Inteligencia Artificial Clasica

Es LA MISMA red de la Guia 6. No se construye un modelo distinto:
el codigo aqui es el de aquel notebook, reorganizado como modulo.

        C  (Carga semanal)
       / \\
      v   v
     F --> E
  (Fatiga) (Exito competitivo)

Las variables C y F son, a proposito, los niveles 1 y 2 del arbol
Min-Max: asi los dos metodos hablan del mismo mundo.

Todo el calculo es A MANO (diccionarios y aritmetica), siguiendo el
formato de resolucion del material de clase. Sin librerias de redes
bayesianas.

Genera: bayes_bars.png
"""

from itertools import product

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import dominio as D


# ═══════════════════════════════════════════════════════════════════
# 1. VARIABLES Y CPTs
# ═══════════════════════════════════════════════════════════════════

VALORES_C = ["Alta", "Moderada"]
VALORES_F = ["Alta", "Baja"]
VALORES_E = ["Exito", "Fallo"]

# CPT 1 — P(C): probabilidad previa de la carga semanal
P_C = {"Alta": 0.40, "Moderada": 0.60}

# CPT 2 — P(F | C): la fatiga depende de la carga
P_F_dado_C = {
    "Alta":     {"Alta": 0.75, "Baja": 0.25},
    "Moderada": {"Alta": 0.30, "Baja": 0.70},
}

# CPT 3 — P(E | C, F): el exito depende de ambas
P_E_dado_CF = {
    ("Alta",     "Alta"): {"Exito": 0.25, "Fallo": 0.75},
    ("Alta",     "Baja"): {"Exito": 0.65, "Fallo": 0.35},
    ("Moderada", "Alta"): {"Exito": 0.45, "Fallo": 0.55},
    ("Moderada", "Baja"): {"Exito": 0.85, "Fallo": 0.15},
}


def validar_cpts(p_c=None):
    """Toda distribucion de probabilidad debe sumar 1."""
    p_c = p_c or P_C
    ok = abs(sum(p_c.values()) - 1) < 1e-9
    ok &= all(abs(sum(d.values()) - 1) < 1e-9 for d in P_F_dado_C.values())
    ok &= all(abs(sum(d.values()) - 1) < 1e-9 for d in P_E_dado_CF.values())
    return ok


# ═══════════════════════════════════════════════════════════════════
# 2. INFERENCIA
# ═══════════════════════════════════════════════════════════════════

def p_conjunta(c, f, e, p_c=None):
    """P(C,F,E) = P(C) * P(F|C) * P(E|C,F)  — factorizacion de la red."""
    p_c = p_c or P_C
    return p_c[c] * P_F_dado_C[c][f] * P_E_dado_CF[(c, f)][e]


def p_exito_marginal(p_c=None):
    """P(E=Exito) — regla de la probabilidad total sobre C y F."""
    return sum(p_conjunta(c, f, "Exito", p_c)
               for c, f in product(VALORES_C, VALORES_F))


def p_exito_dado_carga(c, p_c=None):
    """
    Razonamiento CAUSAL: P(E|C) = SUMA_F P(E|C,F) * P(F|C)

    No hace falta dividir: C es la raiz de la red, asi que los
    pesos P(F|C) ya suman 1.
    """
    return sum(P_E_dado_CF[(c, f)]["Exito"] * P_F_dado_C[c][f]
               for f in VALORES_F)


def p_carga_dado_fatiga(c_obs, f_obs, p_c=None):
    """
    Razonamiento DIAGNOSTICO: Teorema de Bayes.

                 P(F|C) * P(C)
        P(C|F) = -------------
                     P(F)
    """
    p_c = p_c or P_C
    num = P_F_dado_C[c_obs][f_obs] * p_c[c_obs]
    den = sum(P_F_dado_C[c][f_obs] * p_c[c] for c in VALORES_C)
    return num / den


def p_exito_dado_fatiga(f_obs, p_c=None):
    """
    P(E=Exito | F). Combina las dos direcciones: retrocede de F a C
    y avanza de C a E. Aqui SI hay que normalizar, porque la
    evidencia esta en una variable que no es la raiz.

    Es la consulta que usa el agente en su paso observe -> posterior.
    """
    p_c = p_c or P_C
    num = sum(p_c[c] * P_F_dado_C[c][f_obs] * P_E_dado_CF[(c, f_obs)]["Exito"]
              for c in VALORES_C)
    den = sum(p_c[c] * P_F_dado_C[c][f_obs] for c in VALORES_C)
    return num / den


def inferir(evidencia, p_c=None):
    """
    Interfaz que usa el agente.

    evidencia : dict, por ejemplo {"F": "Alta"}
    devuelve  : dict con el posterior de exito y el diagnostico
    """
    p_c = p_c or P_C
    if "F" in evidencia:
        f = evidencia["F"]
        return {
            "exito":          p_exito_dado_fatiga(f, p_c),
            "exito_marginal": p_exito_marginal(p_c),
            "diagnostico":    p_carga_dado_fatiga("Alta", f, p_c),
            "prior_carga":    p_c["Alta"],
            "evidencia":      f"F = {f}",
        }
    if "C" in evidencia:
        c = evidencia["C"]
        return {
            "exito":          p_exito_dado_carga(c, p_c),
            "exito_marginal": p_exito_marginal(p_c),
            "diagnostico":    None,
            "prior_carga":    p_c["Alta"],
            "evidencia":      f"C = {c}",
        }
    return {"exito": p_exito_marginal(p_c),
            "exito_marginal": p_exito_marginal(p_c),
            "diagnostico": None, "prior_carga": p_c["Alta"],
            "evidencia": "ninguna"}


# ═══════════════════════════════════════════════════════════════════
# 3. VISUALIZACION — bayes_bars.png
# ═══════════════════════════════════════════════════════════════════

def dibujar_barras(archivo="bayes_bars.png", p_c=None):
    """
    Grafico de barras con las probabilidades calculadas.

    Requisito del enunciado: ejes y etiquetas claras, y la evidencia
    usada visible DENTRO del grafico.
    """
    p_c = p_c or P_C
    marginal = p_exito_marginal(p_c)
    diag = p_carga_dado_fatiga("Alta", "Alta", p_c)

    escenarios = [
        ("Sin evidencia\n(marginal)",        marginal,                      D.GRIS),
        ("Evidencia:\nC = Moderada",         p_exito_dado_carga("Moderada", p_c), D.VERDE),
        ("Evidencia:\nC = Alta",             p_exito_dado_carga("Alta", p_c),     D.ROJO),
        ("Evidencia:\nF = Baja (fresco)",    p_exito_dado_fatiga("Baja", p_c),    D.AZUL),
        ("Evidencia:\nF = Alta (fatigado)",  p_exito_dado_fatiga("Alta", p_c),    D.NARANJA),
    ]

    nombres = [e[0] for e in escenarios]
    valores = [e[1] * 100 for e in escenarios]
    colores = [e[2] for e in escenarios]

    fig, ax = plt.subplots(figsize=(12, 6.5))
    barras = ax.bar(nombres, valores, color=colores, alpha=0.9,
                    edgecolor="white", linewidth=2)

    for b, v in zip(barras, valores):
        ax.annotate(f"{v:.1f} %",
                    (b.get_x() + b.get_width() / 2, b.get_height()),
                    ha="center", va="bottom", xytext=(0, 5),
                    textcoords="offset points",
                    fontsize=12, fontweight="bold", color=D.AZUL)

    ax.axhline(marginal * 100, color=D.GRIS, linestyle="--", linewidth=2,
               zorder=0)
    ax.annotate(f"linea base sin evidencia = {marginal*100:.1f} %",
                xy=(4.42, marginal * 100 + 1.4), ha="right", fontsize=9,
                color=D.GRIS, style="italic")

    # Umbral de decision del agente
    ax.axhline(D.UMBRAL_EXITO * 100, color=D.ROJO, linestyle=":",
               linewidth=2, zorder=0)
    ax.annotate(f"umbral del agente = {D.UMBRAL_EXITO*100:.0f} %  "
                f"(por debajo -> plan conservador)",
                xy=(-0.42, D.UMBRAL_EXITO * 100 + 1.4), ha="left",
                fontsize=9, color=D.ROJO, style="italic")

    ax.set_ylabel("P(E = Exito competitivo)   [%]", fontsize=12,
                  fontweight="bold")
    ax.set_ylim(0, 100)
    ax.set_title(
        "Probabilidad de exito competitivo segun la evidencia observada\n"
        "Red bayesiana  C (Carga) -> F (Fatiga) -> E (Exito)",
        fontsize=13, fontweight="bold", color=D.AZUL, pad=16)
    ax.grid(axis="y", alpha=0.3)
    ax.set_axisbelow(True)

    texto = ("EVIDENCIA UTILIZADA\n"
             "  C = Carga semanal aplicada (planilla del cuerpo tecnico)\n"
             "  F = Fatiga medida por HRV, sueno y carga GPS/IMU (Kinexon)\n"
             f"\nDiagnostico asociado:  P(C=Alta | F=Alta) = {diag*100:.1f} %\n"
             f"(el prior era {p_c['Alta']*100:.0f} %)")
    ax.text(0.015, 0.97, texto, transform=ax.transAxes, fontsize=9,
            va="top", ha="left", family="monospace",
            bbox=dict(boxstyle="round,pad=0.6", facecolor="#FFFDF0",
                      edgecolor=D.AMARILLO, linewidth=1.5))

    plt.tight_layout()
    plt.savefig(archivo, dpi=140, bbox_inches="tight")
    plt.close()
    return archivo


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 70)
    print("  RED BAYESIANA — C (Carga) -> F (Fatiga) -> E (Exito)")
    print("=" * 70)
    print(f"\n  CPTs validas: {validar_cpts()}")
    total = sum(p_conjunta(c, f, e)
                for c, f, e in product(VALORES_C, VALORES_F, VALORES_E))
    print(f"  Conjunta suma: {total:.5f}")

    print(f"\n  P(C=Moderada, F=Baja, E=Exito) = "
          f"{p_conjunta('Moderada','Baja','Exito'):.5f}")
    print(f"  P(C=Alta, F=Alta, E=Exito)     = "
          f"{p_conjunta('Alta','Alta','Exito'):.5f}")
    print(f"\n  P(E=Exito) marginal        = {p_exito_marginal():.4f}")
    print(f"  P(E=Exito | C=Moderada)    = {p_exito_dado_carga('Moderada'):.4f}")
    print(f"  P(E=Exito | C=Alta)        = {p_exito_dado_carga('Alta'):.4f}")
    print(f"  P(E=Exito | F=Alta)        = {p_exito_dado_fatiga('Alta'):.4f}")
    print(f"  P(E=Exito | F=Baja)        = {p_exito_dado_fatiga('Baja'):.4f}")
    print(f"  P(C=Alta  | F=Alta)        = "
          f"{p_carga_dado_fatiga('Alta','Alta'):.4f}")
    print(f"\n  Figura: {dibujar_barras()}")
