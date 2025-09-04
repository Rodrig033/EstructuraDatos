import pandas as pd
import matplotlib.pyplot as plt


# Crea una matriz en dónde almacene las calificaciones del usuario (fila) a la película (columna):

calificaciones = [["Usuario", "Tenet", "The pianist", "Inception", "Dune", "Formula 1"],
                  ["Rodrigo", 4, 5, 4, 4, 4], 
                  ["Sergio P.", 3, 5, 3, 5, 1],
                  ["Cleopatra", 5, 4, 2, 5, 3],
                  ["Elon", 5, 2, 5, 5, 5]]

tenet = 0
pianist = 0
inception = 0
dune = 0
formula = 0

columnas = calificaciones[0]
datos = calificaciones[1:]

# Usare matplotlib y pandas para que mi matriz se vea más ordenada:

df = pd.DataFrame(datos, columns=columnas)
print("\n")
print(df.to_string(index=False))

for fila in calificaciones:
    if fila[0] == "Usuario":
        continue
    else:
        tenet += fila[1] / 5
        pianist += fila[2] / 5
        inception += fila[3] / 5
        formula += fila[4] / 5

print("\nCalificación PROMEDIO por película: ")
print(calificaciones[0][1], tenet)
print(calificaciones[0][2], pianist)
print(calificaciones[0][3], inception)
print(calificaciones[0][4], formula)

print("\n------ Usuarios ------")
for usuario in calificaciones:
    if usuario[0] == "Usuario":
        continue
    else:
        print("User: ",usuario)

