# Algoritmo de ordenamiento: Inserción
sensores = []

for i in range(8):
    lectura = float(input(f"Ingrese la lectura del sensor {i + 1}: "))    
    j = len(sensores) - 1
    sensores.append(lectura)  
    while j >= 0 and sensores[j] > lectura:
        sensores[j + 1] = sensores[j]  
        j -= 1
    sensores[j + 1] = lectura  

    print(f"Lista ordenada después de la lectura {i + 1}: {sensores}")

print("\nLecturas finales ordenadas: ", sensores)