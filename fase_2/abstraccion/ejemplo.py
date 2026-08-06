# Ejemplo de clase abstracta

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

# figura1 = Figura() # TypeError  => No se puede instanciar una clase abstracta.

# class Circulo(Figura):
#     def __init__(self,radio):
#         self.radio = radio
    # No se define el area
    
# circulo1 = Circulo(5) # TypeError =>  La clase no implementa el método area.
# print(circulo1.radio)

# Can't instantiate abstract class Figura without an implementation for abstract method 'area'

class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def area(self):
        return 3.1416 * self.radio ** 2
    
circulo2 = Circulo(5) # => Funciona porque la clase implementa correctamente el método "area"

print(circulo2.area()) # 78.53