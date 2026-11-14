import random
from data import AEROPUERTOS, AVIONES
from flight import Vuelo

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def generar_vuelos_dia(dia):
    """
    Genera una lista de vuelos aleatorios para un día.

    Parámetros:
        dia (str): nombre del día de la semana.
    Retorna:
        list[Vuelo]: vuelos generados para ese día.
    """
    
    #Creamos una lista vacia para ir llenando con cada vuelo generado
    vuelos = []

    #Cantidad aleatoria de vuelos para el día
    cantidad = random.randint(2, 10)

    #Generamos un prefijo para el código del vuelo basado en el día de la semana
    prefijo = dia[:2]

    #Generamos los vuelos con origen, destino y tipo de avión aleatorios
    for i in range(1, cantidad + 1):
        origen, destino = random.sample(list(AEROPUERTOS), 2)  # Crea una lista con dos aeropuertos distintos- 
        tipo_avion = random.choice(list(AVIONES)) #Escogemos un avión aleatorio de la lista de aviones
        capacidad = AVIONES[tipo_avion]["pasajeros_tipicos"]
        asientos_vendidos = random.randint(0, capacidad)
        codigo = f"{prefijo}{i:03d}"  # Generamos un código de vuelo único para cada vuelo, dependendo del día y el número de vuelo 
        vuelos.append(Vuelo(codigo, origen, destino, tipo_avion, asientos_vendidos)) #Agregamos el vuelo a la lista de vuelos del día 

    return vuelos


def generar_programacion_semanal():
    """
    Genera los vuelos de toda la semana.

    Retorna:
        dict: {dia: [Vuelo, Vuelo, ...]}
    """
    return {dia: generar_vuelos_dia(dia) for dia in DIAS_SEMANA}


def buscar_vuelos(programacion, origen=None, destino=None, dia=None):
    """
    Busca vuelos en la programación. Los filtros que se dejen en None se ignoran.

    Retorna:
        list[tuple[str, Vuelo]]: lista de (dia, vuelo) que cumplen los filtros.
    """

    #Crear una lista vacía para ir llenando con los vuelos que cumplan los filtros
    resultados = []

    #Dos variables, que son el día y la lista de vuelos de ese día, que se van a ir recorriendo en el diccionario de programación
    for d, vuelos in programacion.items():
        #Si se especifica un día, solo se buscan vuelos en ese día
        if dia is not None and d != dia:
            continue

        #Iteramos sobre los vuelos del día, y si cumplen los filtros de origen y destino, se agregan a la lista de resultados
        for vuelo in vuelos:

            #Filtramos por origen y destino, si se especifica alguno de ellos
            if origen is not None and vuelo.origen != origen:
                continue
            if destino is not None and vuelo.destino != destino:
                continue
            resultados.append((d, vuelo))
    return resultados

def obtener_vuelo(programacion, codigo):
    """Retorna el vuelo con ese código, o None si no existe."""
    for vuelos in programacion.values():
        for vuelo in vuelos:
            if vuelo.codigo == codigo:
                return vuelo
    return None