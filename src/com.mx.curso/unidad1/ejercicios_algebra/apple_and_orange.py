# Árbol de manzanas y naranjas:
s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]
apples_counter = 0
oranges_counter = 0
auxiliar = 0

for i in range(len(apples)):
    auxiliar = a + apples[i]
    if auxiliar >= s and auxiliar <= t:
        apples_counter += 1

for i in range(len(oranges)):
    auxiliar = b + oranges[i]
    if auxiliar >= s and auxiliar <= t:
        oranges_counter += 1

print("Manzanas: ", apples_counter)
print("Naranjas: ", oranges_counter)