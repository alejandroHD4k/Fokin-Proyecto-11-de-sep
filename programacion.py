import random
from data import AEROPUERTOS, AVIONES
from flight import Flight

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def generar_vuelos_dia(dia, min_vuelos=3, max_vuelos=8):
    """
    Genera una lista de vuelos aleatorios para un día.

    Parámetros:
        dia (str): nombre del día de la semana.
        min_vuelos (int): mínimo de vuelos del día.
        max_vuelos (int): máximo de vuelos del día.

    Retorna:
        list[Flight]: vuelos generados para ese día.
    """
    vuelos = []
    cantidad = random.randint(min_vuelos, max_vuelos)
    prefijo = dia[:2].upper()   # "LU", "MA", "MI", ...

    for i in range(1, cantidad + 1):
        origen, destino = random.sample(list(AEROPUERTOS), 2)  # garantiza que sean distintos
        tipo_avion = random.choice(list(AVIONES))
        codigo = f"{prefijo}{i:03d}"  # ej. "LU001"
        vuelos.append(Flight(codigo, origen, destino, tipo_avion))

    return vuelos


def generar_programacion_semanal(min_vuelos=3, max_vuelos=8):
    """
    Genera los vuelos de toda la semana.

    Retorna:
        dict: {dia: [Flight, Flight, ...]}
    """
    return {dia: generar_vuelos_dia(dia, min_vuelos, max_vuelos) for dia in DIAS_SEMANA}


def buscar_vuelos(programacion, origen=None, destino=None, dia=None):
    """
    Busca vuelos en la programación. Los filtros que se dejen en None se ignoran.

    Retorna:
        list[tuple[str, Flight]]: lista de (dia, vuelo) que cumplen los filtros.
    """
    resultados = []
    for d, vuelos in programacion.items():
        if dia is not None and d != dia:
            continue
        for vuelo in vuelos:
            if origen is not None and vuelo.origen != origen:
                continue
            if destino is not None and vuelo.destino != destino:
                continue
            resultados.append((d, vuelo))
    return resultados

if __name__ == "__main__":
    semana = generar_programacion_semanal()
    for dia, vuelos in semana.items():
        print(f"\n=== {dia} ({len(vuelos)} vuelos) ===")
        for v in vuelos:
            print(v)

    print("\n--- Vuelos que salen de BOG ---")
    for dia, v in buscar_vuelos(semana, origen="BOG"):
        print(dia, "|", v)