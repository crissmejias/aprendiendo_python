from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self,nombre):
        self.nombre = nombre
    @abstractmethod
    def calcular_pago(self):
        pass
    
#  Ana = Empleado("Ana")
#  TypeError: Can't instantiate abstract class Empleado without an implementation for abstract method 'calcular_pago'

class Gerente(Empleado):
    def __init__(self,nombre):
        self.nombre = nombre

# Jose = Gerente("Jose")

# TypeError: Can't instantiate abstract class Gerente without an implementation for abstract method 'calcular_pago'

class Vendedor(Empleado):
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def calcular_pago(self):
        print(f"El pago es de {self.sueldo}")
        
Ana = Vendedor("Ana", 2000)
Ana.calcular_pago()
        