# Unidad candela 
intensidad = [[400, 300, 250, 100],
              [150, 350, 230, 750],
              [500, 150, 450, 170],
              [450, 600, 650, 100]]

flag = True

# Imprimir la matriz:
print("Matriz de intensidad: ")
for i in range(len(intensidad)):
    for j in range(len(intensidad)):
        print(intensidad[i][j], end= " ")
    print()

def actualizar_matriz(intensidad):
    print("\nMatriz actualizada: ")
    for i in range(len(intensidad)):
        for j in range(len(intensidad)):
            print(intensidad[i][j], end= " ")
        print()

suma = 0
for i in range(len(intensidad)):
    for j in range(len(intensidad)):
        suma += intensidad[i][j]

def introducir_ficha(intensidad, fila, columna, opcion):
    if columna >= len(intensidad[0]) or columna < 0 or fila >= len(intensidad) or fila < 0:
        print("ERROR: Fila o columna fuera del rango.")
        return
    intensidad[fila][columna] = opcion


while flag:
    fila = int(input("\nIntroduzca la fila: "))
    columna = int(input("Introduzca una columna: "))
    valor = int(input("Introduzca la intensidad: "))
    introducir_ficha(intensidad, fila, columna, valor)
    actualizar_matriz(intensidad)
    intentar = input("¿Desea seguir (s/n)?")
    if intentar.lower() == 'n':
        flag = False

for i in range(len(intensidad)):
    suma_fila = 0
    for j in range(len(intensidad)):
        suma_fila += intensidad[i][j]
    print("Promedio de la fila:", i, ": ", (suma_fila / len(intensidad[i])))