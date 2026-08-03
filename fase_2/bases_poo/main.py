from coche import Coche
from cuenta_bancaria import CuentaBancaria
from estudiante import Estudiante
from rectangulo import Rectangulo
from producto import Producto

# Coche
coche1 = Coche("Toyota","Corolla",2016)
coche1.describir()

# Cuenta Bancaria

cuenta_criss = CuentaBancaria("Criss",1000)
print(cuenta_criss.depositar(500))
print(cuenta_criss.retirar(200))

# Estudiantes
estudiantes = [Estudiante("Marcos", 4.5), Estudiante("Ana", 2.7), Estudiante("José", 2.9)]
for es in estudiantes:
    print(es.aprobado())
    
# Rectángulo

rectangulo1 = Rectangulo(2,4)
print(rectangulo1.area())
print(rectangulo1.perimetro())

# Productos

productos = [Producto("manzanas",2000,20),Producto("sandias",6000,6),Producto("uvas",4000,60)]
precios = [ x.valor_total() for x in productos]
suma_total = sum(precios)
print(suma_total)