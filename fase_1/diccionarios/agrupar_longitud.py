palabras = ["oso", "gato", "elefante", "perro", "hormiga", "pez", "leon"]
dict_palabras= {}
for p in palabras:
    dict_palabras.setdefault(len(p),[]).append(p)
print(dict_palabras)