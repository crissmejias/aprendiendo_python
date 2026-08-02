def promedio_seguro(lista):
    try:
        suma = 0
        for n in lista:
            suma += n
        return suma / len(lista)
    except ZeroDivisionError:
        return 0
    
lista = []
print(promedio_seguro(lista))