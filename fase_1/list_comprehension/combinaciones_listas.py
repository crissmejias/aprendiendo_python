colores = ["rojo", "azul"]
tallas = ["S", "M", "L"]

combinadas = [f"{c}-{t}" for c in colores for t in tallas]
print(combinadas)