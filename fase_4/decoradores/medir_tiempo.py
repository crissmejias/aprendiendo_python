import time 
def medir_tiempo(func):
    def envoltura(*args,**kwargs):
        inicio = time.time()
        resultado = func(*args,**kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def tarea_lenta():
    time.sleep(1)
    return "Listo"

print(tarea_lenta.__name__)
print(tarea_lenta())
