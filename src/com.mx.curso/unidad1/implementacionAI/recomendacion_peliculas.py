import pandas as pd


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
        tenet += fila[1] 
        pianist += fila[2] 
        inception += fila[3] 
        dune += fila[4] 
        formula += fila[5] 

usuarios = len(datos)
print("\nCalificación PROMEDIO por película: ")
print("Tenet: ", tenet / usuarios)
print("The pianist: ", pianist / usuarios)
print("Inception: ", inception / usuarios)
print("Dune: ", dune / usuarios)
print("Formula 1: ", formula / usuarios)

print("\n------ Usuarios ------")
for usuario in calificaciones:
    if usuario[0] == "Usuario":
        continue
    else:
        print("User: ",usuario)

