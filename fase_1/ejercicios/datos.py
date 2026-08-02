datos = {"a": "10", "b": "veinte", "c": "30", "d": "cuarenta"}
datos_a_enteros = {}
for x, y in datos.items():
    try:
        datos_a_enteros[x] = int(y)
    except ValueError:
        print("No se puede convertir el elemento")
        
print(datos_a_enteros)