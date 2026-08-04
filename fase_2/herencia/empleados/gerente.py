from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    def calcular_pago(self):
        return self.salario_base + self.bono