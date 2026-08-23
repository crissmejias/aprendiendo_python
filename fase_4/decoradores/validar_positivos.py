def validar_positivos(func):
    def envoltura(*args,**kwargs):
        if all(n > 0 for n in args):
            resultado = func(*args,**kwargs)
            return  resultado
        else:
            raise ValueError("El número debe ser positivo")
    return envoltura

@validar_positivos
def division(a,b):
    return a /b

print(division(2,3))  
print(division(-2,3))  
