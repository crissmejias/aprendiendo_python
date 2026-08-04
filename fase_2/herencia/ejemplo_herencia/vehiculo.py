class Vehiculo:
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima
    def info(self):
        print(f"{self.marca} - max {self.velocidad_maxima} km/h")
