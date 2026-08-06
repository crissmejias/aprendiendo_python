class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def encender(self):
        print(f"Motor encendido con {self.potencia} HP")

class Coche:
    def __init__(self, marca, potencia_motor):
        self.marca = marca
        self.motor = Motor(potencia_motor)   # Coche TIENE un Motor — composición

    def arrancar(self):
        print(f"{self.marca} arrancando...")
        self.motor.encender()   # delega el trabajo al objeto interno
        
        
coche1 = Coche("Toyota", 150)
coche1.arrancar()
