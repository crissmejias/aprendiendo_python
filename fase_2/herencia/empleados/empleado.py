class Empleado:
    def __init__(self,nombre,salario_base):
        self.nombre = nombre
        self.salario_base = salario_base
    def calcular_pago(self):
        return self.salario_base