class Fila:
    def __init__(self):
        self.items = [] 

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def frente(self):
        if not self.esta_vacia():
            return self.items[0]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return f"Fila: {self.items}"
    
f = Fila()

f.encolar("A")
f.encolar("B")
f.encolar("C")

print(f)                
print(f.desencolar())   
print(f.frente())       
print(f.tamano())       
print(f.esta_vacia())