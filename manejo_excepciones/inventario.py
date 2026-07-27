inventario = {"manzanas": 10, "peras": 5}

def consultar_producto(producto):
    try:
        return inventario[producto]
    except KeyError:
        return "El producto no existe"

print(consultar_producto("manzanas"))
print(consultar_producto("pan"))

# 10
# El producto no existe