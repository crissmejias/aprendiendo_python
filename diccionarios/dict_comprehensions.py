# Se utiliza el mismo patrón de las listas, sin embargo, usaremos llaves {}

numeros = [1,2,3,4,5]
cuadrados = {n: n**2 for n in numeros}
print(cuadrados)

## Usando una condición

pares_cuadrados = {n: n**2 for n in numeros if n % 2 ==0}
print(pares_cuadrados)

# Transformando un diccionario existente

precios = {"manzana": 10, "pera": 15, "uva": 8}

con_descuento = {producto: precio * 0.9 for producto, precio in precios.items()}
print(con_descuento)

