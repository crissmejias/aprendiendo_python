from empleado import Empleado
from vendedor import Vendedor
from gerente import Gerente

empleados = [Empleado("Lisa",10000), Gerente("Lisa",10000,5000),  Vendedor("Lisa",20000,2000),Empleado("Lisa",10000), Vendedor("Lisa",20000,2000),Gerente("Lisa",10000,5000), Empleado("Lisa",10000)]

for e in empleados:
    print(e.calcular_pago())