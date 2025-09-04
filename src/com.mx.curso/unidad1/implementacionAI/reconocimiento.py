# Reconocimiento de patrones

caracteristicas = [3.5, 1.5, 0.2]

suma = 0

# Suma los elementos: 
for i in caracteristicas:
    suma += i

print("La suma total de las caracteristicas es: ", i)

# Normalización: 
for j in range(len(caracteristicas)):
    caracteristicas[j] = caracteristicas[j] / suma

print("La suma normalizadadas son: ", caracteristicas)

