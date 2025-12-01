def burbuja(lista):
    contador_swap = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiar los elementos "Swap"
                contador_swap += 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print("Swap             a")
                print(f"{contador_swap}      {lista}")
                print("\n")
                
    print(f"El arreglo fue ordenado en {contador_swap} swaps.")
    print(f"Primer elemento: {lista[0]}.")
    print(f"Ultimo elemento: {lista[-1]}.")
    return lista

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
burbuja(numeros)