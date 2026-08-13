# Permite usar indexación y slicing en un objeto. También hace que sea iterable por defecto (si no tiene __iter__)

class Collection:
    def __init__(self,items):
        self.items = items
    def __getitem__(self,indice):
        return self.items[indice]

collection = Collection(["producto1","producto2","producto3","producto4"])

print(collection[3]) # producto4
print(collection[2]) # producto3
print(collection[0]) # producto1

print(collection[:2]) # ["producto1","producto2"]