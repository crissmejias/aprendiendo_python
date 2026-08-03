class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def aprobado(self):
        return True if self.nota >= 3.0 else False