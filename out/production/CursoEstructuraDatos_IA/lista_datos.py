# Arreglo con información de altua, peso y edad:
informacion = [190, 80, 30]

# Acceder al valor de la lista:
print("\nAltura: ", informacion[0], " cm. ")
print("Peso: ", informacion[1], " kg.")
print("Edad: ", informacion[2], " años.")

# Modificar valores:
print("\nModificación: ")
informacion[0] = 195
informacion[1] = 87
informacion[2] = 33
print("Altura: ", informacion[0], " cm. ")
print("Peso: ", informacion[1], " kg.")
print("Edad: ", informacion[2], " años.")

suma = 0
# Obtener la media de los valores:
for i in informacion:
    suma += i


print("\nSuma de los valores: ",suma)

for i in informacion:
    media = suma / len(informacion)
print("Media: ",media)