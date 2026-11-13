import math
from data import AEROPUERTOS

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

if __name__ == "__main__":
    print(calcular_distancia("BOG", "BGA")) 
    print(calcular_distancia("BOG", "LET"))