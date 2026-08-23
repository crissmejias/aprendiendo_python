def contar_llamadas(func):
    contador = 0
    def envoltura(*args,**kwargs):
        resultado = func(*args,**kwargs)
        nonlocal contador 
        contador += 1
        print(f"Hay un total de {contador} llamadas")
        return resultado
    return envoltura

@contar_llamadas
def saludar(nombre):
    return f"Hola {nombre}"

saludar("Ana")
saludar("Cris")
saludar("Luis")


