class Fecha:
    def __str__(self):
        return "01/01/2026"

class Coordenada:
    def __str__(self):
        return "4.7°N, 74.0°W"

class Precio:
    def __str__(self):
        return "$50000"
    
def mostrar(objeto):
    print(objeto)
    
mostrar(Precio()) # $50000
mostrar(Coordenada()) # 4.7°N, 74.0°W
mostrar(Fecha()) # 01/01/2026