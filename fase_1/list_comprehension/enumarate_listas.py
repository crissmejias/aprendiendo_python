letras = ["a", "b", "c", "d"]

letras_tupla = [(i,l) for i,l in enumerate(letras) if i % 2 ==0 ]
print(letras_tupla)