# Matriz que represente la sala de cine con 4 filas y 5 asientos por fila:
print("\n---- CINEPOLIS - Sala 10 ---- \n")
sala_cine = [[0, 1, 1, 1, 1],
             [0, 0, 0, 1, 0],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]]

# Sala
for i in sala_cine:
    print(i)

print("\n0 = Asiento libre")
print("1 = Asieto ocupado\n")

fila = int(input("Ingrese la fila: "))
asiento = int(input("Ingrese la columna: "))

for i in sala_cine:
    if sala_cine[fila][asiento] == 1:
        print("Asiento ocupado")

    else: 
        sala_cine[fila][asiento] = 1



for i in sala_cine:
    print(i)