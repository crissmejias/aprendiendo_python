from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self,marca,velocidad_maxima,cilindraje):
        super().__init__(marca,velocidad_maxima)
        self.cilindraje = cilindraje
    def info(self):
        print(f"{self.marca} - max {self.velocidad_maxima} km/h - {self.cilindraje} cc")
        
moto1 = Moto("Kawasaki Ninja H2R",400, 998)
moto1.info()