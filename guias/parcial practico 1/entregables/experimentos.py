# -*- coding: utf-8 -*-
"""
experimentos.py — Los dos bloques extra del enunciado
======================================================
Parcial Practico 1 — Inteligencia Artificial Clasica

BLOQUE 1 — Comparacion de heuristicas y poda en Min-Max
   (i) Min-Max basico  (ii) + alfa-beta  (iii) + heuristica disenada
   en 3 escenarios x profundidades {2, 3, 4}
   midiendo tiempo, nodos expandidos y decision escogida.

BLOQUE 2 — Analisis de sensibilidad bayesiano
   Se varia el prior P(C=Alta) y se vuelve a correr el flujo completo
   del agente (observe -> posterior -> plan -> decide).

Ejecutar:  python experimentos.py
Genera:    resultados_bloque1.csv, resultados_bloque2.csv,
           sensibilidad.png
"""

import pandas as pd

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import agente
import bayes
import dominio as D
import minmax
import strips


REPETICIONES = 300     # para que la medida de tiempo sea estable


# ═══════════════════════════════════════════════════════════════════
# BLOQUE 1 — Heuristicas y poda
# ═══════════════════════════════════════════════════════════════════

VERSIONES = [
    ("(i)  Min-Max basico",        dict(poda=False, heuristica=False)),
    ("(ii) Min-Max + alfa-beta",   dict(poda=True,  heuristica=False)),
    ("(iii) Min-Max + heuristica", dict(poda=False, heuristica=True)),
    ("(iii+) heuristica + poda",   dict(poda=True,  heuristica=True)),
]


def medir(profundidad, delta, **kwargs):
    """Ejecuta varias veces para estabilizar la medida de tiempo."""
    r = minmax.decidir(profundidad=profundidad, delta=delta, **kwargs)
    total = 0.0
    for _ in range(REPETICIONES):
        total += minmax.decidir(profundidad=profundidad, delta=delta,
                                **kwargs)["tiempo_ms"]
    r["tiempo_ms"] = total / REPETICIONES
    return r


def bloque1():
    filas = []
    escenarios = [("0. Base (Guia 5)", D.ESCENARIO_BASE, "")] + [
        (nombre, datos["delta"], datos["desc"])
        for nombre, datos in D.ESCENARIOS.items()
    ]

    for nombre_esc, delta, _ in escenarios:
        for prof in (2, 3, 4):
            for nombre_ver, cfg in VERSIONES:
                r = medir(prof, delta, **cfg)
                filas.append({
                    "Escenario":   nombre_esc,
                    "Profundidad": prof,
                    "Version":     nombre_ver,
                    "Tiempo (ms)": round(r["tiempo_ms"], 4),
                    "Nodos":       r["nodos"],
                    "Hojas eval.": r["hojas"],
                    "Podas":       r["podas"],
                    "Decision":    r["decision"],
                    "Rama":        r["rama"].replace("_", " "),
                    "Valor":       round(r["valor"], 1),
                })
    return pd.DataFrame(filas)


def informe_bloque1(df):
    D.log("=" * 78)
    D.log("  BLOQUE 1 — COMPARACION DE HEURISTICAS Y PODA EN MIN-MAX")
    D.log("=" * 78)

    for esc in df["Escenario"].unique():
        sub = df[df["Escenario"] == esc]
        D.log(f"\n  ### {esc}")
        D.log(sub.drop(columns=["Escenario", "Rama"]).to_string(index=False))

    D.log("\n" + "=" * 78)
    D.log("  ANALISIS")
    D.log("=" * 78)

    # (a) alfa-beta debe dar SIEMPRE la misma decision que el basico
    fallos = []
    for esc in df["Escenario"].unique():
        for prof in (2, 3, 4):
            s = df[(df["Escenario"] == esc) & (df["Profundidad"] == prof)]
            basico = s[s["Version"].str.startswith("(i) ")]
            abeta = s[s["Version"].str.startswith("(ii)")]
            if (basico["Decision"].iloc[0] != abeta["Decision"].iloc[0]
                    or basico["Valor"].iloc[0] != abeta["Valor"].iloc[0]):
                fallos.append((esc, prof))

    D.log("\n  1) CORRECCION DE LA PODA ALFA-BETA")
    if not fallos:
        D.log("     La poda da EXACTAMENTE la misma decision y el mismo valor")
        D.log("     que la version basica en los 12 casos. Es la garantia")
        D.log("     teorica del algoritmo: alfa-beta no cambia el resultado,")
        D.log("     solo evita evaluar lo que no puede cambiarlo.")
    else:
        D.log(f"     ERROR: difieren en {fallos}")

    # (b) cuanto ahorra la poda
    base = df[df["Version"].str.startswith("(i) ")]["Nodos"].sum()
    con_poda = df[df["Version"].str.startswith("(ii)")]["Nodos"].sum()
    D.log(f"\n  2) AHORRO DE LA PODA")
    D.log(f"     Nodos totales sin poda : {base}")
    D.log(f"     Nodos totales con poda : {con_poda}")
    D.log(f"     Ahorro                 : "
          f"{100*(base-con_poda)/base:.1f} %")

    # (c) la heuristica, cambia la decision?
    D.log(f"\n  3) EFECTO DE LA HEURISTICA DISENADA")
    cambios = []
    for esc in df["Escenario"].unique():
        for prof in (2, 3, 4):
            s = df[(df["Escenario"] == esc) & (df["Profundidad"] == prof)]
            ing = s[s["Version"].str.startswith("(i) ")]["Decision"].iloc[0]
            heu = s[s["Version"].str.startswith("(iii) ")]["Decision"].iloc[0]
            if ing != heu:
                cambios.append((esc, prof, ing, heu))

    if cambios:
        D.log("     La decision CAMBIA en estos casos:")
        for esc, prof, ing, heu in cambios:
            D.log(f"       {esc:26} prof={prof}: "
                  f"ingenua -> {ing:9} | heuristica -> {heu}")
        profs_cambio = sorted({c[1] for c in cambios})
        D.log("")
        D.log(f"     Solo difieren a profundidad {profs_cambio}. De "
              f"profundidad 3 en")
        D.log("     adelante ambas coinciden.")
        D.log("")
        D.log("     Lectura: a profundidad 2 la busqueda se corta JUSTO")
        D.log("     despues de la respuesta de fatiga, sin llegar a ver que")
        D.log("     el cuerpo tecnico todavia puede DESCANSAR al jugador.")
        D.log("")
        D.log("     - La evaluacion INGENUA solo mira el rendimiento, y como")
        D.log("       la carga moderada rinde mas que la baja, la elige sin")
        D.log("       enterarse del desgaste que implica.")
        D.log("     - La HEURISTICA disenada si ve el CO2 metabolico, el")
        D.log("       riesgo de lesion y la recuperacion. Como en ese")
        D.log("       horizonte corto no puede contar todavia con el")
        D.log("       descanso como mitigacion, se protege bajando la carga.")
        D.log("")
        D.log("     Cual es MEJOR? A profundidad 2 la heuristica es mas")
        D.log("     prudente pero mas conservadora de lo necesario: acierta")
        D.log("     al penalizar el desgaste y se equivoca al no saber que")
        D.log("     habia una salida mejor un nivel mas abajo. La leccion no")
        D.log("     es que una evaluacion sea superior a la otra, sino que")
        D.log("     NINGUNA heuristica compensa cortar la busqueda demasiado")
        D.log("     pronto.")
    else:
        D.log("     No hay cambios de decision entre ambas evaluaciones.")

    # (d) efecto de la profundidad
    D.log(f"\n  4) EFECTO DE LA PROFUNDIDAD")
    for esc in df["Escenario"].unique():
        s = df[(df["Escenario"] == esc)
               & df["Version"].str.startswith("(iii+)")]
        decs = list(s.sort_values("Profundidad")["Rama"])
        distintas = len(set(decs)) > 1
        D.log(f"     {esc:26} "
              f"{'CAMBIA con la profundidad' if distintas else 'estable'}")
        for prof, rama in zip((2, 3, 4), decs):
            D.log(f"         prof={prof}: {rama}")
    D.log("")
    D.log("     El cambio ocurre entre profundidad 2 y 3, y a partir de")
    D.log("     ahi la decision se ESTABILIZA:")
    D.log("")
    D.log("       prof 2 -> Carga Baja")
    D.log("                 El agente no alcanza a ver el nivel de DECISION,")
    D.log("                 asi que no sabe que puede descansar al jugador.")
    D.log("                 Sin esa salida, la unica forma de protegerlo es")
    D.log("                 entrenarlo menos.")
    D.log("")
    D.log("       prof 3 -> Carga Moderada + Descansar")
    D.log("                 Al ver un nivel mas descubre una combinacion")
    D.log("                 mejor: mantener la carga util de entrenamiento y")
    D.log("                 proteger al atleta el fin de semana. Valor")
    D.log("                 garantizado +19 frente a los +13.7 de la carga")
    D.log("                 baja.")
    D.log("")
    D.log("       prof 4 -> la MISMA decision")
    D.log("                 Anadir la respuesta fisica (molestia muscular)")
    D.log("                 baja el valor garantizado, porque MIN siempre")
    D.log("                 concede la molestia, pero NO cambia que hacer.")
    D.log("")
    D.log("     Conclusion: el horizonte minimo util para este problema es")
    D.log("     3 niveles. Con 2 el agente toma una decision peor por no")
    D.log("     ver la mitigacion disponible; con 4 no gana nada nuevo y")
    D.log("     paga 64 nodos en vez de 28. Para la demo en vivo, por tanto,")
    D.log("     profundidad 3 es la configuracion correcta.")


# ═══════════════════════════════════════════════════════════════════
# BLOQUE 2 — Sensibilidad bayesiana
# ═══════════════════════════════════════════════════════════════════

PRIORS = [0.10, 0.25, 0.40, 0.60, 0.80]
EVIDENCIA = {"F": "Alta", "fuente": "barrido de sensibilidad"}


def bloque2():
    filas = []
    for p in PRIORS:
        p_c = {"Alta": p, "Moderada": 1 - p}
        res = agente.ejecutar(evidencia=EVIDENCIA, p_c=p_c,
                              verbose=False, escribir_log=False)
        post = res["posterior"]
        filas.append({
            "P(C=Alta) prior":   p,
            "P(C=Alta|F=Alta)":  round(post["diagnostico"], 4),
            "P(E=Exito|F=Alta)": round(post["exito"], 4),
            "Supera umbral":     "SI" if not res["conservador"] else "NO",
            "Meta STRIPS":       ("conservadora" if res["conservador"]
                                  else "estandar"),
            "Pasos del plan":    len(res["plan"]["plan"]),
            "CO2 del plan":      res["plan"]["costo"],
            "Decision Min-Max":  res["decision"]["decision"],
            "Valor":             round(res["decision"]["valor"], 1),
        })
    return pd.DataFrame(filas)


def informe_bloque2(df):
    D.log("\n\n" + "=" * 78)
    D.log("  BLOQUE 2 — ANALISIS DE SENSIBILIDAD BAYESIANO")
    D.log("=" * 78)
    D.log(f"\n  Evidencia fija en todas las corridas: F = Alta (atleta fatigado)")
    D.log(f"  Umbral del agente: {D.UMBRAL_EXITO}")
    D.log("")
    D.log(df.to_string(index=False))

    D.log("\n" + "=" * 78)
    D.log("  ANALISIS")
    D.log("=" * 78)

    # Donde cambia la decision
    cambios = []
    for i in range(1, len(df)):
        if df["Meta STRIPS"].iloc[i] != df["Meta STRIPS"].iloc[i - 1]:
            cambios.append((df["P(C=Alta) prior"].iloc[i - 1],
                            df["P(C=Alta) prior"].iloc[i]))

    D.log("\n  1) IMPACTO EN EL POSTERIOR")
    D.log(f"     El posterior P(E=Exito|F=Alta) baja de "
          f"{df['P(E=Exito|F=Alta)'].max()*100:.1f} % a "
          f"{df['P(E=Exito|F=Alta)'].min()*100:.1f} % al mover el prior de "
          f"{df['P(C=Alta) prior'].min()} a {df['P(C=Alta) prior'].max()}.")
    D.log(f"     Es un rango de "
          f"{(df['P(E=Exito|F=Alta)'].max()-df['P(E=Exito|F=Alta)'].min())*100:.1f}"
          f" puntos porcentuales: el prior SI importa.")

    D.log("\n  2) IMPACTO EN EL PLAN DE STRIPS")
    if cambios:
        for a, b in cambios:
            D.log(f"     La meta cambia entre prior={a} y prior={b}.")
        D.log(f"     Por debajo de ese punto el agente usa el plan estandar")
        D.log(f"     (5 acciones, CO2 9). Por encima exige reserva energetica")
        D.log(f"     y el plan pasa a 6 acciones (CO2 10).")
    else:
        D.log("     El plan no cambia en todo el rango barrido.")

    D.log("\n  3) IMPACTO EN LA DECISION DE MIN-MAX")
    if df["Decision Min-Max"].nunique() == 1:
        D.log(f"     NINGUNO: la decision es '{df['Decision Min-Max'].iloc[0]}'")
        D.log(f"     en los {len(df)} casos. Era esperable: Min-Max no usa")
        D.log(f"     probabilidades, razona sobre el peor caso. El prior")
        D.log(f"     bayesiano no lo toca.")
        D.log(f"     Esto es una PROPIEDAD, no un defecto: significa que la")
        D.log(f"     recomendacion de carga es robusta a errores de")
        D.log(f"     estimacion. Lo que si se mueve es el PLAN de preparacion.")
    else:
        D.log("     La decision de Min-Max cambia a lo largo del barrido.")

    D.log("\n  4) ESTABILIDAD vs FRAGILIDAD")
    if cambios:
        a, b = cambios[0]
        D.log(f"     FRAGIL en la zona prior ~{a}-{b}: ahi una diferencia")
        D.log(f"     pequena de creencia sobre la carga aplicada cambia el")
        D.log(f"     plan del atleta.")
        D.log(f"     ESTABLE de prior={b} en adelante: da igual afinar el")
        D.log(f"     numero, el agente siempre protege al atleta.")
        D.log("")
        D.log(f"     Conclusion practica: el dato que hay que registrar con")
        D.log(f"     rigor es la CARGA SEMANAL REALMENTE APLICADA. Si el")
        D.log(f"     cuerpo tecnico cree que casi nunca aplica cargas altas,")
        D.log(f"     el agente se confia. Todo lo demas el modelo lo aguanta.")


def grafica_sensibilidad(df, archivo="sensibilidad.png"):
    fig, ax = plt.subplots(figsize=(11, 6))

    x = df["P(C=Alta) prior"]
    y = df["P(E=Exito|F=Alta)"] * 100
    colores = [D.VERDE if s == "SI" else D.NARANJA
               for s in df["Supera umbral"]]

    ax.plot(x, y, "-", color=D.AZUL, lw=2.5, zorder=1)
    ax.scatter(x, y, s=190, c=colores, edgecolors="white", linewidths=2,
               zorder=2)
    for xi, yi, meta in zip(x, y, df["Meta STRIPS"]):
        ax.annotate(f"{yi:.1f} %\n{meta}", (xi, yi),
                    textcoords="offset points", xytext=(0, 15),
                    ha="center", fontsize=8.5, fontweight="bold",
                    color=D.AZUL)

    ax.axhline(D.UMBRAL_EXITO * 100, color=D.ROJO, ls="--", lw=2)
    ax.annotate(f"umbral del agente = {D.UMBRAL_EXITO*100:.0f} %",
                xy=(0.795, D.UMBRAL_EXITO * 100 + 0.8), ha="right",
                fontsize=9.5, color=D.ROJO, fontweight="bold")

    ax.fill_between([0.05, 0.85], 0, D.UMBRAL_EXITO * 100,
                    color=D.NARANJA, alpha=0.07)
    ax.fill_between([0.05, 0.85], D.UMBRAL_EXITO * 100, 60,
                    color=D.VERDE, alpha=0.07)
    ax.text(0.82, D.UMBRAL_EXITO * 100 - 2.2, "plan CONSERVADOR",
            ha="right", va="top", fontsize=9, color=D.NARANJA,
            fontweight="bold")
    ax.text(0.82, D.UMBRAL_EXITO * 100 + 2.2, "plan estandar",
            ha="right", va="bottom", fontsize=9, color=D.VERDE,
            fontweight="bold")

    ax.set_xlabel("Prior  P(C = Alta)   —  cada cuanto se aplica carga alta",
                  fontsize=11, fontweight="bold")
    ax.set_ylabel("Posterior  P(E = Exito | F = Alta)   [%]",
                  fontsize=11, fontweight="bold")
    ax.set_title("Analisis de sensibilidad bayesiano\n"
                 "Evidencia fija: F = Alta (atleta fatigado)",
                 fontsize=13, fontweight="bold", color=D.AZUL, pad=14)
    ax.set_xlim(0.05, 0.85)
    ax.set_ylim(20, 50)
    ax.grid(alpha=0.3)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(archivo, dpi=140, bbox_inches="tight")
    plt.close()
    return archivo


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    D.limpiar_log()

    df1 = bloque1()
    informe_bloque1(df1)
    df1.to_csv("resultados_bloque1.csv", index=False, encoding="utf-8")

    df2 = bloque2()
    informe_bloque2(df2)
    df2.to_csv("resultados_bloque2.csv", index=False, encoding="utf-8")

    fig = grafica_sensibilidad(df2)

    D.guardar_log("experimentos_log.txt")
    print(f"\n>> resultados_bloque1.csv  ({len(df1)} filas)")
    print(f">> resultados_bloque2.csv  ({len(df2)} filas)")
    print(f">> {fig}")
    print(f">> experimentos_log.txt")
