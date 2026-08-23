def validador(func):
    def envoltura(*args,**kwargs):
        resultado = func(*args,**kwargs)
        n1,n2 = args
        if n1 > 0 and n2 > 0:
            return  resultado
        else:
            raise ValueError("El número debe ser positivo")
    return envoltura
@validador
def division(a,b):
    return a /b

print(division(2,3))  
print(division(-2,3))  
