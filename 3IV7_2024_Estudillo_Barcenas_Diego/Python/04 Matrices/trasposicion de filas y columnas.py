def ingresar_matriz():
    matriz = []
    print("Introduce los valores de la matriz 3x3 (por columnas): ")
    for j in range(3):  # Ahora iteramos primero sobre las columnas
        columna = []
        for i in range(3):  # Luego, sobre las filas
            valor = float(input(f"Elemento [{i+1}],[{j+1}]: "))
            columna.append(valor)
        matriz.append(columna)

    matriz_transpuesta = transponer_matriz(matriz)
    return matriz_transpuesta

def transponer_matriz(matriz):
    matriz_transpuesta = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz[j][i]) 
        matriz_transpuesta.append(fila)
    return matriz_transpuesta

def sumar_matriz(matriz1, matriz2):
    matriz_suma = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Matriz 1: ")
matriz1 = ingresar_matriz()

print("Matriz 2: ")
matriz2 = ingresar_matriz()

matriz_resultado = sumar_matriz(matriz1, matriz2)

print("El resultado de la suma es: ")
imprimir_matriz(matriz_resultado)