class Terrestre:
    def desplazarse(self):
        print("Camina por la tierra")
        
class Acuatico:
    def desplazarse(self):
        print("Nada por el agua")

class Anfibio(Acuatico, Terrestre):
    pass

anfibio = Anfibio()
print(Anfibio.__mro__)  # (<class '__main__.Anfibio'>, <class '__main__.Acuatico'>, <class '__main__.Terrestre'>, <class 'object'>)
anfibio.desplazarse() # Nada por el agua
