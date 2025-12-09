from NodoPila import NodoPila

class BusquedaPila:
    def __init__(self):
        self.tope = None

    # Métodos semejantes a java:
    def agregar(self, estado):
        nuevo = NodoPila(estado)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        print("[Push] ", estado)

    def eliminar(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        
        valor = self.tope.estado
        self.tope = self.tope.siguiente
        print(f"[POP] Procesando estado {valor}")
        return valor

    
    def mostrar_pila(self):
        print("\nEstados pendientes por explorar:")
        actual = self.tope
        while actual is not None:
            print(" -", actual.estado)
            actual = actual.siguiente
        print()

# Iniciamos la pruebas
if __name__ == "__main__":

    pila = BusquedaPila()
    pila.agregar("Inicio en A")
    pila.agregar("Explorar A -> B")
    pila.agregar("Explorar B -> C")
    pila.agregar("Retroceder, explorar otro camino")
    pila.agregar("Intentar ruta alternativa en D")

    pila.mostrar_pila()

    print("----- Iniciando exploración LIFO -----\n")
    while pila.eliminar() is not None:
        pass