palabras = ["sol", "luna", "estrella", "mar", "arena"]

palabras_dict = {x[::-1] : len(x)  for x in palabras}
print(palabras_dict)