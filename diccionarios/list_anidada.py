numeros = range(1, 51)
lista_divisibles = [n for n in numeros if (n % 3 ==0) ^ (n % 5 ==0)]
print(lista_divisibles)