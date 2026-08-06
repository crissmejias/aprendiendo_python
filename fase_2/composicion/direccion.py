class Direccion:
    def __init__(self, calle, ciudad):
        self.calle = calle
        self.ciudad = ciudad
    def __str__(self):
        return f"{self.calle}, {self.ciudad}"

class Persona:
    def __init__(self,nombre,calle,ciudad):
        self.nombre = nombre
        self.direccion = Direccion(calle,ciudad)
    def __str__(self):
        return f"{self.nombre} - {self.direccion}"        
criss = Persona("Criss", "Calle 164", "Bogotá")

print(criss)
