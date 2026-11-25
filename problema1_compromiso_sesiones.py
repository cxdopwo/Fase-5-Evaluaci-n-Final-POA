# Nombre del estudiante: Jehison Steven Naranjo Peña
# Grupo: 213022_1173
# Tutor: Diomar Antonio Pineda Cervantes
# Programa: Ingeniería en Inteligencia Artificial y Ciencia de Datos
# Código Fuente: autoría propia
# Curso: Fundamentos de Programación (213022)
# Fase 5: Evaluación Final POA
# Problema 1: Clasificación del nivel de compromiso de sesiones

"""
Evalúa el compromiso de sesiones de clientes almacenadas en una matriz
[ID, duración en segundos, número de clics].

Clasificación:
- Alto:  duración > 180  y  clics > 8
- Bajo:  duración < 60   o   clics < 3
- Medio: cualquier otro caso

Integra constantes, arreglo bidimensional, función con parámetros y retorno,
selección (if) y repetición (for), alineado con los resultados de aprendizaje
del curso (Deitel y Deitel, 2016; Ceballos Sierra, 2015).
"""

# ---------------------------------------------------------------------------
# CONSTANTES (umbrales de negocio)
# ---------------------------------------------------------------------------
DURACION_ALTO = 180
CLICS_ALTO = 8
DURACION_BAJO = 60
CLICS_BAJO = 3

# Matriz de sesiones: [ID del cliente, duración (s), clics] — mínimo 5 filas
SESIONES = [
    ["C001", 240, 12],   # Alto:  240 > 180 y 12 > 8
    ["C002", 45, 10],    # Bajo:  45 < 60
    ["C003", 200, 2],    # Bajo:  2 < 3  (aunque duración sea alta)
    ["C004", 90, 5],     # Medio
    ["C005", 300, 9],    # Alto:  300 > 180 y 9 > 8
    ["C006", 150, 8],    # Medio: clics = 8, no cumple > 8
]


def clasificar_compromiso(duracion, clics):
    """Retorna 'Alto', 'Bajo' o 'Medio' según duración y clics.

    Parameters
    ----------
    duracion : int o float
        Duración de la sesión en segundos.
    clics : int
        Número de clics registrados en la sesión.

    Returns
    -------
    str
        Nivel de compromiso: Alto, Bajo o Medio.
    """
    if duracion > DURACION_ALTO and clics > CLICS_ALTO:
        return "Alto"
    if duracion < DURACION_BAJO or clics < CLICS_BAJO:
        return "Bajo"
    return "Medio"


def generar_informe(matriz_sesiones):
    """Recorre la matriz, clasifica cada sesión e imprime el informe."""
    print("=" * 60)
    print("  INFORME DE COMPROMISO DE SESIONES")
    print("=" * 60)
    print("ID cliente    Duración (s)    Clics    Clasificación")
    print("-" * 60)

    total_alto = 0
    total_medio = 0
    total_bajo = 0

    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        nivel = clasificar_compromiso(duracion, clics)

        if nivel == "Alto":
            total_alto = total_alto + 1
        elif nivel == "Medio":
            total_medio = total_medio + 1
        else:
            total_bajo = total_bajo + 1

        print(
            str(id_cliente).ljust(13)
            + str(duracion).ljust(16)
            + str(clics).ljust(9)
            + nivel
        )

    print("-" * 60)
    print(
        "Resumen: Alto =", total_alto,
        "| Medio =", total_medio,
        "| Bajo =", total_bajo,
    )
    print("Total de sesiones analizadas:", len(matriz_sesiones))
    print("=" * 60)
    return total_alto, total_medio, total_bajo


def prueba_escritorio():
    """Muestra el razonamiento de dos casos borde (para la sustentación)."""
    print("\n--- Prueba de escritorio ---")
    print("C003: duración=200, clics=2")
    print("  200 > 180? Sí, pero clics > 8? No → no es Alto.")
    print("  200 < 60? No; clics < 3? Sí → Bajo (condición OR).")
    print("  Resultado:", clasificar_compromiso(200, 2))
    print("C006: duración=150, clics=8")
    print("  150 > 180? No → no es Alto.")
    print("  150 < 60? No; clics < 3? No → Medio.")
    print("  Resultado:", clasificar_compromiso(150, 8))


def main():
    """Punto de entrada: informe y prueba de escritorio."""
    generar_informe(SESIONES)
    prueba_escritorio()


if __name__ == "__main__":
    main()
