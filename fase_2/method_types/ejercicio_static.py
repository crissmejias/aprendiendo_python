class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def es_congelante(celsius):
        return celsius <= 0
    
print(Temperatura.es_congelante(-15))