from empleado import Empleado

class Vendedor(Empleado):
    def __init__(self, nombre, salario_base, comision):
        super().__init__(nombre, salario_base)
        self.comision = comision
    def calcular_pago(self):
        return self.salario_base + self.comision