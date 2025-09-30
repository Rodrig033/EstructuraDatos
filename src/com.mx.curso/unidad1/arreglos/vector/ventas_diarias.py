# Crea un arreglo vacío de 7 posiciones:
ventas = []
semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]


for i in range(7):
    venta = int(input(f"Ingrese las ventas totales {semana[i]}: "))
    ventas.append(venta)

total_ventas = 0
dia_mayor = 0
dia_menor = 0

for i in range(7):
    total_ventas += ventas[i]
    if ventas[i] > ventas[dia_mayor]:
        dia_mayor = i
    elif ventas[i] < ventas[dia_menor]:
        dia_menor = i

print("\nTotal ventas: ", total_ventas)
print(f"Día con más ventas {semana[dia_mayor]} con {ventas[dia_mayor]}")
print(f"Día con menos ventas {semana[dia_menor]} con {ventas[dia_menor]}")
