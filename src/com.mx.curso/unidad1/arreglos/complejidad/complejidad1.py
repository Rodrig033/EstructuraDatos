# Analisis de complejidad de algoritmos:
import time 


def buscar_elementos(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False
    
starTime = time.time()
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            11, 12, 13, 14, 15, 16, 17, 18, 19, 
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
elemento = 30
encontrado = buscar_elementos(mi_lista, elemento)
endTime = time.time()
if encontrado:
    print(f"El elemento {elemento} fue encontrado en la lista.")
else: 
    print(f"El elemento {elemento} no fue encontrado en la lista.")
print(f"El tiempo de ejecución: {endTime - starTime} segundos.")


