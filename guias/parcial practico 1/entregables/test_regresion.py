# -*- coding: utf-8 -*-
"""
test_regresion.py — Comprobaciones automaticas
===============================================
Parcial Practico 1 — Inteligencia Artificial Clasica

Verifica que el codigo sigue dando los mismos resultados que las
guias anteriores. Si algo aqui falla, hay un error.

Ejecutar:  python test_regresion.py
"""

import dominio as D
import bayes
import minmax
import strips

fallos = []


def comprobar(nombre, obtenido, esperado, tol=1e-6):
    ok = (abs(obtenido - esperado) < tol
          if isinstance(esperado, (int, float)) else obtenido == esperado)
    print(f"  [{'OK ' if ok else 'FALLA'}] {nombre:52} "
          f"{obtenido}  (esperado {esperado})")
    if not ok:
        fallos.append(nombre)


print("=" * 84)
print("  TESTS DE REGRESION")
print("=" * 84)

# ══ 1. Las 8 hojas de la Guia 5 ══════════════════════════════════
print("\n  1. UTILIDADES DE LA GUIA 5  (arbol Min-Max original)")
esperadas_g5 = {
    ("Alta", "Alta", "Jugar"): -27,       ("Alta", "Alta", "Descansar"): -1,
    ("Alta", "Baja", "Jugar"): 4,         ("Alta", "Baja", "Descansar"): 21,
    ("Moderada", "Alta", "Jugar"): 9,     ("Moderada", "Alta", "Descansar"): 19,
    ("Moderada", "Baja", "Jugar"): 42,    ("Moderada", "Baja", "Descansar"): 41,
}
for ruta, esperado in esperadas_g5.items():
    comprobar(" + ".join(ruta),
              D.utilidad_vector(D.vector_estado(ruta)), esperado)

# ══ 2. El resultado Min-Max de la Guia 5 ═════════════════════════
print("\n  2. RESULTADO MIN-MAX DE LA GUIA 5  (opciones restringidas)")
sin = minmax.decidir(3, poda=False, heuristica=True,
                     opciones=D.OPCIONES_GUIA5)
con = minmax.decidir(3, poda=True, heuristica=True,
                     opciones=D.OPCIONES_GUIA5)
comprobar("valor de la raiz", con["valor"], 19)
comprobar("rama escogida", con["rama"], "Moderada -> Alta -> Descansar")
comprobar("hojas evaluadas SIN poda", sin["hojas"], 8)
comprobar("hojas evaluadas CON poda", con["hojas"], 6)
comprobar("podas alfa-beta", con["podas"], 2)
comprobar("poda no cambia la decision", con["ruta"] == sin["ruta"], True)
comprobar("poda no cambia el valor", con["valor"], sin["valor"])

# ══ 3. La red bayesiana de la Guia 6 ═════════════════════════════
print("\n  3. RED BAYESIANA DE LA GUIA 6")
comprobar("CPTs validas (suman 1)", bayes.validar_cpts(), True)
comprobar("P(Moderada, Baja, Exito)",
          round(bayes.p_conjunta("Moderada", "Baja", "Exito"), 5), 0.357)
comprobar("P(Alta, Alta, Exito)",
          round(bayes.p_conjunta("Alta", "Alta", "Exito"), 5), 0.075)
comprobar("P(E=Exito) marginal", round(bayes.p_exito_marginal(), 4), 0.578)
comprobar("P(E=Exito | C=Moderada)",
          round(bayes.p_exito_dado_carga("Moderada"), 4), 0.73)
comprobar("P(E=Exito | C=Alta)",
          round(bayes.p_exito_dado_carga("Alta"), 4), 0.35)
comprobar("P(E=Exito | F=Alta)",
          round(bayes.p_exito_dado_fatiga("Alta"), 4), 0.325)
comprobar("P(E=Exito | F=Baja)",
          round(bayes.p_exito_dado_fatiga("Baja"), 4), 0.8115)
comprobar("P(C=Alta | F=Alta) diagnostico",
          round(bayes.p_carga_dado_fatiga("Alta", "Alta"), 4), 0.625)

# ══ 4. Planificacion STRIPS ══════════════════════════════════════
print("\n  4. PLANIFICACION STRIPS + A*")
est = strips.planificar_astar(strips.ESTADO_INICIAL, strips.META_BASE,
                              strips.ACCIONES)
cons = strips.planificar_astar(strips.ESTADO_INICIAL,
                               strips.META_CONSERVADORA, strips.ACCIONES)
comprobar("plan estandar: exito", est["exito"], True)
comprobar("plan estandar: numero de acciones", len(est["plan"]), 5)
comprobar("plan estandar: CO2 total", est["costo"], 9)
comprobar("plan conservador: numero de acciones", len(cons["plan"]), 6)
comprobar("plan conservador: CO2 total", cons["costo"], 10)
comprobar("A* mejora a la busqueda forward greedy",
          est["costo"] < strips.busqueda_forward(
              strips.ESTADO_INICIAL, strips.META_BASE,
              strips.ACCIONES)[2], True)

# El cerrojo del CO2: el entrenamiento debe ir DESPUES del monitoreo
nombres = [a.nombre for a in est["plan"]]
comprobar("el monitoreo precede al entrenamiento",
          nombres.index("Monitorear_Biomarcadores")
          < nombres.index("Ejecutar_Entrenamiento_Especifico"), True)

# ══ 5. Anomalia de Sussman ═══════════════════════════════════════
print("\n  5. ANOMALIA DE SUSSMAN  (planificador lineal)")
demo = strips.demostrar_sussman(strips.ESTADO_INICIAL,
                                strips.META_CONSERVADORA, strips.ACCIONES)
comprobar("orden A (recuperado primero) se BLOQUEA",
          demo["A"]["exito"], False)
comprobar("orden A se bloquea en reserva_energetica",
          demo["A"]["fallo"], "reserva_energetica(alta)")
comprobar("orden B (reserva primero) tiene exito", demo["B"]["exito"], True)
comprobar("A* resuelve lo que el lineal no", cons["exito"], True)

# ══ Resumen ══════════════════════════════════════════════════════
print("\n" + "=" * 84)
if fallos:
    print(f"  {len(fallos)} PRUEBA(S) FALLIDA(S): {fallos}")
    raise SystemExit(1)
print("  TODAS LAS PRUEBAS PASAN")
print("=" * 84)
