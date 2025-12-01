import random
productos = []

for i in range(1, 10):
    nombre = f"Producto {i}"
    puntuacion = round(random.uniform(0, 1), 2)
    productos.append((nombre, puntuacion))

print("Puntuaciones no ordenadas")
print(productos)

n=len(productos)

for i in range(n):
    # Suponemos que el elemento i es el mayor
    maximo = i
    for j in range(i+1,n):
        if productos[j][1]<productos[maximo][1]:
            maximo=j
    # Intercambiar
    temp=productos[i]
    productos[i]=productos[maximo]
    productos[maximo]=temp

print("Productos ordenados: ",productos)


print("\nProductos recomendados: ")
mejores_5 = productos[-5:]
mejores_5 = mejores_5[::-1]
for nombre, puntuacion in mejores_5:
    print(nombre ,": ", puntuacion)