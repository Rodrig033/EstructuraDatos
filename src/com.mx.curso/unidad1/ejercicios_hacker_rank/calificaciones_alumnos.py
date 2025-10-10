# Crea un arreglo que permita almacenar las 
import pandas as pd
# Crea una matriz en donde filas(estudiantes) y columnas(exámenes):
examenes = [["Estudiante", "Calificación"],
                  ["Alan Turing", 0], 
                  ["Elon Musk", 0],
                  ["Samuel Altman", 0],
                  ["Ada Lovelace", 0]]

columnas = examenes[0]
datos = examenes[1:]
flag = True
flag_two = True

# Usaré la librería pandas para hacer más dinámica la matriz:
df = pd.DataFrame(datos, columns=columnas)
print("\n")
print(df.to_string(index=False))

# Ingresa las calificaciones por estudiante:
for i in range(len(datos)):
    nombre = datos[i][0] # Siempre fila cero
    for j in range(1, len(columnas)):
        examen = columnas[0:][j] # Desde la fila cero e iterando
        calificacion = int(input(f"Ingrese la calificación de {nombre} en el {examen}: "))
        datos[i][j] = calificacion

# Actualizo la matriz:
df = pd.DataFrame(datos, columns=columnas)
print("\n")
print(df.to_string(index=False))

# Obtener la calificaciones por medio del indice:
while flag_two:
    pregunta = input("¿Desea modificar una calificación (s/n)?")
    print(pregunta)
    if pregunta.lower() == 's':
        indice = input("Ingrese el nombre del alumno: ")
        encontrado = False
        print(indice)
        for i in range(len(datos)):
            nombre = datos[i][0] # Siempre fila cero
            if nombre.lower() == indice.lower():
                encontrado = True
                for j in range(1, len(columnas)):
                    examen = columnas[0:][j] # Desde la fila cero e iterando
                    calificacion = int(input(f"Ingrese la calificación de {indice} en el {examen}: "))
                    datos[i][j] = calificacion
                    break                
    else: 
        flag_two = False


# Obtener el promedio:
promedios_estudiantes = [sum(fila[1:]) / (len(fila) - 1) for fila in datos]

print(f"\nPromedio de cada estudiante:")
for i, promedio in enumerate(promedios_estudiantes):
    print(f"{datos[i][0]}: {promedio:.2f}")

# Almacena el promedio por examen en una matriz:
promedio_examen = []
for examen in range(1, len(columnas)):
    suma = sum(fila[examen] for fila in datos)
    promedio = suma / len(datos)
    promedio_examen.append(promedio)

# Promedio por examen:
print(f"\nPromedio de examen:")
for i, promedio in enumerate(promedio_examen, start= 1):
    print(f"{columnas[i]}: {promedio:.2f}")

# Calificación más alta:
maxima_nota = 0
mejor_estudiante = ""
for i, fila in enumerate(datos):
    nota_max = max(fila[1:])
    if nota_max > maxima_nota:
        maxima_nota = nota_max
        mejor_estudiante = fila[0]

print(f"\nEl estudiante con la calificación más alta es {mejor_estudiante} con {maxima_nota}")