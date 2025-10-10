temperaturas = [[40, 35, 25],
                [43, 20, 33],
                [21, 17, 50]]
flag = True

# Imprimir la matriz:
print("Matriz de temperaturas: ")
for i in range(len(temperaturas)):
    for j in range(len(temperaturas)):
        print(temperaturas[i][j], end= " ")
    print()

def actualizar_matriz(temperaturas):
    print("\nMatriz actualizada: ")
    for i in range(len(temperaturas)):
        for j in range(len(temperaturas)):
            print(temperaturas[i][j], end= " ")
        print()

def introducir_ficha(temperaturas, fila, columna, opcion):
    if columna >= len(temperaturas[0]) or columna < 0 or fila >= len(temperaturas) or fila < 0:
        print("ERROR: Fila o columna fuera del rango.")
        return
    temperaturas[fila][columna] = opcion

while flag:
    fila = int(input("\nIntroduzca la fila: "))
    columna = int(input("Introduzca una columna: "))
    valor = int(input("Introduzca la temperatura: "))
    introducir_ficha(temperaturas, fila, columna, valor)
    actualizar_matriz(temperaturas)
    intentar = input("¿Desea seguir (s/n)?")
    if intentar.lower() == 'n':
        flag = False