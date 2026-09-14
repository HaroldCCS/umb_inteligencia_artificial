# -*- coding: utf-8 -*-
"""
strips.py — Planificacion STRIPS con motor de busqueda A*
==========================================================
Parcial Practico 1 — Inteligencia Artificial Clasica

Dominio: preparacion del atleta en los 5 dias previos al partido.

Incluye:
  - Representacion STRIPS (precondiciones / ADD / DELETE)   [Guia 5]
  - Busqueda FORWARD (encadenamiento hacia adelante)        [Guia 5]
  - Busqueda BACKWARD (regresion de metas)                  [Guia 5]
  - Deteccion de interferencias, acciones huerfanas y
    ANOMALIA DE SUSSMAN                                     [Guia 5]
  - Motor A* sobre el espacio de estados                    [Guia 4]
        -> lo pide explicitamente el profesor:
           "implementen el algoritmo de busqueda que identificaron
            como el mas eficiente (ej. A*)"

Genera: strips_graph.png
"""

import heapq

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import dominio as D


# ═══════════════════════════════════════════════════════════════════
# 1. REPRESENTACION STRIPS
# ═══════════════════════════════════════════════════════════════════
#
# Estructura exactamente la que sugiere el material de clase:
#
#   class Accion:
#       nombre, precondiciones, add, delete
#
#   aplicar:  nuevo_estado = (estado - delete) | add
#
# Se anade `co2_costo`: la huella metabolica de ejecutar la accion,
# que hace las veces de costo g(n) para el A*.
# ═══════════════════════════════════════════════════════════════════

class Accion:
    """Operador STRIPS: precondiciones, ADD, DELETE y costo."""

    def __init__(self, nombre, precondiciones, add, delete, co2_costo=1):
        self.nombre = nombre
        self.precondiciones = frozenset(precondiciones)
        self.add = frozenset(add)
        self.delete = frozenset(delete)
        self.co2_costo = co2_costo

    def es_aplicable(self, estado):
        """Las precondiciones deben cumplirse en el estado actual."""
        return self.precondiciones <= estado

    def aplicar(self, estado):
        """Axioma de persistencia: solo cambia lo que esta en ADD/DELETE."""
        if not self.es_aplicable(estado):
            return None
        return frozenset((estado - self.delete) | self.add)

    def __repr__(self):
        return f"Accion({self.nombre})"


# ═══════════════════════════════════════════════════════════════════
# 2. EL PROBLEMA
# ═══════════════════════════════════════════════════════════════════

ESTADO_INICIAL = frozenset({
    "atleta(fatigado)",
    "carga_semanal(alta)",
    "riesgo_lesion(elevado)",
    "rendimiento(bajo)",
    "co2_acumulado(alto)",
    "partido_en(5_dias)",
})

# Meta estandar: el atleta llega listo para competir.
META_BASE = frozenset({
    "atleta(recuperado)",
    "riesgo_lesion(bajo)",
    "rendimiento(alto)",
    "co2_acumulado(bajo)",
    "listo_para_competir",
})

# Meta conservadora: ademas exige reserva energetica.
# El agente la activa cuando la red bayesiana da una probabilidad
# de exito por debajo del umbral.
META_CONSERVADORA = META_BASE | {"reserva_energetica(alta)"}


ACCIONES = [
    Accion(
        nombre="Aplicar_Sesion_Regenerativa",
        precondiciones={"atleta(fatigado)", "carga_semanal(alta)"},
        add={"atleta(en_recuperacion)", "carga_semanal(moderada)"},
        delete={"atleta(fatigado)", "carga_semanal(alta)"},
        co2_costo=1,        # movilidad suave, gasto minimo
    ),
    Accion(
        nombre="Monitorear_Biomarcadores",
        precondiciones={"atleta(en_recuperacion)"},
        add={"datos_fisiologicos(disponibles)", "co2_acumulado(bajo)"},
        delete={"co2_acumulado(alto)"},
        co2_costo=1,        # accion pasiva: sensores GPS/IMU
    ),
    Accion(
        nombre="Aplicar_Descarga_Extra",
        precondiciones={"atleta(en_recuperacion)", "co2_acumulado(bajo)"},
        add={"reserva_energetica(alta)"},
        delete=set(),
        co2_costo=1,        # segunda sesion regenerativa
    ),
    Accion(
        nombre="Ajustar_Plan_Nutricional",
        precondiciones={"datos_fisiologicos(disponibles)",
                        "co2_acumulado(bajo)"},
        add={"nutricion(optimizada)", "atleta(recuperado)"},
        delete={"atleta(en_recuperacion)"},
        co2_costo=1,        # sin gasto fisico directo
    ),
    Accion(
        nombre="Ejecutar_Entrenamiento_Especifico",
        precondiciones={"atleta(recuperado)", "nutricion(optimizada)",
                        "co2_acumulado(bajo)"},
        add={"rendimiento(alto)", "riesgo_lesion(bajo)",
             "carga_semanal(optima)"},
        delete={"rendimiento(bajo)", "riesgo_lesion(elevado)",
                "carga_semanal(moderada)"},
        co2_costo=5,        # sprints y tactica de alta intensidad
    ),
    Accion(
        nombre="Validar_Estado_Competitivo",
        precondiciones={"rendimiento(alto)", "riesgo_lesion(bajo)",
                        "atleta(recuperado)"},
        add={"listo_para_competir"},
        delete=set(),
        co2_costo=1,        # evaluacion medica
    ),
]

COSTO_MIN_ACCION = min(a.co2_costo for a in ACCIONES)


# ═══════════════════════════════════════════════════════════════════
# 3. BUSQUEDA FORWARD  (encadenamiento hacia adelante)
# ═══════════════════════════════════════════════════════════════════
#
# "Si estoy aqui, que puedo hacer?"
# Aplica la primera accion cuyas precondiciones se cumplan.
# Es el planificador LINEAL simple del material de clase, y sirve
# para exhibir su debilidad (ver seccion 6: anomalia de Sussman).
# ═══════════════════════════════════════════════════════════════════

def busqueda_forward(estado_inicial, meta, acciones, max_pasos=20):
    """
    Devuelve SIEMPRE 5 elementos:
        (plan, estados, co2_total, exito, co2_historia)
    """
    estado = frozenset(estado_inicial)
    plan, estados = [], [estado]
    co2_total, co2_historia = 0, [0]

    for _ in range(max_pasos):
        if meta <= estado:
            break
        aplicada = False
        for accion in acciones:
            nuevo = accion.aplicar(estado)
            if nuevo is not None and nuevo != estado:
                plan.append(accion)
                estado = nuevo
                co2_total += accion.co2_costo
                co2_historia.append(co2_total)
                estados.append(estado)
                aplicada = True
                break
        if not aplicada:
            return plan, estados, co2_total, False, co2_historia

    return plan, estados, co2_total, meta <= estado, co2_historia


# ═══════════════════════════════════════════════════════════════════
# 4. BUSQUEDA BACKWARD  (regresion de metas)
# ═══════════════════════════════════════════════════════════════════
#
# "Para lograr esto, que debio pasar antes?"
# Se parte de la meta y se busca la accion cuyo efecto ADD la
# cumple; sus precondiciones pasan a ser las nuevas sub-metas.
# ═══════════════════════════════════════════════════════════════════

def busqueda_backward(meta, estado_inicial, acciones, max_pasos=20):
    """Devuelve (plan_invertido, historial_de_submetas, exito)."""
    submetas = frozenset(meta)
    plan, historial = [], [submetas]

    for _ in range(max_pasos):
        if submetas <= estado_inicial:
            return plan, historial, True

        # Predicados que todavia faltan por lograr
        pendientes = submetas - estado_inicial
        elegida = None
        for accion in reversed(acciones):
            if accion.add & pendientes:          # relevante para la meta
                elegida = accion
                break

        if elegida is None:
            return plan, historial, False

        # Regresion: quitamos lo que la accion produce y anadimos
        # sus precondiciones como nuevas sub-metas.
        submetas = frozenset((submetas - elegida.add) | elegida.precondiciones)
        plan.append(elegida)
        historial.append(submetas)

    return plan, historial, submetas <= estado_inicial


# ═══════════════════════════════════════════════════════════════════
# 5. MOTOR A*  sobre el espacio de estados
# ═══════════════════════════════════════════════════════════════════
#
# Requisito explicito del profesor (Guia 5, ACTIVIDAD 2):
#   "No van a dejar que el agente elija acciones al azar. Van a
#    implementar el algoritmo de busqueda que identificaron como
#    el mas eficiente (ej. A*)."
#
#   Nodo      = estado STRIPS completo (frozenset de predicados)
#   Sucesores = acciones aplicables, (estado - DELETE) | ADD
#   g(n)      = CO2 metabolico acumulado del plan
#   h(n)      = predicados de la meta que faltan x costo minimo
#
# ADMISIBILIDAD de h(n): ninguna accion de costo 1 aporta mas de
# UN predicado de la meta, y la unica que aporta varios
# (Ejecutar_Entrenamiento_Especifico, 2-3 predicados) cuesta 5.
# Por tanto h(n) nunca sobreestima el costo real -> A* es optimo.
# ═══════════════════════════════════════════════════════════════════

def heuristica(estado, meta):
    """h(n) = (predicados de la meta que faltan) x (costo minimo)."""
    return len(meta - estado) * COSTO_MIN_ACCION


def planificar_astar(estado_inicial, meta, acciones):
    """
    A* sobre el espacio de estados STRIPS.

    Devuelve un diccionario con el plan, su costo, los nodos
    expandidos y el arbol de busqueda (para dibujarlo).
    """
    inicio = frozenset(estado_inicial)
    meta = frozenset(meta)

    contador = 0                       # desempate estable en el heap
    frontera = [(heuristica(inicio, meta), 0, contador, inicio)]
    g_score = {inicio: 0}
    padre = {inicio: (None, None)}     # estado -> (estado_previo, accion)
    visitados = set()
    expandidos = 0
    aristas = []                       # (estado_origen, estado_destino, accion)

    while frontera:
        _, g, _, estado = heapq.heappop(frontera)
        if estado in visitados:
            continue
        visitados.add(estado)
        expandidos += 1

        if meta <= estado:
            # Reconstruccion del plan hacia atras
            plan, nodo = [], estado
            while padre[nodo][0] is not None:
                previo, accion = padre[nodo]
                plan.append(accion)
                nodo = previo
            plan.reverse()
            return {
                "plan":       plan,
                "costo":      g,
                "expandidos": expandidos,
                "visitados":  visitados,
                "aristas":    aristas,
                "padre":      padre,
                "estado_meta": estado,
                "exito":      True,
            }

        for accion in acciones:
            nuevo = accion.aplicar(estado)
            if nuevo is None or nuevo == estado:
                continue
            aristas.append((estado, nuevo, accion))
            tentativo = g + accion.co2_costo
            if tentativo < g_score.get(nuevo, float("inf")):
                g_score[nuevo] = tentativo
                padre[nuevo] = (estado, accion)
                contador += 1
                heapq.heappush(
                    frontera,
                    (tentativo + heuristica(nuevo, meta), tentativo,
                     contador, nuevo))

    return {"plan": [], "costo": float("inf"), "expandidos": expandidos,
            "visitados": visitados, "aristas": aristas, "padre": padre,
            "estado_meta": None, "exito": False}


# ═══════════════════════════════════════════════════════════════════
# 6. DETECCION DE BLOQUEOS E INTERFERENCIAS
# ═══════════════════════════════════════════════════════════════════

def detectar_interferencias(acciones):
    """Acciones cuyo DELETE borra una precondicion de otra accion."""
    return [(a.nombre, b.nombre, set(a.delete & b.precondiciones))
            for a in acciones for b in acciones
            if a.nombre != b.nombre and (a.delete & b.precondiciones)]


def detectar_huerfanas(acciones, meta):
    """Acciones cuyo ADD no aporta a la meta ni a otra precondicion."""
    utiles = set(meta)
    for a in acciones:
        utiles |= a.precondiciones
    return [a.nombre for a in acciones if not (a.add & utiles)]


def detectar_sussman(acciones, meta, estado_inicial):
    """
    Busca interferencias que son ANOMALIA DE SUSSMAN propiamente
    dicha: una accion necesaria para una sub-meta borra la
    precondicion de otra accion necesaria para OTRA sub-meta.

    Un planificador lineal que resuelva las sub-metas una por una
    puede quedar bloqueado para siempre.
    """
    casos = []
    for a in acciones:                       # la que "rompe"
        if not (a.add & meta):
            continue
        for b in acciones:                   # la que queda bloqueada
            if a.nombre == b.nombre or not (b.add & meta):
                continue
            borrado = a.delete & b.precondiciones
            if not borrado:
                continue
            # b solo se bloquea si esa precondicion no se puede
            # recuperar con otra accion posterior
            recuperable = any(
                c.add & borrado for c in acciones if c.nombre != a.nombre
                and not (c.precondiciones & borrado)
            )
            casos.append({
                "rompe": a.nombre,
                "bloquea": b.nombre,
                "predicado": set(borrado),
                "submeta_de_a": set(a.add & meta),
                "submeta_de_b": set(b.add & meta),
                "recuperable": recuperable,
            })
    return casos


def planificador_lineal(estado_inicial, meta, acciones, orden_submetas):
    """
    Planificador LINEAL al estilo del STRIPS original: resuelve las
    sub-metas UNA POR UNA, en el orden dado, sin intercalarlas.

    Es exactamente el planificador que falla ante la Anomalia de
    Sussman. Se usa para DEMOSTRARLA, no solo para afirmarla.

    Devuelve (plan, estado_final, exito, submeta_que_fallo).
    """
    estado = frozenset(estado_inicial)
    plan = []
    for submeta in orden_submetas:
        if {submeta} <= estado:
            continue
        r = planificar_astar(estado, {submeta}, acciones)
        if not r["exito"]:
            return plan, estado, False, submeta
        plan += r["plan"]
        for a in r["plan"]:
            estado = a.aplicar(estado)
    return plan, estado, frozenset(meta) <= estado, None


def demostrar_sussman(estado_inicial, meta, acciones):
    """
    Ejecuta el planificador lineal con dos ordenes de sub-metas
    opuestos y comprueba empiricamente que uno se bloquea.
    """
    submetas = sorted(meta)
    # Orden A: primero "atleta(recuperado)" -> rompe en_recuperacion
    orden_a = ["atleta(recuperado)"] + [m for m in submetas
                                        if m != "atleta(recuperado)"]
    # Orden B: primero la reserva energetica
    orden_b = ["reserva_energetica(alta)"] + [m for m in submetas
                                              if m != "reserva_energetica(alta)"] \
        if "reserva_energetica(alta)" in meta else submetas

    res = {}
    for nombre, orden in [("A", orden_a), ("B", orden_b)]:
        plan, estado, ok, fallo = planificador_lineal(
            estado_inicial, meta, acciones, orden)
        res[nombre] = {"orden": orden, "plan": plan, "exito": ok,
                       "fallo": fallo,
                       "co2": sum(a.co2_costo for a in plan)}
    return res


# ═══════════════════════════════════════════════════════════════════
# 7. VISUALIZACION — strips_graph.png
# ═══════════════════════════════════════════════════════════════════

# Predicados que resumen el estado para la etiqueta del nodo
_CLAVES = ["atleta", "co2_acumulado", "rendimiento", "riesgo_lesion",
           "reserva_energetica", "listo_para_competir"]

_CORTO = {
    "atleta(fatigado)": "fatigado",
    "atleta(en_recuperacion)": "en recup.",
    "atleta(recuperado)": "recuperado",
    "co2_acumulado(alto)": "CO2 alto",
    "co2_acumulado(bajo)": "CO2 bajo",
    "rendimiento(bajo)": "rend. bajo",
    "rendimiento(alto)": "REND. ALTO",
    "riesgo_lesion(elevado)": "riesgo alto",
    "riesgo_lesion(bajo)": "riesgo bajo",
    "reserva_energetica(alta)": "+reserva",
    "listo_para_competir": "LISTO",
}


def etiqueta_estado(estado):
    """Resumen legible de un estado (3-4 predicados clave)."""
    partes = []
    for clave in _CLAVES:
        for p in sorted(estado):
            if p.startswith(clave) and p in _CORTO:
                partes.append(_CORTO[p])
    return "\n".join(partes) if partes else "(vacio)"


def dibujar_grafo(resultado, estado_inicial, meta,
                  archivo="strips_graph.png", titulo_extra=""):
    """
    Grafo de estados del planificador.

      - Cada nodo es un estado (proposicion compuesta).
      - Cada arista es una accion STRIPS, etiquetada con su CO2.
      - La RUTA DEL PLAN queda resaltada en rojo y grueso.
      - Leyenda con estado inicial, meta y el plan completo.
    """
    inicio = frozenset(estado_inicial)
    plan = resultado["plan"]

    # Estados que forman el plan, en orden
    ruta_estados, estado = [inicio], inicio
    for accion in plan:
        estado = accion.aplicar(estado)
        ruta_estados.append(estado)
    en_ruta = set(ruta_estados)
    aristas_plan = {(ruta_estados[i], ruta_estados[i + 1])
                    for i in range(len(ruta_estados) - 1)}

    # Grafo con los estados que A* llego a expandir
    G = nx.DiGraph()
    explorados = resultado["visitados"] | en_ruta
    for origen, destino, accion in resultado["aristas"]:
        if origen in explorados and destino in explorados:
            G.add_edge(origen, destino, accion=accion)
    for e in explorados:
        G.add_node(e)

    # ── Posiciones: la ruta del plan en linea recta; el resto,
    #    repartido arriba y abajo segun su distancia al inicio ──
    pos, nivel_de = {}, {}
    for i, e in enumerate(ruta_estados):
        pos[e] = (i * 2.6, 0.0)
        nivel_de[e] = i

    otros = [e for e in G.nodes if e not in en_ruta]
    dist = nx.single_source_shortest_path_length(G, inicio)
    arriba = True
    contador_nivel = {}
    for e in sorted(otros, key=lambda s: (dist.get(s, 9), sorted(s))):
        d = dist.get(e, len(ruta_estados))
        k = contador_nivel.get(d, 0)
        contador_nivel[d] = k + 1
        signo = 1 if (k % 2 == 0) else -1
        pos[e] = (d * 2.6 + 0.30, signo * (1.25 + 0.75 * (k // 2)))
        arriba = not arriba

    fig, ax = plt.subplots(figsize=(19, 7.2))

    # ── Aristas ───────────────────────────────────────────────────
    for u, v, datos in G.edges(data=True):
        es_plan = (u, v) in aristas_plan
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(
                        arrowstyle="-|>",
                        color=D.ROJO if es_plan else "#C8CFD4",
                        lw=3.2 if es_plan else 1.0,
                        alpha=1.0 if es_plan else 0.55,
                        shrinkA=26, shrinkB=26,
                        connectionstyle="arc3,rad=0.0" if es_plan
                                        else "arc3,rad=0.16"),
                    zorder=1)
        if es_plan:
            a = datos["accion"]
            ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.30,
                    f"{a.nombre.replace('_', ' ')}\nCO2 = {a.co2_costo}",
                    fontsize=7.6, ha="center", va="bottom",
                    color=D.ROJO, fontweight="bold",
                    bbox=dict(boxstyle="round,pad=0.28", facecolor="white",
                              edgecolor=D.ROJO, alpha=0.95, linewidth=1.1),
                    zorder=4)

    # ── Nodos ─────────────────────────────────────────────────────
    for e in G.nodes:
        x, y = pos[e]
        es_inicio = (e == inicio)
        es_meta = meta <= e
        en_plan = e in en_ruta

        if es_inicio:
            color, borde = D.VERDE, D.VERDE
        elif es_meta:
            color, borde = D.NARANJA, D.NARANJA
        elif en_plan:
            color, borde = D.AZUL, D.ROJO
        else:
            color, borde = "#D5DBDB", D.GRIS

        ax.scatter([x], [y], s=3100 if en_plan else 1500, marker="o",
                   c=color, edgecolors=borde,
                   linewidths=3.0 if en_plan else 1.0,
                   zorder=2, alpha=1.0 if en_plan else 0.6)

        if en_plan:
            ax.text(x, y, etiqueta_estado(e), fontsize=6.4, ha="center",
                    va="center", color="white", fontweight="bold", zorder=3)

    # ── Leyenda: inicial, metas y plan ────────────────────────────
    txt_inicial = "ESTADO INICIAL  S0\n" + "\n".join(
        f"  · {p}" for p in sorted(inicio))
    txt_meta = "META  G\n" + "\n".join(f"  · {p}" for p in sorted(meta))
    txt_plan = f"PLAN ENCONTRADO  (A*, CO2 total = {resultado['costo']})\n" + \
        "\n".join(f"  {i}. {a.nombre.replace('_', ' ')}  [CO2 {a.co2_costo}]"
                  for i, a in enumerate(plan, 1))

    caja = dict(boxstyle="round,pad=0.55", facecolor="#FCFCFC",
                edgecolor=D.GRIS, linewidth=1.2)
    ax.text(0.005, -0.055, txt_inicial, transform=ax.transAxes, fontsize=7.4,
            va="top", ha="left", family="monospace",
            bbox=dict(caja, edgecolor=D.VERDE))
    ax.text(0.345, -0.055, txt_meta, transform=ax.transAxes, fontsize=7.4,
            va="top", ha="left", family="monospace",
            bbox=dict(caja, edgecolor=D.NARANJA))
    ax.text(0.655, -0.055, txt_plan, transform=ax.transAxes, fontsize=7.4,
            va="top", ha="left", family="monospace",
            bbox=dict(caja, edgecolor=D.ROJO))

    leyenda = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=D.VERDE,
               markersize=13, label="Estado inicial S0"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor=D.AZUL,
               markersize=13, label="Estado intermedio del plan"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor=D.NARANJA,
               markersize=13, label="Estado meta G"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#D5DBDB",
               markersize=11, label="Estado explorado y descartado"),
        Line2D([0], [0], color=D.ROJO, lw=3.2, label="RUTA DEL PLAN"),
    ]
    ax.legend(handles=leyenda, loc="upper center", ncol=5, fontsize=8.6,
              frameon=True, bbox_to_anchor=(0.5, 1.055))

    ax.set_title(
        f"Grafo de estados STRIPS — preparacion del atleta{titulo_extra}\n"
        f"Plan de {len(plan)} acciones  |  CO2 metabolico total = "
        f"{resultado['costo']} kg CO2eq  |  "
        f"estados expandidos por A* = {resultado['expandidos']}",
        fontsize=13, fontweight="bold", color=D.AZUL, pad=34)

    ax.set_xlim(-1.6, (len(ruta_estados) - 1) * 2.6 + 1.9)
    alto = max([abs(y) for _, y in pos.values()] + [1.4])
    ax.set_ylim(-alto - 0.85, alto + 0.85)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(archivo, dpi=135, bbox_inches="tight")
    plt.close()
    return archivo


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 74)
    print("  STRIPS — preparacion del atleta")
    print("=" * 74)

    for nombre, meta in [("META ESTANDAR", META_BASE),
                         ("META CONSERVADORA", META_CONSERVADORA)]:
        r = planificar_astar(ESTADO_INICIAL, meta, ACCIONES)
        print(f"\n  --- {nombre} ---")
        print(f"  Exito: {r['exito']}  |  CO2 total: {r['costo']}  |  "
              f"estados expandidos: {r['expandidos']}")
        for i, a in enumerate(r["plan"], 1):
            print(f"    {i}. {a.nombre:36} CO2 {a.co2_costo}")

    print("\n" + "=" * 74)
    print("  FORWARD vs BACKWARD (meta estandar)")
    print("=" * 74)
    plan_fw, _, co2_fw, ok_fw, _ = busqueda_forward(
        ESTADO_INICIAL, META_BASE, ACCIONES)
    print(f"  Forward : exito={ok_fw}  CO2={co2_fw}  "
          f"{[a.nombre for a in plan_fw]}")
    plan_bw, _, ok_bw = busqueda_backward(
        META_BASE, ESTADO_INICIAL, ACCIONES)
    print(f"  Backward: exito={ok_bw}  "
          f"{[a.nombre for a in reversed(plan_bw)]}")

    print("\n" + "=" * 74)
    print("  BLOQUEOS")
    print("=" * 74)
    for a, b, pred in detectar_interferencias(ACCIONES):
        print(f"  '{a}' borra {pred} que necesita '{b}'")
    print(f"  Huerfanas (meta estandar)    : "
          f"{detectar_huerfanas(ACCIONES, META_BASE)}")
    print(f"  Huerfanas (meta conservadora): "
          f"{detectar_huerfanas(ACCIONES, META_CONSERVADORA)}")
    print("\n  --- ANOMALIA DE SUSSMAN (demostracion empirica) ---")
    demo = demostrar_sussman(ESTADO_INICIAL, META_CONSERVADORA, ACCIONES)
    for k, v in demo.items():
        print(f"  Orden {k}: primero '{v['orden'][0]}'")
        print(f"     exito={v['exito']}  pasos={len(v['plan'])}  CO2={v['co2']}")
        if not v["exito"]:
            print(f"     BLOQUEADO al intentar: {v['fallo']}")
    r_ast = planificar_astar(ESTADO_INICIAL, META_CONSERVADORA, ACCIONES)
    print(f"  A* (intercala sub-metas): exito={r_ast['exito']}  "
          f"pasos={len(r_ast['plan'])}  CO2={r_ast['costo']}")

    r = planificar_astar(ESTADO_INICIAL, META_BASE, ACCIONES)
    print("\n  Figura:", dibujar_grafo(r, ESTADO_INICIAL, META_BASE))
