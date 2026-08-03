class Coche:
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def describir(self):
        print(f"{self.marca} {self.modelo} - {self.anio}")
        