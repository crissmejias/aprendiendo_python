from functools import wraps

def decorador(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        print("Antes de ejecutar la función")
        resultado = func(*args,**kwargs) 
        print("Después de ejecutar la función")
        return resultado
    return envoltura

@decorador
def saludar():
    return "Hola"

print(saludar.__name__)

print(saludar())
