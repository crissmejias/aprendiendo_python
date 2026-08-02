edades = {"Ana": 22, "Luis": 17, "Camila": 20, "Diego": 16, "Valentina": 25}

mayores = {nombre: edad for nombre,edad in edades.items() if edad >= 18}
print(mayores)

