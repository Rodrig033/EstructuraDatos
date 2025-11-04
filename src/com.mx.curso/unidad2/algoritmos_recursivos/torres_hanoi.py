def torres_hanoi(discos, origen, auxiliar, destino):
    if discos == 0:
        return
    torres_hanoi(discos - 1, origen, destino, auxiliar)
    print(f"El disco {discos} se moverá desde {origen} hasta {destino}.")
    torres_hanoi(discos - 1, auxiliar, origen, destino)

discos = 3
origen = "A"
auxiliar = "B"
destino = "C"

torres_hanoi(discos, origen, auxiliar, destino)