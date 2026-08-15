from collections import deque

def fila_de_atencion(*args):
    fila = deque()
    for i in args:
        fila.append(i)
        
    while len(fila) > 0:
        print(f"Atendiendo a {fila[0]}")
        fila.popleft()
    print("Fila vacía")

fila_de_atencion("Cris", "Tefa", "Lisa", "Garfield")