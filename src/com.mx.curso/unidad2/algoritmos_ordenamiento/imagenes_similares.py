# Algoritmo de ordenamiento: Quicksort
import random

puntos = [round(random.uniform(0, 1), 2) for _ in range(200)]
puntuaciones = [0.6, 0.9, 0.3, 0.8, 0.5, 0.7, 0.2, 1.0, 0.4, 0.95]

def partition(array, low, high):
    pivote = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] >= pivote:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

quicksort(puntos)
print("Puntuaciones: ", puntos)