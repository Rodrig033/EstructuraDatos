# Algoritmo de ordenamiento: Merge 
recomendacion_1 = [1, 3, 3, 5, 6, 7, 7, 8, 9, 9]
recomendacion_2 = [2, 4, 4, 4, 5, 6, 6, 9, 10, 10]

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arreglo_ordenado = merge(recomendacion_1, recomendacion_2)
print("Recomendaciones:", arreglo_ordenado)