NIVELES = {"Platinum": 15_000, "Gold": 5_000, "Silver": 0}
MULTIPLICADORES = {"Silver": 1.0, "Gold": 1.25, "Platinum": 1.5}
MILLAS_POR_KM_REDENCION = 0.001

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

class PassengerVIP(Passenger):
    def __init__(self, nombre, documento, millas_iniciales=0):
        """
        Crea un pasajero VIP segun sus viajes.

        Parámetros:
            millas_iniciales (int): millas con las que empieza (útil para simular).
        """
        super().__init__(nombre, documento)
        self._millas = millas_iniciales
        self._millas_acumuladas = millas_iniciales  # total histórico
        self._nivel = "Silver" #Todos empiezan en Silver
        self._actualizarNivel()

    #Propiedades para acceder a los atributos encapsulados
    @property
    def millas(self):
        return self._millas

    @property
    def millas_acumuladas(self):
        return self._millas_acumuladas

    @property
    def nivel(self):
        return self._nivel

    #El pasajero sube de nivel según las millas acumuladas históricamente
    def _actualizarNivel(self):
        """Sube de nivel según las millas acumuladas históricamente."""

        #Iterar sobre los niveles de mayor a menor, y asignar el nivel correspondiente según las millas acumuladas
        for nivel, umbral in NIVELES.items():
            if self._millas_acumuladas >= umbral:
                if nivel != self._nivel:
                    print(f"¡{self.nombre} subió a nivel {nivel}!")
                self._nivel = nivel
                break

    #El pasajero gana millas según la distancia del vuelo y el multiplicador de su nivel
    def earnMiles(self, distancia):
        """
        Suma millas según la distancia y el multiplicador del nivel actual.

        Retorna:
            int: millas ganadas.
        """
        ganadas = int(distancia * MULTIPLICADORES[self._nivel])
        #Sumamos las millas ganadas a las millas disponibles y a las millas acumuladas históricamente
        self._millas += ganadas
        self._millas_acumuladas += ganadas
        self._actualizarNivel()
        return ganadas

    #Reserva un vuelo pagado y gana millas automáticamente. Sobrescribe el método de Passenger por el polimorfismo.
    def reservarVuelo(self, vuelo, precio):
        """
        Reserva un vuelo pagado y gana millas automáticamente.
        Sobrescribe el método de Passenger (polimorfismo).
        """
        super().reservarVuelo(vuelo, precio)  # si hay overbooking, se detiene aquí
        return self.earnMiles(vuelo.distancia)


    def costoEnMillas(self, vuelo):
        """Retorna cuántas millas cuesta redimir un vuelo."""
        return int(vuelo.distancia * MILLAS_POR_KM_REDENCION)

    def redemir(self, vuelo):
        """
        Redime un vuelo con millas.

        Lanza:
            MillasInsuficientesError: si el saldo no alcanza.
            OverbookingError: si el vuelo está lleno (las millas NO se descuentan).
        """
        costo = self.costoEnMillas(vuelo)
        if self._millas < costo:
            raise Exception(
                f"Se necesitan {costo:,} millas y solo tiene {self._millas:,}")

        super().reservarVuelo(vuelo, 0)  # primero reserva (precio 0, no gana millas)
        self._millas -= costo             # solo descuenta si la reserva fue exitosa

    def __str__(self):
        return (f"{super().__str__()} | Nivel {self._nivel} | "
                f"{self._millas:,} millas disponibles")

if __name__ == "__main__":
    from flight import Vuelo

    vip = PassengerVIP("Arianna González", "1098000000", millas_iniciales=4_800)
    print(vip)

    # 1. Vuelo pagado → gana millas y sube a Gold
    vuelo1 = Vuelo("LU001", "BOG", "BGA", "A320", asientos_vendidos=80)
    print("Millas ganadas:", vip.reservarVuelo(vuelo1, 181454.5))
    print(vip)

    # 2. Redimir un vuelo corto → debería funcionar
    vuelo2 = Vuelo("MA001", "BGA", "BOG", "A320", asientos_vendidos=50)
    vip.redemir(vuelo2)
    print("Redimido. ", vip)

    # 3. Redimir un vuelo largo → millas insuficientes
    vuelo3 = Vuelo("MI001", "BOG", "LET", "A320", asientos_vendidos=50)
    try:
        vip.redemir(vuelo3)
    except Exception as e:
        print("Error:", e)

    # 4. Redimir en un vuelo lleno → overbooking, las millas NO se descuentan
    vuelo4 = Vuelo("JU001", "BOG", "PEI", "A320", asientos_vendidos=160)
    antes = vip.millas
    try:
        vip.redemir(vuelo4)
    except Exception as e:
        print("Error:", e, "| Millas antes:", antes, "después:", vip.millas)

    print("\nHistorial:")
    for reserva in vip.historial:
        print(reserva)