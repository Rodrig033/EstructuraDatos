flag = True
def crear_tablero(filas, columnas):
    return [[0]*columnas for _ in range(filas)]

"""Función para mostrar un tablero más completo:"""
def mostrar_tablero(tablero):
    columnas = len(tablero[0])
    """Sacamos por pantalla la cabezera: """
    print("    ", end="")
    for i in range(columnas):
        print(f" {i}  ", end="")
    print()


    separador = "   +" + "---+" * columnas
    
    """Sacamos por pantalla el tablero completo: """
    for i in range(len(tablero)):
        print(separador) 
        print(f" {i} ", end= "")
        for j in range(columnas):
            print(f"| {tablero[i][j]}", end=" ")
        print("|")
    print(separador)







tablero = crear_tablero(5, 5)
mostrar_tablero(tablero)

def introducir_ficha(tablero, fila, columna, opcion):
    if columna >= len(tablero[0]) or columna < 0 or fila >= len(tablero) or fila < 0:
        print("ERROR: Fila o columna fuera del rango.")
        return
    if opcion not in [0,1]:
        print("ERROR: El valor debe de estar entre 0 y 1.")
        return
    tablero[fila][columna] = opcion

while flag:
    fila = int(input("\n\nIntroduzca la fila: "))
    columna = int(input("Introduzca una columna: "))
    valor = int(input("Introduzca 0 o 1: "))
    introducir_ficha(tablero, fila, columna, valor)
    mostrar_tablero(tablero)
    intentar = input("¿Desea seguir (s/n)?")
    if intentar.lower() == 'n':
        flag = False

total_obstaculos = sum(sum(fila) for fila in tablero)
print("\nTotal de obstáculos en el tablero:", total_obstaculos)

fila_elegida = int(input("Eliga una fila para contar obstáculos: "))
if fila_elegida < 0 or fila_elegida >= len(tablero):
    print("Fila fuera del rango")
else:
    obstaculos_fila = sum(tablero[fila_elegida])
    print(f"Los obstaculos en la fila {fila_elegida}: {obstaculos_fila}")