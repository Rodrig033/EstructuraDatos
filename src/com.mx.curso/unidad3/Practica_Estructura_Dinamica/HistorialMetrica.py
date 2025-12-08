class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class HistorialMetrica:
    def __init__(self):
        self.cabeza = None

    def HistorialMetrica(self):
         self.cabeza = None

    def insertarMetrica(self, metrica):
        nuevoNodo = Nodo(metrica)
        nuevoNodo.siguiente = self.cabeza

        self.cabeza = nuevoNodo

    def insertarMetricaFin(self, metrica):
        nuevo = Nodo(metrica)

        if self.cabeza is None:
            self.cabeza = nuevo
            print("Nueva métrica agregada ", metrica)
            return
        

        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        
        actual.siguiente = nuevo
        print("Nueva métrica agregada ", metrica)

    def historialMetricas(self):
        actual = self.cabeza
        print("\nHistorial de métricass")
        print("Epoch | Valor")
        print("----------------")
        epoch = 1

        while actual is not None:
            print(f"{epoch:5} | {actual.dato}")
            actual = actual.siguiente
            epoch += 1
    
    def buscarMetrica(self, metrica):
        if self.cabeza is None:
            print("La lista está vacía -> No existe la métrica ", metrica)
            return False
        
        actual = self.cabeza
        posicion = 1

        print()
        while actual is not None:
            if actual.dato == metrica:
                print("Buscando métrica ", metrica, "...")
                print("Métrica encontrada en Epoch ", posicion, " : ", metrica)
                return True
                
            actual = actual.siguiente
            posicion += 1;
        
        print("Buscando métrica ", metrica, "...")
        print("La métrica ", metrica, " no ha sido encontrada en el historial.")
        return False
    
historial = HistorialMetrica()
historial.insertarMetricaFin(70);
historial.insertarMetricaFin(83);
historial.insertarMetricaFin(45);
historial.insertarMetricaFin(20);
historial.insertarMetricaFin(33);

historial.historialMetricas()

historial.buscarMetrica(33);
historial.buscarMetrica(45);

