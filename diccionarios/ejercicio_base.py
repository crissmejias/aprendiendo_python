libro = {"titulo": "Cien años de soledad", "autor": "García Márquez", "año": 1967}

# Imprimir titulo

print(libro["titulo"])

print("---------------------")

# Agregar una nueva clave

libro["paginas"] = 471
print(libro["paginas"])
print("---------------------")
# Recorrer el diccionario e imprimir cada clave en conjunto con su valor en formato clave: valor.

for clave, valor in libro.items():
    print(clave+":",valor)