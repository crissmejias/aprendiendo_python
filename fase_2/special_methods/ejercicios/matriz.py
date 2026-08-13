class Matriz:
    def __init__(self, matriz):
        self.matriz = matriz
    def __getitem__(self,indice):
        fila, columna = indice
        return self.matriz[fila][columna]
    def __contains__(self,value):
        for n in self.matriz:
            if value in n:
                return True
        return False
    def __repr__(self):
        return f"Matriz: filas: {len(self.matriz)!r}, columnas: {len(self.matriz[0])!r}."
    
matriz = Matriz([[1,2,3],[4,5,6]])
print(matriz[1,2])
print(matriz)  
print(3 in matriz)
print(10 in matriz)