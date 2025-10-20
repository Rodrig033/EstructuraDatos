# Clasificación y recomendación:
import random
productos = []

for i in range(1, 101):
    nombre = f"Producto {i}"
    puntuacion = round(random.uniform(0, 1), 2)
    productos.append((nombre, puntuacion))


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

productos_ordenados = mergeSort(productos)
print("Productos ordenados: ",productos_ordenados)

print("\nProductos recomendados: ")
mejores_5 = productos_ordenados[-5:]
mejores_5 = mejores_5[::-1]
for nombre, puntuacion in mejores_5:
    print(nombre ,": ", puntuacion)
    