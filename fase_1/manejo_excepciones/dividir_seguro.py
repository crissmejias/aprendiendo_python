def dividir_seguro(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

resultado = dividir_seguro(1,0)
if(resultado is None):
    print("No se puede dividir entre 0")
else:
    print(resultado)