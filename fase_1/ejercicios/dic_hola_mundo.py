from collections import Counter

texto = "hola mundo"

conteo = dict(Counter(texto[1:-1]))
print((conteo))
