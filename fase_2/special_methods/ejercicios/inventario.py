class Inventario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.inventario = {}
    def __len__(self):
        return len(self.inventario)
    def __getitem__(self,producto):
            return self.inventario[producto]
    def agregar(self,producto,cantidad):
        self.inventario[producto] = cantidad
        print(f"Se ha agregado el producto {producto}!")
    def __contains__(self,producto):
        return producto in self.inventario
    def __repr__(self):
        return f"Inventario(nombre={self.nombre!r}, cantidad_productos={len(self.inventario)!r})"

#Crear objeto
mi_inventario = Inventario("criss")

#Agregar productos
mi_inventario.agregar("Teclado",200)
mi_inventario.agregar("Mouse",100)
mi_inventario.agregar("Monitor",50)

#Imprimir referencia del objeto
print(mi_inventario)

#Acceder con un string
print(mi_inventario["Teclado"])
print(mi_inventario["Celulares"])


# Verificar si un producto existe
print("Monitor" in mi_inventario)