# -*- coding: utf-8 -*-
"""
minmax.py — Min-Max, poda alfa-beta y heuristica de evaluacion
===============================================================
Parcial Practico 1 — Inteligencia Artificial Clasica

Implementa las TRES versiones que pide el enunciado:

  (i)   Min-Max basico      -> sin poda, evaluacion INGENUA en el corte
  (ii)  Min-Max + alfa-beta -> misma evaluacion, con poda
  (iii) Min-Max + heuristica-> nuestra funcion de utilidad completa
                               (opcionalmente tambien con poda)

y mide, para cada una: tiempo, nodos expandidos y decision escogida.

Genera: minmax_tree.png
"""

import math
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

import dominio as D


# ═══════════════════════════════════════════════════════════════════
# 1. FUNCIONES DE EVALUACION
# ═══════════════════════════════════════════════════════════════════
#
# Cuando la busqueda se corta antes de llegar a una hoja real, hay
# que estimar el valor del estado. Ahi es donde se diferencian las
# tres versiones del enunciado.
# ═══════════════════════════════════════════════════════════════════

def eval_ingenua(ruta, delta):
    """
    Evaluacion INGENUA (versiones i y ii).

    Mira UNICAMENTE el rendimiento: "el que mejor rinde, juega".
    Ignora CO2 metabolico, riesgo de lesion y recuperacion.
    Es la decision de un cuerpo tecnico sin datos.
    """
    return D.utilidad_ingenua(D.vector_estado(ruta, delta))


def eval_heuristica(ruta, delta):
    """
    Heuristica DISENADA (version iii).

    Aplica la funcion de utilidad completa de la Guia 5 al vector
    de metricas del estado:

        U = (Rend x 4) - (CO2 x 2 x lambda) - (Riesgo x 3) + (Recup x 2)

    Para estados internos (niveles 1 y 2) el vector es un valor
    PRECALCULADO en dominio.py, asi que estimar cuesta una consulta
    de diccionario: no se expande ni un solo nodo extra.

    Es el mismo papel que jugaba h(n) en el A* de la Guia 4:
    estimar lo que falta sin recorrerlo.
    """
    return D.utilidad_vector(D.vector_estado(ruta, delta))


# ═══════════════════════════════════════════════════════════════════
# 2. EL ALGORITMO
# ═══════════════════════════════════════════════════════════════════

class Contador:
    """Instrumentacion de una ejecucion de Min-Max."""

    def __init__(self):
        self.nodos_expandidos = 0    # llamadas a minimax()
        self.hojas_evaluadas = 0     # veces que se aplico la evaluacion
        self.podas = 0               # cortes alfa-beta efectuados
        self.rutas_podadas = set()   # subarboles no explorados
        self.valores = {}            # ruta -> valor calculado


def _opciones_nivel(nivel, opciones):
    """Opciones disponibles en un nivel, respetando restricciones."""
    _, nombre, por_defecto = D.NIVELES[nivel]
    return opciones.get(nombre, por_defecto) if opciones else por_defecto


def minimax(ruta, profundidad, alpha, beta, cnt,
            evaluar=eval_heuristica, delta=D.ESCENARIO_BASE,
            poda=True, opciones=None):
    """
    Min-Max con poda alfa-beta opcional.

    Devuelve (valor, mejor_ruta_completa).

    Parametros
    ----------
    ruta         : tupla de decisiones tomadas hasta este nodo
    profundidad  : cuantos niveles mas se permite expandir
    alpha        : mejor valor asegurado para MAX hasta ahora
    beta         : mejor valor asegurado para MIN hasta ahora
    cnt          : objeto Contador (instrumentacion)
    evaluar      : funcion de evaluacion para los cortes
    delta        : desplazamiento del escenario
    poda         : activar/desactivar alfa-beta
    opciones     : dict para restringir las opciones de cada nivel
    """
    cnt.nodos_expandidos += 1
    nivel = len(ruta)

    # ── Caso base: hoja real o corte por profundidad ──────────────
    if nivel >= D.PROFUNDIDAD_MAXIMA or profundidad == 0:
        cnt.hojas_evaluadas += 1
        valor = evaluar(ruta, delta)
        cnt.valores[ruta] = valor
        return valor, ruta

    jugador, _, _ = D.NIVELES[nivel]
    hijos = _opciones_nivel(nivel, opciones)

    mejor_ruta = None

    if jugador == "MAX":
        mejor_val = -math.inf
        for i, opcion in enumerate(hijos):
            val, sub = minimax(ruta + (opcion,), profundidad - 1,
                               alpha, beta, cnt, evaluar, delta,
                               poda, opciones)
            if val > mejor_val:
                mejor_val, mejor_ruta = val, sub

            alpha = max(alpha, mejor_val)

            if poda and alpha >= beta:
                # Poda beta: MIN nunca dejara que lleguemos aqui
                cnt.podas += 1
                for restante in hijos[i + 1:]:
                    cnt.rutas_podadas.add(ruta + (restante,))
                break
    else:  # MIN
        mejor_val = math.inf
        for i, opcion in enumerate(hijos):
            val, sub = minimax(ruta + (opcion,), profundidad - 1,
                               alpha, beta, cnt, evaluar, delta,
                               poda, opciones)
            if val < mejor_val:
                mejor_val, mejor_ruta = val, sub

            beta = min(beta, mejor_val)

            if poda and alpha >= beta:
                # Poda alfa: MAX ya tiene algo mejor en otra rama
                cnt.podas += 1
                for restante in hijos[i + 1:]:
                    cnt.rutas_podadas.add(ruta + (restante,))
                break

    cnt.valores[ruta] = mejor_val
    return mejor_val, mejor_ruta


# ═══════════════════════════════════════════════════════════════════
# 3. INTERFAZ DE ALTO NIVEL
# ═══════════════════════════════════════════════════════════════════

def decidir(profundidad=D.PROFUNDIDAD, poda=True, heuristica=True,
            delta=D.ESCENARIO_BASE, opciones=None):
    """
    Ejecuta Min-Max y devuelve un diccionario con el resultado
    completo y sus metricas de rendimiento.
    """
    evaluar = eval_heuristica if heuristica else eval_ingenua
    cnt = Contador()

    t0 = time.perf_counter()
    valor, ruta = minimax((), profundidad, -math.inf, math.inf, cnt,
                          evaluar, delta, poda, opciones)
    t1 = time.perf_counter()

    return {
        "valor":       valor,
        "ruta":        ruta,
        "decision":    ruta[0] if ruta else None,
        "rama":        " -> ".join(ruta),
        "nodos":       cnt.nodos_expandidos,
        "hojas":       cnt.hojas_evaluadas,
        "podas":       cnt.podas,
        "podadas":     cnt.rutas_podadas,
        "valores":     cnt.valores,
        "tiempo_ms":   (t1 - t0) * 1000,
        "version":     ("heuristica" if heuristica else "ingenua")
                       + ("+poda" if poda else ""),
        "profundidad": profundidad,
    }


# ═══════════════════════════════════════════════════════════════════
# 4. VISUALIZACION — minmax_tree.png
# ═══════════════════════════════════════════════════════════════════

def _construir_layout(profundidad, opciones=None):
    """Posiciones (x, y) de cada nodo del arbol, por orden de hojas."""
    pos, hojas = {}, []

    def recorrer(ruta):
        nivel = len(ruta)
        if nivel >= D.PROFUNDIDAD_MAXIMA or nivel == profundidad:
            pos[ruta] = [len(hojas), -nivel]
            hojas.append(ruta)
            return [len(hojas) - 1]
        xs = []
        for opcion in _opciones_nivel(nivel, opciones):
            xs += recorrer(ruta + (opcion,))
        pos[ruta] = [sum(xs) / len(xs), -nivel]
        return xs

    recorrer(())
    return pos, hojas


def dibujar_arbol(profundidad=D.PROFUNDIDAD, delta=D.ESCENARIO_BASE,
                  opciones=None, titulo_extra="",
                  archivo="minmax_tree.png"):
    """
    Dibuja el arbol Min-Max cumpliendo los tres requisitos del
    enunciado:

      1. TODOS los nodos y hojas muestran su valor evaluado.
      2. La rama escogida por el agente queda resaltada.
      3. Cada arista lleva la etiqueta del movimiento que representa.

    Ademas, los nodos que la poda alfa-beta descarto se dibujan en
    gris, para que se vea cuanto ahorro.
    """
    # (a) Corrida SIN poda -> valores de absolutamente todos los nodos
    completo = decidir(profundidad, poda=False, heuristica=True,
                       delta=delta, opciones=opciones)
    # (b) Corrida CON poda -> que subarboles se descartaron
    podado = decidir(profundidad, poda=True, heuristica=True,
                     delta=delta, opciones=opciones)

    valores = completo["valores"]
    rama_elegida = podado["ruta"]
    pos, hojas = _construir_layout(profundidad, opciones)

    def esta_podado(ruta):
        return any(ruta[:k] in podado["podadas"] for k in range(len(ruta) + 1))

    fig, ax = plt.subplots(figsize=(max(15, len(hojas) * 1.25), 8.2))

    # ── Aristas ───────────────────────────────────────────────────
    for ruta in pos:
        if not ruta:
            continue
        padre = ruta[:-1]
        x0, y0 = pos[padre]
        x1, y1 = pos[ruta]

        en_rama = (rama_elegida[:len(ruta)] == ruta)
        gris = esta_podado(ruta)

        color = D.ROJO if en_rama else (D.GRIS if gris else "#BDC3C7")
        ancho = 3.4 if en_rama else (1.0 if gris else 1.6)
        estilo = ":" if gris and not en_rama else "-"

        ax.plot([x0, x1], [y0, y1], color=color, linewidth=ancho,
                linestyle=estilo, zorder=1,
                alpha=0.45 if gris and not en_rama else 1.0)

        # Etiqueta del movimiento sobre la arista.
        # Se escalona segun el indice del hijo para que no se pisen
        # cuando un nodo tiene tres opciones.
        hermanos = _opciones_nivel(len(ruta) - 1, opciones)
        idx = hermanos.index(ruta[-1])
        t = 0.38 + 0.20 * (idx % 3)
        ax.text(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t,
                ruta[-1].replace("_", " "),
                fontsize=6.8, rotation=0, ha="center", va="center",
                color=D.ROJO if en_rama else "#5D6D7E",
                fontweight="bold" if en_rama else "normal",
                bbox=dict(boxstyle="round,pad=0.18", facecolor="white",
                          edgecolor="none", alpha=0.9), zorder=2)

    # ── Nodos ─────────────────────────────────────────────────────
    for ruta, (x, y) in pos.items():
        nivel = len(ruta)
        es_hoja = (nivel >= D.PROFUNDIDAD_MAXIMA or nivel == profundidad)
        jugador = "MAX" if nivel == 0 else D.NIVELES[nivel - 1][0]
        # el tipo del nodo lo marca QUIEN decide EN el, no quien llego
        tipo = "HOJA" if es_hoja else D.NIVELES[nivel][0]

        gris = esta_podado(ruta)
        en_rama = (rama_elegida[:len(ruta)] == ruta)

        if gris:
            color, borde = "#D5D8DC", D.GRIS
        elif tipo == "MAX":
            color, borde = D.AZUL, D.AZUL
        elif tipo == "MIN":
            color, borde = D.NARANJA, D.NARANJA
        else:
            color, borde = D.VERDE, D.VERDE

        marca = {"MAX": "^", "MIN": "v", "HOJA": "s"}[tipo]
        ax.scatter([x], [y], s=960 if not es_hoja else 780,
                   marker=marca, c=color, edgecolors=D.ROJO if en_rama else borde,
                   linewidths=3.0 if en_rama else 1.4, zorder=3)

        # VALOR EVALUADO — requisito explicito del enunciado
        v = valores.get(ruta)
        txt = f"{v:.0f}" if v is not None else "—"
        ax.text(x, y, txt, ha="center", va="center", fontsize=8.2,
                fontweight="bold", color="white", zorder=4)

    # ── Etiquetas de nivel a la izquierda ─────────────────────────
    # Cada fila se nombra por LO QUE SE DECIDE EN ELLA, no por lo
    # que se decidio para llegar.
    for i in range(profundidad):
        jugador, nombre_nivel, _ = D.NIVELES[i]
        quien = "cuerpo tecnico" if jugador == "MAX" else "organismo"
        ax.text(-1.5, -i,
                f"Nivel {i+1} — {nombre_nivel.upper()}\n({jugador}: {quien})",
                fontsize=8, ha="right", va="center",
                color=D.AZUL if jugador == "MAX" else D.NARANJA,
                fontweight="bold")
    ax.text(-1.5, -profundidad, "HOJAS\nutilidad evaluada",
            fontsize=8, ha="right", va="center",
            color=D.VERDE, fontweight="bold")

    # ── Leyenda ───────────────────────────────────────────────────
    leyenda = [
        Line2D([0], [0], marker="^", color="w", markerfacecolor=D.AZUL,
               markersize=13, label="Nodo MAX — decide el cuerpo tecnico"),
        Line2D([0], [0], marker="v", color="w", markerfacecolor=D.NARANJA,
               markersize=13, label="Nodo MIN — responde el organismo"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor=D.VERDE,
               markersize=12, label="Hoja — utilidad evaluada"),
        Line2D([0], [0], color=D.ROJO, lw=3.4,
               label="RAMA ESCOGIDA por el agente"),
        Patch(facecolor="#D5D8DC", edgecolor=D.GRIS,
              label=f"Podado por alfa-beta ({podado['podas']} cortes)"),
    ]
    ax.legend(handles=leyenda, loc="lower center", ncol=5, fontsize=8.5,
              frameon=True, bbox_to_anchor=(0.5, -0.05))

    # ── Titulo ────────────────────────────────────────────────────
    ahorro = 100 * (completo["nodos"] - podado["nodos"]) / completo["nodos"]
    ax.set_title(
        f"Arbol Min-Max con poda alfa-beta — gestion de carga del atleta"
        f"{titulo_extra}\n"
        f"Decision: {podado['rama']}   |   valor garantizado = "
        f"{podado['valor']:+.0f}   |   "
        f"nodos {completo['nodos']} -> {podado['nodos']} ({ahorro:.0f} % menos)",
        fontsize=12.5, fontweight="bold", color=D.AZUL, pad=16)

    ax.set_xlim(-4.2, len(hojas) - 0.3)
    ax.set_ylim(-profundidad - 0.42, 0.55)
    ax.axis("off")
    plt.tight_layout()
    plt.savefig(archivo, dpi=135, bbox_inches="tight")
    plt.close()
    return archivo, podado, completo


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 74)
    print("  MIN-MAX + PODA ALFA-BETA — gestion de carga del atleta")
    print("=" * 74)

    r = decidir(profundidad=3, poda=True, heuristica=True)
    print(f"\n  Decision           : {r['rama']}")
    print(f"  Valor garantizado  : {r['valor']:+.1f}")
    print(f"  Nodos expandidos   : {r['nodos']}")
    print(f"  Podas realizadas   : {r['podas']}")
    print(f"  Tiempo             : {r['tiempo_ms']:.3f} ms")

    archivo, pod, comp = dibujar_arbol()
    print(f"\n  Figura guardada    : {archivo}")
    print(f"  Sin poda {comp['nodos']} nodos  ->  con poda {pod['nodos']} nodos")
