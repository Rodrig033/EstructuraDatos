class Stack:
    def __init__(self):
        self.items = []             

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def tamano(self):
        return len(self.items)

    def __str__(self):
        return f"Pila: {self.items}"
    
p = Stack()

p.push(10)
p.push(20)
p.push(30)

print(p)              
print(p.pop())       
print(p.peek())       
print(p.tamano())     
print(p.esta_vacia())