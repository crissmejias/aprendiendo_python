class Equipo:
    def __init__(self,jugadores):
        self.jugadores = jugadores
    def __len__(self):
        return len(self.jugadores)
barca = Equipo(["Pedri","Gavi", "Lamine","Raphinha"])

print(len(barca))

class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"{self.nombre}, {self.nota}"
    def __eq__(self, other):
        return self.nombre == other.nombre and self.nota == other.nota
    def  __lt__(self,other):
        return self.nota < other.nota

lisa = Estudiante("Lisa", 4.7)
print(lisa)

otra_lisa = Estudiante ("Lisa",4.7)

print(lisa ==  otra_lisa)

garfield = Estudiante("Garfield",3)
print(lisa == garfield)

tefa =  Estudiante("Tefa", 5)

criss = Estudiante("Criss",4.8)

lista_estudiantes = sorted([criss,tefa,lisa,garfield],reverse=True)

for e in lista_estudiantes:
    print(e)