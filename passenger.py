class Passenger:
    def __init__(self, nombre, documento):
        """
        Crea un pasajero con su nombre, numero de documento y un historial de vuelos vacio.
        
        Parámetros:
            nombre (str): nombre del pasajero.
            documento (str): número de documento del pasajero.
        """
        self._nombre = nombre
        self._documento = documento
        self._historial = []  # Lista de vuelos que ha tomado el pasajero

    #Propiedades para acceder a los atributos encapsulados
    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def historial(self):
        """Retorna una copia del historial para que no se pueda modificar desde afuera."""
        return list(self._historial)

    def reservarVuelo(self, vuelo, precio):
        """
        Reserva un vuelo para el pasajero, agregándolo a su historial y descontando un asiento disponible del vuelo.
        
        Parámetros:
            vuelo (Vuelo): vuelo a reservar.
            precio (float): precio del tiquete en COP."""
        try:
            vuelo.reservar_asiento()
            self._historial.append({
                "codigo": vuelo.codigo,
                "origen": vuelo.origen,
                "destino": vuelo.destino,
                "precio": precio,
            })

            print("¡Reserva realizada correctamente!")

        except Exception as error:
            print(f"Error al reservar: {error}")

    def totalGastado(self):
        """Retorna el total pagado en todas las reservas (COP)."""
        return round(sum(reserva["precio"] for reserva in self._historial), 2)

    #Devuelve los datos e información del pasajero, incluyendo el historial de vuelos y el total gastado
    def __str__(self):
        return (f"{self._nombre} (Doc. {self._documento}) | "
                f"{len(self._historial)} reservas | "
                f"Total gastado: ${self.totalGastado():,.0f} COP")
