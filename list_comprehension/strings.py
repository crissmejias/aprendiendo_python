frase = "El perro corre en el parque"
palabras= [ x for x in frase.split() if len(x) > 3]
print(palabras)