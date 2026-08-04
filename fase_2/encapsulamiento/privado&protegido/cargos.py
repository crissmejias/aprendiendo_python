class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario
        
class Gerente(Empleado):
    def  aumentar_salario(self,monto):
        self._salario += monto
        print(f"Nuevo salario: {self._salario}")
        
gerente1 = Gerente("Ana", 20000)
gerente1._salario = 20
print(gerente1._salario)

gerente1.aumentar_salario(50000)