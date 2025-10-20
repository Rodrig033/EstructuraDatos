import random

productos = [(f"Producto {i+1}", round(random.uniform(0, 1), 2)) for i in range(8)]

print("Lista original:")
print(productos)
print("\n")

def merge(left, right):
    result = []
    i = j = 0
    print(f"Mezclando {left} y {right}")
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    print(f"Resultado de la mezcla: {result}\n")
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    print(f"Dividiendo {arr} -> {leftHalf} y {rightHalf}\n")

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

productos_ordenados = mergeSort(productos)

print("Lista final ordenada:")
print(productos_ordenados)