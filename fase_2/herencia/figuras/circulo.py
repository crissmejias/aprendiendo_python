from figura import Figura
class Circulo(Figura):
    def __init__(self,nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    def area(self):
        return 3.14 * self.radio **2
    def describir(self):
        super().describir()
        print(f"Mi area es {self.area()}")