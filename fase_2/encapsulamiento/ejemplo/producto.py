class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        if nuevo_precio < 0:
            print("El nuevo precio no puede ser negativo")
        else:
            self.__precio  = nuevo_precio
    