# Ejercicio 3: Sala de asientos de cine con 4 fila y 5 asientos por fila:

sala_cine = [[0,1,0,0,1],
             [1,1,0,0,0],
             [0,0,1,0,1],
             [1,1,1,1,0]]

columnas = sala_cine[0]
datos = sala_cine[:-1]

for i in range(len(sala_cine)):
    for j in range(len(sala_cine[i])):
        print(sala_cine[i][j], end=" ")
    print()

print("\n")
print("    ✧  BIENVENIDO A  ✧")
print(" ╔════════════════════╗")
print(" ║      CINEPOLIS     ║")
print(" ╚════════════════════╝")
print()



# El usuario debe elegir su asiento:
fila = int(input("Eliga la fila: "))
asiento = int(input("Eliga su asiento: "))

for i in range(len(sala_cine)):
    for j in range(len(sala_cine[i])):
       if sala_cine[i][j] == 0:
           sala_cine[fila][asiento] = 1

while sala_cine[fila][asiento] == 1:
    print("Este asiento está ocupado...")
    fila = int(input("Eliga la fila: "))
    asiento = int(input("Eliga su asiento: "))

sala_cine[fila][asiento] = 1


for i in range(len(sala_cine)):
    for j in range(len(sala_cine[i])):
        print(sala_cine[i][j], end=" ")
    print()