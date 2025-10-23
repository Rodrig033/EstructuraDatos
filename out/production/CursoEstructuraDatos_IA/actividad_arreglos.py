# Construcción de un vector de características:
individuo = {"Altura": 1.90, "Peso": 80, "Edad": 30}

clave_diccionario = input("Selecciona el valor al que deseas acceder: ")

try:
    valor_diccionario = individuo[clave_diccionario]
    if clave_diccionario == "Peso":
        print(f"El valor es de {valor_diccionario} kg.")
    elif clave_diccionario == "Altura":
        print(f"El valor es de {valor_diccionario} cm.")
    elif clave_diccionario == "Edad":
        print(f"El valor es de {valor_diccionario} años.")
except KeyError:
    print("El valor no se encuentra dentro del diccionario.")

# Modificación del valor:
input("¿Desea modificar algún valor? (S/N)")




    