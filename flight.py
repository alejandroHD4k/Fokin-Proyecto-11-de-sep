import random
from data import AVIONES
from viajes import calcular_distancia

class Vuelo:
    def __init__(self, codigo, origen, destino, tipo_avion, asientos_vendidos):
        """
        Crea un vuelo. Se asume que los datos vienen validados desde programacion.py.

        Parámetros:
            codigo (str): código del vuelo (ej. "LU001").
            origen (str): código IATA del aeropuerto de origen.
            destino (str): código IATA del aeropuerto de destino.
            tipo_avion (str): clave del avión en AVIONES (ej. "A320").
            asientos_vendidos (int): asientos ya vendidos al crear el vuelo.
        """

        #Encapsulamos los atributos para que no puedan ser modificados desde fuera de la clase
        self._codigo = codigo
        self._origen = origen
        self._destino = destino
        self._tipo_avion = tipo_avion
        self._capacidad_maxima = AVIONES[tipo_avion]["pasajeros_tipicos"]
        self._asientos_disponibles = self._capacidad_maxima - asientos_vendidos

    # Propiedades para acceder a los atributos encapsulados
    @property
    def codigo(self):
        return self._codigo

    @property
    def origen(self):
        return self._origen

    @property
    def destino(self):
        return self._destino

    @property
    def tipo_avion(self):
        return self._tipo_avion

    @property
    def asientos_disponibles(self):
        return self._asientos_disponibles

    @property
    def distancia(self):
        """Distancia del vuelo en km, calculada con viajes.py."""
        return calcular_distancia(self._origen, self._destino)

    # Reserva de asiento
    def reservar_asiento(self):
        """
        Reserva un asiento en el vuelo.

        Lanza:
            Exception: si no hay asientos disponibles.
        """
        if self._asientos_disponibles == 0:
            raise Exception(f"El vuelo {self._codigo} está lleno")
        
        #Resta un asiento disponible al vuelo
        self._asientos_disponibles -= 1

    #Calcula el porcentaje de ocupación del vuelo para el precio dinamico
    def occupancyStatus(self):
        """
        Retorna el porcentaje de ocupación del vuelo (0 a 100).
        """
        ocupados = self._capacidad_maxima - self._asientos_disponibles
        return round((ocupados / self._capacidad_maxima) * 100, 2)

    # Programación de Vuelo 
    def __str__(self):
        return (f"Vuelo {self._codigo}: {self._origen} → {self._destino} | "
                f"{AVIONES[self._tipo_avion]['nombre']} | "
                f"{self._asientos_disponibles}/{self._capacidad_maxima} asientos libres "
                f"({self.occupancyStatus()}% ocupado)")
