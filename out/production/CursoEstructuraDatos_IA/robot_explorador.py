# Lectura de datos de los 4 sensores:
data_sensores = [120, 85, 210, 150, 100]
umbral_critico = 100

# Lecturas mayores al umbral
print("\nSensores de Spirit activados...")
print("Umbral critico: 100 \n")
for i in data_sensores:
    if i > 100:
        print("Lectura SUPERIOR al umbral: ", i)
    elif i < 100:
        print("ADVERTENCIA (Lectura inferior al umbral): ", i)
    else:
        print("Lectura DENTRO del umbral: ", i)