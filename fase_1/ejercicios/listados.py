inventario = {"manzanas": 10, "peras": 0, "uvas": 5, "kiwis": 0}

stock = {x : y for x,y in inventario.items() if y > 0}

print(stock)