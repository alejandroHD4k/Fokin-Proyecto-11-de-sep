"""
main.py
Simulador de aerolínea: reservas de vuelos y programa de viajero frecuente.
"""

from data import AEROPUERTOS
from viajes import calcular_precio_base, calcular_precio_dinamico, calcular_emisiones
from programacion import DIAS_SEMANA, generar_programacion_semanal, buscar_vuelos, obtener_vuelo
from passenger import Passenger, PassengerVIP


# =============== Entrada de datos (validación) ===============
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")

def pedir_aeropuerto(mensaje):
    """Pide un código IATA. Enter = sin filtro (retorna None)."""
    while True:
        codigo = input(mensaje).strip().upper()
        if codigo == "":
            return None
        if codigo in AEROPUERTOS:
            return codigo
        print("Código no válido. Opciones:", ", ".join(AEROPUERTOS))


def pedir_dia():
    print("Días:", " | ".join(f"{i}. {d}" for i, d in enumerate(DIAS_SEMANA, 1)))
    while True:
        opcion = input("Día (1-7, Enter = todos): ").strip()
        if opcion == "":
            return None
        if opcion.isdigit() and 1 <= int(opcion) <= 7:
            return DIAS_SEMANA[int(opcion) - 1]
        print("Opción no válida.")


def confirmar(mensaje):
    return input(f"{mensaje} (s/n): ").strip().lower() == "s"


# =============== Registro ===============
def registrar_pasajero():
    print("\n=== Registro de pasajero ===")
    nombre = pedir_texto("Nombre completo: ")
    documento = pedir_texto("Documento: ")

    if confirmar("¿Pertenece al programa de viajero frecuente?"):
        millas = input("Millas iniciales (Enter = 0): ").strip()
        millas = int(millas) if millas.isdigit() else 0
        return PassengerVIP(nombre, documento, millas_iniciales=millas)
    return Passenger(nombre, documento)


# =============== Cálculos (usa la librería viajes.py) ===============
def cotizar(vuelo):
    """Retorna (distancia, precio, co2_por_pasajero) de un vuelo."""
    distancia = vuelo.distancia
    precio_base = calcular_precio_base(distancia)
    precio = calcular_precio_dinamico(precio_base, vuelo.occupancyStatus())
    co2 = calcular_emisiones(distancia, vuelo.tipo_avion, 1)
    return distancia, precio, co2


# =============== Opciones del menú ===============
def mostrar_vuelos(resultados):
    if not resultados:
        print("No hay vuelos disponibles con esos filtros.")
        return
    for dia, vuelo in resultados:
        _, precio, _ = cotizar(vuelo)
        print(f"[{dia}] {vuelo} | ${precio:,.0f} COP")


def menu_buscar(semana):
    print("\n=== Buscar vuelos (Enter para omitir un filtro) ===")
    origen = pedir_aeropuerto("Origen (IATA): ")
    destino = pedir_aeropuerto("Destino (IATA): ")
    dia = pedir_dia()
    mostrar_vuelos(buscar_vuelos(semana, origen, destino, dia))


def elegir_vuelo(semana):
    codigo = pedir_texto("\nCódigo del vuelo: ").upper()
    vuelo = obtener_vuelo(semana, codigo)
    if vuelo is None:
        print("No existe un vuelo con ese código.")
    return vuelo


def menu_reservar(semana, pasajero):
    vuelo = elegir_vuelo(semana)
    if vuelo is None:
        return

    distancia, precio, co2 = cotizar(vuelo)
    print(f"\n{vuelo}")
    print(f"Distancia: {distancia:,.0f} km | Precio: ${precio:,.0f} COP | "
          f"Huella de carbono: {co2:,.1f} kg CO₂")

    if not confirmar("¿Confirmar la reserva?"):
        print("Reserva cancelada.")
        return

    try:
        millas_ganadas = pasajero.reservarVuelo(vuelo, precio)
    except Exception as e:
        print("❌", e)
        return

    print("✅ Reserva confirmada.")
    if isinstance(pasajero, PassengerVIP):
        print(f"Ganó {millas_ganadas:,} millas. Saldo: {pasajero.millas:,} | "
              f"Nivel: {pasajero.nivel}")


def menu_redimir(semana, pasajero):
    if not isinstance(pasajero, PassengerVIP):
        print("Solo los pasajeros del programa de viajero frecuente pueden redimir millas.")
        return

    vuelo = elegir_vuelo(semana)
    if vuelo is None:
        return

    costo = pasajero.costoEnMillas(vuelo)
    print(f"\n{vuelo}")
    print(f"Costo: {costo:,} millas | Su saldo: {pasajero.millas:,} millas")

    if not confirmar("¿Redimir este vuelo?"):
        print("Redención cancelada.")
        return

    try:
        pasajero.redeemFlight(vuelo)
    except Exception as e:
        print("❌", e)
        return

    print(f"✅ Vuelo redimido. Saldo restante: {pasajero.millas:,} millas")


def mostrar_perfil(pasajero):
    print(f"\n{pasajero}")
    if not pasajero.historial:
        print("Sin reservas todavía.")
        return
    print("Historial:")
    for r in pasajero.historial:
        pago = "Redimido con millas" if r["precio"] == 0 else f"${r['precio']:,.0f} COP"
        print(f"  {r['codigo']}: {r['origen']} → {r['destino']} | {pago}")


def mostrar_aeropuertos():
    print("\n=== Aeropuertos ===")
    for codigo, info in AEROPUERTOS.items():
        print(f"{codigo} - {info['nombre']} ({info['ciudad']})")


# =============== Programa principal ===============
def main():
    print("✈️  Bienvenido al simulador de aerolínea")
    semana = generar_programacion_semanal()
    pasajero = registrar_pasajero()

    while True:
        print("\n========== MENÚ ==========")
        print("1. Ver programación semanal")
        print("2. Buscar vuelos")
        print("3. Reservar vuelo")
        print("4. Redimir vuelo con millas")
        print("5. Ver mi perfil e historial")
        print("6. Ver aeropuertos")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            mostrar_vuelos(buscar_vuelos(semana, dia=pedir_dia()))
        elif opcion == "2":
            menu_buscar(semana)
        elif opcion == "3":
            menu_reservar(semana, pasajero)
        elif opcion == "4":
            menu_redimir(semana, pasajero)
        elif opcion == "5":
            mostrar_perfil(pasajero)
        elif opcion == "6":
            mostrar_aeropuertos()
        elif opcion == "0":
            print("¡Buen viaje! ✈️")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()