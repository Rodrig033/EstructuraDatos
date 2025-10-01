# Metricas de precisión:
metrics = []
flag = True    

while flag:
    valor = int(input("Ingrese una precision a la lista:  "))
    metrics.append(valor)
    agregar = input("¿Desea agregar otra precisión (s/n)? ")
    if agregar.lower() == 'n':
        flag = False
    
    # Imprimir la lista con las metricas:
    print("Metricas = ", metrics)
    

# Posición final:
print("\nPosición final: ", metrics[-1])

# Posición más alta:
print("Valor maximo: ", max(metrics))

# Imprimir todo los valores:
for i in range(len(metrics)):
    if i != len(metrics ) - 1:
        print(metrics[i], end=", ")
    else:
        print(metrics[i])




