AEROPUERTOS = {
    "BOG": {  # El Dorado (Bogotá)
        "nombre": "Aeropuerto Internacional El Dorado",
        "ciudad": "Bogotá",
        "iata": "BOG",
        "icao": "SKBO",
        "coordenadas": (4.7016, -74.1469)
    },
    "MDE": {  # José María Córdova (Medellín / Rionegro)
        "nombre": "Aeropuerto Internacional José María Córdova",
        "ciudad": "Medellín / Rionegro",
        "iata": "MDE",
        "icao": "SKRG",
        "coordenadas": (6.1645, -75.4231)
    },
    "CTG": {  # Rafael Núñez (Cartagena)
        "nombre": "Aeropuerto Internacional Rafael Núñez",
        "ciudad": "Cartagena",
        "iata": "CTG",
        "icao": "SKCG",
        "coordenadas": (10.4424, -75.5130)
    },
    "CLO": {  # Alfonso Bonilla Aragón (Cali / Palmira)
        "nombre": "Aeropuerto Internacional Alfonso Bonilla Aragón",
        "ciudad": "Cali / Palmira",
        "iata": "CLO",
        "icao": "SKCL",
        "coordenadas": (3.5427, -76.3819)
    },
    "BAQ": {  # Ernesto Cortissoz (Barranquilla)
        "nombre": "Aeropuerto Internacional Ernesto Cortissoz",
        "ciudad": "Barranquilla / Soledad",
        "iata": "BAQ",
        "icao": "SKBQ",
        "coordenadas": (10.8896, -74.7808)
    },
    "ADZ": {  # Gustavo Rojas Pinilla (San Andrés)
        "nombre": "Aeropuerto Internacional Gustavo Rojas Pinilla",
        "ciudad": "San Andrés",
        "iata": "ADZ",
        "icao": "SKSP",
        "coordenadas": (12.5836, -81.7112)
    },
    "PEI": {  # Matecaña (Pereira)
        "nombre": "Aeropuerto Internacional Matecaña",
        "ciudad": "Pereira",
        "iata": "PEI",
        "icao": "SKPE",
        "coordenadas": (4.8127, -75.7395)
    },
    "BGA": {  # Palonegro (Bucaramanga)
        "nombre": "Aeropuerto Internacional Palonegro",
        "ciudad": "Bucaramanga / Lebrija",
        "iata": "BGA",
        "icao": "SKBG",
        "coordenadas": (7.1265, -73.1848)
    },
    "CUC": {  # Camilo Daza (Cúcuta)
        "nombre": "Aeropuerto Internacional Camilo Daza",
        "ciudad": "Cúcuta",
        "iata": "CUC",
        "icao": "SKCC",
        "coordenadas": (7.9276, -72.5115)
    },
    "SMR": {  # Simón Bolívar (Santa Marta)
        "nombre": "Aeropuerto Internacional Simón Bolívar",
        "ciudad": "Santa Marta",
        "iata": "SMR",
        "icao": "SKSM",
        "coordenadas": (11.1196, -74.2306)
    },
    "AXM": {  # El Edén (Armenia)
        "nombre": "Aeropuerto Internacional El Edén",
        "ciudad": "Armenia / La Tebaida",
        "iata": "AXM",
        "icao": "SKAR",
        "coordenadas": (4.4528, -75.7664)
    },
    "LET": {  # Alfredo Vásquez Cobo (Leticia)
        "nombre": "Aeropuerto Internacional Alfredo Vásquez Cobo",
        "ciudad": "Leticia",
        "iata": "LET",
        "icao": "SKLT",
        "coordenadas": (-4.1911, -69.9420)
    },
    "MTR": {  # Los Garzones (Montería)
        "nombre": "Aeropuerto Internacional Los Garzones",
        "ciudad": "Montería / Cereté",
        "iata": "MTR",
        "icao": "SKMR",
        "coordenadas": (8.8239, -75.8258)  # aprox. según fuentes estándar
    },
    "RCH": {  # Almirante Padilla (Riohacha)
        "nombre": "Aeropuerto Internacional Almirante Padilla",
        "ciudad": "Riohacha",
        "iata": "RCH",
        "icao": "SKRH",
        "coordenadas": (11.5262, -72.9260)
    },
    "EYP": {  # El Alcaraván (Yopal)
        "nombre": "Aeropuerto El Alcaraván",
        "ciudad": "Yopal",
        "iata": "EYP",
        "icao": "SKYP",
        "coordenadas": (5.3192, -72.3842)
    }
}


AVIONES = {

    #Los valores están expresados en kg CO₂ por pasajero-kilómetro.

    "B737": {
        "nombre": "Boeing 737",
        "pasajeros_tipicos": 175,
        "factor_emision": 0.0677 
    },
    "A320": {
        "nombre": "Airbus A320",
        "pasajeros_tipicos": 160,
        "factor_emision": 0.0787
    },
    "A321": {
        "nombre": "Airbus A321",
        "pasajeros_tipicos": 210,
        "factor_emision": 0.0717
    },
    "E170_190": {
        "nombre": "Embraer E-Jets",
        "pasajeros_tipicos": 105,
        "factor_emision": 0.1440
    },
    "A319": {
        "nombre": "Airbus A319",
        "pasajeros_tipicos": 135,
        "factor_emision": 0.0911
    },
    "B787": {
        "nombre": "Boeing 787 Dreamliner",
        "pasajeros_tipicos": 285,
        "factor_emision": 0.0840
    },
    "A220": {
        "nombre": "Airbus A220",
        "pasajeros_tipicos": 125,
        "factor_emision": 0.1007
    },
    "A350": {
        "nombre": "Airbus A350",
        "pasajeros_tipicos": 355,
        "factor_emision": 0.0861
    },
    "B777": {
        "nombre": "Boeing 777-300ER",
        "pasajeros_tipicos": 350,
        "factor_emision": 0.1094
    },
    "A330": {
        "nombre": "Airbus A330",
        "pasajeros_tipicos": 300,
        "factor_emision": 0.1117
    }
}
