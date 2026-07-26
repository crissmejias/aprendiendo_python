# Datos guardados como clave valor
estudiante = {
    "nombre": "Criss",
    "carrera": "Ingenieria de software",
    "semestre":1
}

## Acceder a un valor por clave:
print(estudiante["nombre"])

# Agregar o modificar clave 
estudiante["semestre"] = 2
estudiante["universidad"] = "Universitaria de Colombia"

# Borrar una clave
del estudiante["universidad"]
print(estudiante)
print("------------------")

# Verificando si existe una clave
if "nombre" in estudiante:
    print("El estudiante tiene nombre")
print("------------------")

# Accceso con .get()
estudiante.get("apellido") # None, el programa sigue corriendo
print("------------------")
estudiante.get("apellido","N/A")  # N/A como valor por defecto
print("------------------")

# Iteraciones
for clave in estudiante:
    print(clave) # imprime solo las claves
print("------------------")
for clave,valor in estudiante.items():
    print(clave,valor)


