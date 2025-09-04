caracteriticas = [3.5, 1.4, 0.2]

suma_car = 0
division = 0

for caracteristica in caracteriticas:
    suma_car += caracteristica

print("Suma características: ",suma_car)

suma_total = 0
for elemento in caracteriticas:
    division = elemento / suma_car
    suma_total += division
    print(division)

print("Suma total: ",suma_total)
    