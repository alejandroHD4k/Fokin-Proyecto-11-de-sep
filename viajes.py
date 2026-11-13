import math
from data import AEROPUERTOS, AVIONES

def calcular_distancia(aeropuerto1, aeropuerto2):
    """
    Calcula la distancia entre dos aeropuertos utilizando la fórmula de Haversine.
    
    Parámetros:
    aeropuerto1 (str): Código IATA del primer aeropuerto.
    aeropuerto2 (str): Código IATA del segundo aeropuerto.
    
    Retorna:
    float: Distancia en kilómetros entre los dos aeropuertos.
    """

    # Validación de los códigos de aeropuerto
    if aeropuerto1 not in AEROPUERTOS or aeropuerto2 not in AEROPUERTOS:
        raise ValueError("Código de Aeropuerto no válido")
    if aeropuerto1 == aeropuerto2:
        raise ValueError("Los códigos de aeropuerto no pueden ser iguales")

    #Convertimos las coordenadas en variables, nos devuelve dos variables porque las coordenadas son tuplas de latitud y longitud
    lat1, lon1 = AEROPUERTOS[aeropuerto1.upper()]["coordenadas"] 
    lat2, lon2 = AEROPUERTOS[aeropuerto2.upper()]["coordenadas"]
    
    # Convertir grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Fórmula de Haversine
    dlon = lon2_rad - lon1_rad #Distania entre las dos longitudes
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + (math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(dlon / 2)**2))
    c = 2 * math.asin(math.sqrt(a)) 
    
    distancia = 6371 * c #Ese es el radio de la tierra en km, para obtener la distancia en km
    return round(distancia, 2)  # Redondeamos a dos decimales

def calcular_emisiones(distancia, tipo_avion, pasajeros):
    """
    Calcula las emisiones de CO₂ para un vuelo segun su distancia, pasajeros y un tipo de avión específico.
    
    Parámetros:
    distancia (float): Distancia entre los aeropuertos en kilómetros.
    tipo_avion (str): Tipo de avión utilizado para el vuelo.
    pasajeros (int): Número de pasajeros en el vuelo.
    Retorna:
    float: Emisiones de CO₂ en kilogramos para el vuelo.
    """
    
    # Obtener las emisiones por pasajero-kilómetro para el tipo de avión
    factor_emision = AVIONES[tipo_avion]["factor_emision"]
    
    # Calcular las emisiones totales
    emisiones_totales = distancia * factor_emision * pasajeros
    
    return round(emisiones_totales, 2)  # Redondeamos a dos decimales

def calcular_precio_base(distancia):
    """
    Calcula el precio base del vuelo según la distancia.
    
    Parámetros:
    distancia (float): Distancia entre los aeropuertos en kilómetros.
    
    Retorna:
    float: Precio base del vuelo en dólares.
    """

    # Definir un precio base por kilómetro
    precio_por_km = 350  # Precio base por kilómetro en dólares
    
    # Calcular el precio base
    precio_base = round(80000 + (distancia * precio_por_km), 2)
    return precio_base

def calcular_precio_dinamico(precio_base, ocupacion):
    """
    Aplica un recargo al precio base según el porcentaje de ocupación del vuelo.

    Parámetros:
        precio_base (float): precio base del tiquete en COP.
        ocupacion (float): porcentaje de ocupación del vuelo (0 a 100).

    Retorna:
        float: precio final en COP.
    """
    if ocupacion < 50:
        recargo = 1.00
    elif ocupacion < 70:
        recargo = 1.15
    elif ocupacion < 85:
        recargo = 1.40
    else:
        recargo = 1.80
    
    return round(precio_base * recargo, 2)  # Redondeamos a dos decimales


base = calcular_precio_base(calcular_distancia("BOG", "BGA"))
print(base)                                  # precio base
print(calcular_precio_dinamico(base, 30))    # sin recargo
print(calcular_precio_dinamico(base, 90)) 