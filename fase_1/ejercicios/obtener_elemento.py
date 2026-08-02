def obtener_elemento(lista,indice):
    try:
        return  lista[indice]
    except IndexError:
        return None
    
lista = [1,2,3,4,5]
print(obtener_elemento(lista,10))
print(obtener_elemento(lista,3))