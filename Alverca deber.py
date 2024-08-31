# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None  # Si no se encuentra el valor, retorna None

# Definir el valor a buscar
valor_a_buscar = 5

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion} (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")