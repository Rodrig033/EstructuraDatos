import random

def quicksort(arreglo):
    if len(arreglo) <= 1:
        return arreglo  # Caso base: arreglo con 0 o 1 elemento
    pivote = arreglo[-1]  # Elegimos el último elemento como pivote
    menores = [x for x in arreglo[:-1] if x[1] <= pivote[1]]  
    mayores = [x for x in arreglo[:-1] if x[1] > pivote[1]] 
      
    # Aplicamos recursión y combinamos resultados
    return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
productos = []
for i in range(1, 10):
    nombre = f"Comentario {i}"
    puntuacion = round(random.uniform(0, 1), 2)
    productos.append((nombre, puntuacion))

print(quicksort(productos))