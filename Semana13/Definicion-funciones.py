def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    :param datos_temperatura: Lista tridimensional donde:
        - La primera dimensión representa las ciudades.
        - La segunda dimensión representa las semanas.
        - La tercera dimensión representa los días de la semana.
    :return: Un diccionario con el promedio de temperaturas para cada ciudad.
    """
    ciudades = ['zamora', 'Nangaritza', 'zumbi']
    promedios = {}

    for i, ciudad in enumerate(ciudades):
        total_temperaturas = 0
        num_datos = 0

        for semana in datos_temperatura[i]:
            for temperatura in semana:
                total_temperaturas += temperatura
                num_datos += 1

        promedio = total_temperaturas / num_datos if num_datos > 0 else 0
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
datos_temperatura = [
    [  # Zamora
        [30, 31, 29, 32, 30, 31, 30],  # Semana 1
        [29, 30, 28, 31, 30, 29, 30],  # Semana 2
        [32, 33, 31, 32, 30, 31, 29],  # Semana 3
        [31, 30, 32, 33, 32, 30, 31]  # Semana 4
    ],
    [  # Nangaritza
        [28, 29, 30, 28, 27, 29, 30],  # Semana 1
        [27, 28, 29, 30, 28, 27, 29],  # Semana 2
        [29, 30, 31, 30, 29, 28, 30],  # Semana 3
        [30, 31, 29, 28, 30, 29, 28]  # Semana 4
    ],
    [  # Zumbi
        [25, 26, 27, 28, 27, 26, 25],  # Semana 1
        [24, 25, 26, 27, 26, 27, 28],  # Semana 2
        [26, 27, 28, 29, 28, 27, 26],  # Semana 3
        [27, 28, 29, 30, 29, 28, 27]  # Semana 4
    ]
]

# Calcular promedios
promedios = calcular_temperatura_promedio(datos_temperatura)
print(promedios)
