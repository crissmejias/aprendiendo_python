# Se usa como respaldo de __str__ cuando no está definido. 
# Su función principal es servir como una representación del objeto en cuestión.
# Usa una convención f"NombreClase(atributo1={self.atributo1!r}, atributo2 = {self.atributo2!r}...)"

# Ejemplo general
class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, precio={self.precio!r})"
    

p = Producto("Teclado",2000)
print(p)
print([p,p])
# En este caso se usa el !r para llamar a repr() de ese valor.
# repr() devuelve una representación en cadena de texto formal e inequívoca de un objeto.
