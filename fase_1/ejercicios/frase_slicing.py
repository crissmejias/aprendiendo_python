frase = "El rendimiento importa mucho en programacion"

frase_separada = [x for x in frase.split()[:3]  if len(x) > 4]

print(frase_separada)