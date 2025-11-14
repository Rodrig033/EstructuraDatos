partes = int(input("Ingrese las partes para la barra: "))
s = []
for i in range(partes):
     valor = int(input(f"Parte {i + 1} :"))
     s.append(valor)

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))

def chocolate_bar(s, d, m):

    formas = 0
    suma = 0
    n = len(s)

    if m > n: 
         return 0

    for i in range(m): 
        suma += s[i]

    if suma == d:
        formas += 1

    for i in range(m, n):
            suma = suma - s[i - m]
            suma += s[i]

            if suma == d:
                formas += 1

    return formas  

print(chocolate_bar(s, dia, mes))