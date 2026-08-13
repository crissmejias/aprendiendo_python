# Define el comportamiento del operador in. __contains nos da control sobre la lógica exacta que usa el objeto.

class Carrito:
    def __init__(self):
        self.productos = []
    def agregar(self,producto):
        self.productos.append(producto)
    def __contains__(self,producto):
        return producto in self.productos
    
carrito = Carrito()
carrito.agregar("Teclado")
print("Teclado" in carrito) # True
print("Mouse" in carrito) # False