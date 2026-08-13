class Rango:
    def __init__(self,inicio,fin):
        self.rango = range(inicio,fin)
        self.inicio = inicio
        self.fin = fin
    def __iter__(self):
        return iter(self.rango)
    def __contains__(self,valor):
        return valor in self.rango
    def __repr__(self):
        return f"Rango(inicio={self.inicio!r}, fin={self.fin!r})"
    
    
# Pruebas

mi_rango = Rango(1,10)

# Probando iterar el rango
for n in mi_rango:
    print(n)
# Imprimir si existe un elemento en el rango    
print(3 in mi_rango)

# Imprimir objeto
print(mi_rango)