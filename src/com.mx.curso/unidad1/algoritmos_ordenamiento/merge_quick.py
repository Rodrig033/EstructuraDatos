# MergeSort vs Quicksort:
import time, random

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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# QuickSort:
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
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


tamaños = [100, 1000, 10000]

print(f"{'Tamaño':<10}{'Tiempo MergeSort (s)':<22}{'Tiempo QuickSort (s)'}")
print("-" * 52)


for n in tamaños:
    datos = [round(random.uniform(0, 1), 2) for _ in range(n)]

    # Tiempo de MergeSort
    inicio_merge = time.time()
    mergeSort(datos)
    tiempo_merge = time.time() - inicio_merge

    # Tiempo de QuickSort
    inicio_quick = time.time()
    quicksort(datos)
    tiempo_quick = time.time() - inicio_quick

    print(f"{n:<10}{tiempo_merge:<22.6f}{tiempo_quick:.6f}")
