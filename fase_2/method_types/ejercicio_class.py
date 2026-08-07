class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    @classmethod
    def desde_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

print(Temperatura.desde_fahrenheit(32).celsius)