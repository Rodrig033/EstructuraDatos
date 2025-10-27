def fibonacci_recursivo(base):
    if base == 0:
        return base
    elif base == 1:
        return base
    else:
        return fibonacci_recursivo(base - 1) + fibonacci_recursivo(base - 2) 

enesimo_elemento = int(input("Ingrese la posición para ver el número fibonacci: "))
print(f"El número en la posición {enesimo_elemento} fibonacci es {fibonacci_recursivo(enesimo_elemento)}.")

# Imprimir los primeros 10 números:
for i in range(10):
    print(f"Número ({i+1}): ", fibonacci_recursivo(i))