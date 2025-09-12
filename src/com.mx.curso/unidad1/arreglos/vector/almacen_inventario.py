import pandas as pd

# Crea una matriz que represente el inventario:
""" Filas: Productos
    Columnas: ID
    Cantidad en stock y precio unitario"""

# Producto ID Cantidad Precio:
inventario = [["Producto", "ID", "Cantidad", "Precio"],
              ["Capitan Crunch", 123, 50, 150],
              ["Caja leche lala", 234, 30, 175],
              ["Yoghurt Oikos", 345, 75, 30]]



columnas = inventario[0]
datos = inventario[1:]
columna_precio = 3
columna_cantidad = 2
columna_id = 1
id_valido = False


df = pd.DataFrame(datos, columns=columnas)
print("\n")
print(df.to_string(index=False))

# Calcula el valor de un producto específico:
print()
producto = input("Ingrese el nombre del producto: ")
producto.lower()
id_producto = int(input("Ingrese el ID del producto: "))


total = 0

while not id_valido:
     for i in inventario[1:]:
          if i[1] == id_producto:
               id_valido = True
               
     if not id_valido:
        id_producto = int(input("Ingrese el ID del producto: "))


for i in range(len(inventario)):
    for j in range(len(inventario[i])):
         if id_producto == inventario[i][1]:
              total = inventario[i][columna_precio] * inventario[i][columna_cantidad]

print(f"\nEl valor total de {producto} es: ", total)

ventas = int(input("Ingrese las unidades a comprar: "))
for fila in inventario[1:]:
    if fila[columna_id] == id_producto:
        if ventas > fila[columna_cantidad]:
            print(f"No hay suficiente stock. Solo hay {fila[columna_cantidad]} unidades disponibles.")
            ventas = fila[columna_cantidad]  
        total = fila[columna_precio] * ventas
        if ventas == 10:
         fila[columna_cantidad] -= ventas
        break


df = pd.DataFrame(inventario[1:], columns=columnas)
print("\nInventario actualizado:")
print(df.to_string(index=False))