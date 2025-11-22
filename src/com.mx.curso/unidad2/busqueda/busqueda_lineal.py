def busqueda_secuencial(arr, x):
    for i in arr:
        if arr[i] == x:
            return i
    return -1


if __name__ == "__main__":
    datos = [3,4,5,6,7,8,9]
    elemento = 9

    indice = busqueda_secuencial(datos, elemento)
    if indice != -1:
        print(f"Elemento {elemento} se ha encontrado en la posición {indice}.")
    else:
        print(f"Elemento {elemento} no se ha encontrado en la lista.")