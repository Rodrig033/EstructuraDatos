# Algoritmo de ordenamiento: Burbuja
correos = [10, 40, 30, 50, 90, 20, 70, 30, 60, 80]

print("Muestras de Spam desordenadas: ", correos)
longitud = len(correos)

for i in range(longitud - 1):
    for j in range(longitud - i - 1):
        if correos[j] > correos[j + 1]:
            correos[j], correos[j + 1] = correos[j + 1], correos[j]

print("Calificación de muestras de Spam: ", correos)