# -*- coding: utf-8 -*-
"""
dominio.py — Base compartida del agente integrador
===================================================
Parcial Practico 1 — Inteligencia Artificial Clasica
Sector: Rendimiento deportivo / gestion de carga del atleta

Este modulo concentra TODO lo que los tres metodos comparten:
metricas, funcion de utilidad, escenarios y constantes ajustables.

Los otros modulos (bayes, strips, minmax, agente) lo importan.
Nada se redefine dos veces.

--------------------------------------------------------------------
PARAMETROS AJUSTABLES  —  cambiar aqui y volver a ejecutar
--------------------------------------------------------------------
"""

# ═══════════════════════════════════════════════════════════════════
# CONSTANTES AJUSTABLES
# ═══════════════════════════════════════════════════════════════════

LAMBDA = 1.0      # peso del CO2 metabolico en la funcion de utilidad
                  # (Guia 5: con LAMBDA >= 1.5 la mejor hoja cambia
                  #  de "Jugar" a "Descansar")

UMBRAL_EXITO = 0.40   # si P(E=Exito | evidencia) cae por debajo,
                      # el agente cambia a la meta conservadora

PROFUNDIDAD = 3       # profundidad por defecto del Min-Max

# Pesos de la funcion de utilidad (Guia 5, con sus fuentes)
W_RENDIMIENTO = 4     # Catapult GPS/IMU — eficacia tactica
W_CO2         = 2     # GHG Protocol adaptado a deporte
W_RIESGO      = 3     # UEFA Medical Matters (2021)
W_RECUPERACION= 2     # Kinexon — HRV y sueno profundo


# ═══════════════════════════════════════════════════════════════════
# 1. FUNCION DE UTILIDAD  (identica a la de la Guia 5)
# ═══════════════════════════════════════════════════════════════════

def utilidad(rendimiento, co2, riesgo_lesion, recuperacion, lam=None):
    """
    U = (Rendimiento x 4) - (CO2 x 2 x lambda)
        - (Riesgo_lesion x 3) + (Recuperacion x 2)

    Todas las variables en escala 0-10.
    """
    lam = LAMBDA if lam is None else lam
    return (rendimiento   * W_RENDIMIENTO
            - co2         * W_CO2 * lam
            - riesgo_lesion * W_RIESGO
            + recuperacion  * W_RECUPERACION)


def utilidad_vector(v, lam=None):
    """Utilidad de un vector de metricas (rend, co2, riesgo, recup)."""
    return utilidad(v[0], v[1], v[2], v[3], lam)


def utilidad_ingenua(v):
    """
    Evaluacion INGENUA: mira solo el rendimiento.

    Es lo que haria un cuerpo tecnico sin datos: "el que mejor
    rinde hoy, juega". Ignora CO2, riesgo de lesion y recuperacion.
    Se usa como funcion de corte del Min-Max basico, para poder
    compararla contra nuestra heuristica disenada.
    """
    return v[0] * W_RENDIMIENTO


# ═══════════════════════════════════════════════════════════════════
# 2. ARBOL DE DECISION — opciones de cada nivel
# ═══════════════════════════════════════════════════════════════════
#
#   Nivel 1 (MAX)  Cuerpo tecnico  -> Carga de entrenamiento
#   Nivel 2 (MIN)  Organismo       -> Fatiga con la que responde
#   Nivel 3 (MAX)  Cuerpo tecnico  -> Uso del jugador
#   Nivel 4 (MIN)  Organismo       -> Respuesta fisica posterior
#
# Los niveles 1 y 3 son MAX porque los decide el cuerpo tecnico.
# Los niveles 2 y 4 son MIN porque los "decide" el cuerpo del
# atleta, que en Min-Max se modela como adversario perfecto.
# ═══════════════════════════════════════════════════════════════════

OPC_CARGA     = ["Alta", "Moderada", "Baja"]
OPC_FATIGA    = ["Alta", "Baja"]
OPC_DECISION  = ["Jugar", "Jugar_parcial", "Descansar"]
OPC_RESPUESTA = ["Molestia", "Sin_molestia"]

NIVELES = [
    ("MAX", "Carga",     OPC_CARGA),
    ("MIN", "Fatiga",    OPC_FATIGA),
    ("MAX", "Decision",  OPC_DECISION),
    ("MIN", "Respuesta", OPC_RESPUESTA),
]

PROFUNDIDAD_MAXIMA = len(NIVELES)

# Subconjunto que reproduce EXACTAMENTE el arbol de la Guia 5.
# Sirve como test de regresion (ver test_regresion.py).
OPCIONES_GUIA5 = {
    "Carga":    ["Alta", "Moderada"],
    "Fatiga":   ["Alta", "Baja"],
    "Decision": ["Jugar", "Descansar"],
}


# ═══════════════════════════════════════════════════════════════════
# 3. VECTORES DE METRICAS POR ESTADO
# ═══════════════════════════════════════════════════════════════════
#
# Cada combinacion (Carga, Fatiga, Decision) produce un vector
#     (rendimiento, co2, riesgo_lesion, recuperacion)
#
# Las 8 combinaciones marcadas [G5] son LITERALMENTE las de la
# Guia 5 (estimaciones del cuerpo tecnico sobre datos GPS/IMU).
# Las demas corresponden a las opciones que anadimos para poder
# explorar profundidad 4 ("Carga Baja" y "Jugar_parcial").
# ═══════════════════════════════════════════════════════════════════

METRICAS_N3 = {
    # ── Carga ALTA ────────────────────────  rend co2 riesgo recup
    ("Alta", "Alta", "Jugar"):          (3,  8,  9,  2),   # [G5] U=-27
    ("Alta", "Alta", "Jugar_parcial"):  (3,  6,  7,  4),
    ("Alta", "Alta", "Descansar"):      (2,  4,  5,  7),   # [G5] U= -1
    ("Alta", "Baja", "Jugar"):          (7,  7,  6,  4),   # [G5] U= +4
    ("Alta", "Baja", "Jugar_parcial"):  (6,  5,  4,  6),
    ("Alta", "Baja", "Descansar"):      (5,  3,  3,  8),   # [G5] U=+21

    # ── Carga MODERADA ────────────────────
    ("Moderada", "Alta", "Jugar"):         (6,  5,  5,  5),  # [G5] U= +9
    ("Moderada", "Alta", "Jugar_parcial"): (5,  4,  4,  6),
    ("Moderada", "Alta", "Descansar"):     (4,  2,  3,  8),  # [G5] U=+19
    ("Moderada", "Baja", "Jugar"):         (9,  3,  2,  9),  # [G5] U=+42
    ("Moderada", "Baja", "Jugar_parcial"): (8,  2,  2,  9),
    ("Moderada", "Baja", "Descansar"):     (7,  1,  1,  9),  # [G5] U=+41

    # ── Carga BAJA (opcion anadida) ───────
    # El atleta llega fresco pero sin ritmo competitivo: el
    # rendimiento cae aunque el riesgo sea minimo.
    ("Baja", "Alta", "Jugar"):          (4,  4,  4,  6),
    ("Baja", "Alta", "Jugar_parcial"):  (4,  3,  3,  7),
    ("Baja", "Alta", "Descansar"):      (3,  2,  2,  8),
    ("Baja", "Baja", "Jugar"):          (6,  2,  2,  9),
    ("Baja", "Baja", "Jugar_parcial"):  (6,  2,  1,  9),
    ("Baja", "Baja", "Descansar"):      (5,  1,  1, 10),
}


# ── Nivel 4: la respuesta fisica modifica el vector ──────────────
#
# El castigo de una molestia muscular es PROPORCIONAL A LA
# EXPOSICION: reventarse jugando 90 minutos duele mucho mas que
# aparecer tras una sesion de descanso.
#
# Este es el motivo por el que la profundidad importa: el dano
# no aparece el mismo dia de la decision.

DELTA_RESPUESTA = {
    ("Jugar",         "Molestia"):     (-2, +1, +4, -3),
    ("Jugar_parcial", "Molestia"):     (-1,  0, +2, -1),
    ("Descansar",     "Molestia"):     ( 0,  0, +1, -1),
    ("Jugar",         "Sin_molestia"): ( 0,  0,  0, +1),
    ("Jugar_parcial", "Sin_molestia"): ( 0,  0,  0, +1),
    ("Descansar",     "Sin_molestia"): ( 0,  0,  0, +1),
}


# ═══════════════════════════════════════════════════════════════════
# 4. ESCENARIOS  (para el experimento de comparacion)
# ═══════════════════════════════════════════════════════════════════
#
# Cada escenario es un desplazamiento del vector base del atleta.
# Representan tres momentos reales de una temporada.
# ═══════════════════════════════════════════════════════════════════

ESCENARIOS = {
    "1. Atleta fresco": {
        "delta": (0, -1, -1, +2),
        "desc": "Inicio de microciclo: CO2 acumulado bajo y buena "
                "recuperacion tras dia libre.",
    },
    "2. Atleta cargado": {
        "delta": (-1, +3, +1, -2),
        "desc": "48 h despues de partido: CO2 metabolico acumulado "
                "alto y recuperacion incompleta.",
    },
    "3. Historial de lesion": {
        "delta": (-1, 0, +3, -1),
        "desc": "Atleta con lesion muscular en los ultimos 3 meses: "
                "riesgo de recaida elevado.",
    },
}

# Escenario neutro: reproduce exactamente la Guia 5.
ESCENARIO_BASE = (0, 0, 0, 0)


def _clamp(x):
    """Las metricas viven en la escala 0-10."""
    return max(0, min(10, x))


def aplicar_delta(vector, delta):
    """Suma un delta al vector y recorta a la escala 0-10."""
    return tuple(_clamp(v + d) for v, d in zip(vector, delta))


# ═══════════════════════════════════════════════════════════════════
# 5. VECTOR DE UN ESTADO CUALQUIERA DEL ARBOL
# ═══════════════════════════════════════════════════════════════════
#
# Un estado se identifica por su RUTA: la tupla de decisiones
# tomadas hasta llegar a el.
#
#   ()                                     -> raiz
#   ("Moderada",)                          -> tras elegir carga
#   ("Moderada","Alta")                    -> tras la respuesta de fatiga
#   ("Moderada","Alta","Descansar")        -> tras decidir el uso
#   ("Moderada","Alta","Descansar","Molestia") -> hoja
#
# Para los niveles 1 y 2 (donde todavia no hay un vector medido)
# se usa el PROMEDIO de los vectores alcanzables desde ahi. Es un
# valor precalculado una sola vez al importar el modulo: la
# heuristica solo hace una consulta de diccionario, NO expande el
# arbol.
# ═══════════════════════════════════════════════════════════════════

def _promedio(vectores):
    n = len(vectores)
    return tuple(sum(v[i] for v in vectores) / n for i in range(4))


# Nivel 2: promedio sobre las decisiones posibles
METRICAS_N2 = {
    (c, f): _promedio([METRICAS_N3[(c, f, d)] for d in OPC_DECISION])
    for c in OPC_CARGA for f in OPC_FATIGA
}

# Nivel 1: promedio sobre las respuestas de fatiga
METRICAS_N1 = {
    c: _promedio([METRICAS_N2[(c, f)] for f in OPC_FATIGA])
    for c in OPC_CARGA
}

# Nivel 0 (raiz): promedio global
METRICAS_N0 = _promedio(list(METRICAS_N1.values()))


def vector_estado(ruta, delta_escenario=ESCENARIO_BASE):
    """
    Vector de metricas del estado identificado por `ruta`,
    ajustado por el escenario.
    """
    n = len(ruta)
    if n == 0:
        base = METRICAS_N0
    elif n == 1:
        base = METRICAS_N1[ruta[0]]
    elif n == 2:
        base = METRICAS_N2[(ruta[0], ruta[1])]
    elif n == 3:
        base = METRICAS_N3[(ruta[0], ruta[1], ruta[2])]
    elif n == 4:
        base = aplicar_delta(
            METRICAS_N3[(ruta[0], ruta[1], ruta[2])],
            DELTA_RESPUESTA[(ruta[2], ruta[3])],
        )
    else:
        raise ValueError(f"Ruta demasiado larga: {ruta}")

    return aplicar_delta(base, delta_escenario)


def etiqueta_movimiento(ruta):
    """Nombre legible del ultimo movimiento de la ruta."""
    if not ruta:
        return "Inicio"
    nivel = len(ruta) - 1
    _, nombre_nivel, _ = NIVELES[nivel]
    return f"{nombre_nivel}: {ruta[-1].replace('_', ' ')}"


# ═══════════════════════════════════════════════════════════════════
# 6. PALETA DE COLORES  (la misma de las Guias 5 y 6)
# ═══════════════════════════════════════════════════════════════════

ROJO     = "#E74C3C"
VERDE    = "#27AE60"
AZUL     = "#2980B9"
AMARILLO = "#F1C40F"
GRIS     = "#95A5A6"
NARANJA  = "#E67E22"
MORADO   = "#8E44AD"
FONDO    = "#F7F7F7"


# ═══════════════════════════════════════════════════════════════════
# 7. UTILIDAD DE REGISTRO (log a consola Y a archivo)
# ═══════════════════════════════════════════════════════════════════

ARCHIVO_LOG = "agent_log.txt"
_buffer_log = []


def log(texto=""):
    """Imprime en consola y acumula para agent_log.txt."""
    print(texto)
    _buffer_log.append(texto)


def guardar_log(ruta=ARCHIVO_LOG):
    """Vuelca el buffer acumulado al archivo de registro."""
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(_buffer_log) + "\n")
    return ruta


def limpiar_log():
    _buffer_log.clear()


# ═══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 66)
    print("  DOMINIO — Gestion de carga del atleta")
    print("=" * 66)
    print(f"\n  Funcion de utilidad:")
    print(f"    U = (Rend x {W_RENDIMIENTO}) - (CO2 x {W_CO2} x {LAMBDA})"
          f" - (Riesgo x {W_RIESGO}) + (Recup x {W_RECUPERACION})")
    print(f"\n  Niveles del arbol:")
    for i, (jug, nom, opc) in enumerate(NIVELES, 1):
        print(f"    Nivel {i} ({jug:3}) {nom:10} -> {', '.join(opc)}")
    print(f"\n  Hojas a profundidad maxima: "
          f"{len(OPC_CARGA)*len(OPC_FATIGA)*len(OPC_DECISION)*len(OPC_RESPUESTA)}")

    print(f"\n  Verificacion contra la Guia 5 (escenario base):")
    print(f"    {'Combinacion':<40} {'Vector':<18} {'U':>7}")
    print("    " + "-" * 66)
    for c in OPCIONES_GUIA5["Carga"]:
        for f in OPCIONES_GUIA5["Fatiga"]:
            for d in OPCIONES_GUIA5["Decision"]:
                v = vector_estado((c, f, d))
                print(f"    {c+' + '+f+' + '+d:<40} {str(v):<18} "
                      f"{utilidad_vector(v):>7.0f}")
