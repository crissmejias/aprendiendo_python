import productos

class Producto:
    descuentos = 0
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    @classmethod
    def precio_rebajado(cls,nombre,precio,descuento):
        precio_rebajado = precio * (1 - descuento / 100)
        cls.descuentos += (precio - precio_rebajado)
        return cls(nombre,precio_rebajado)
    @staticmethod
    def descuento_valido(valor_descuento):
        return valor_descuento >= 0 and valor_descuento <= 100
    @classmethod
    def total_descontado(cls):
        return cls.descuentos

# Crear productos
for nombre, precio in productos.productos:
    producto = Producto(nombre,precio)
    print(producto.nombre,producto.precio,sep=" - ") 
    
print("---------------------------")

# Crear productos con descuento
for nombre, precio, descuento in productos.descuentos_a_aplicar:
    producto = Producto.precio_rebajado(nombre,precio,descuento)
    print(producto.nombre,producto.precio)
    
print("---------------------------")

# Validar total ahorrado

print(Producto.total_descontado())

print("---------------------------")

# Validar descuentos

for descuento in productos.porcentajes_para_validar:
    print(Producto.descuento_valido(descuento))
    