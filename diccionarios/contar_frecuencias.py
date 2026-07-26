from collections import Counter

texto = "programacion en python"
conteo = {}

# Usando get para obtener el valor del conteo y sumar uno

for l in texto:
    conteo[l] = conteo.get(l,0) + 1
print(conteo)
print("----------------------------")

# Usando Counter

nuevo_conteo = Counter(texto)
print(nuevo_conteo)