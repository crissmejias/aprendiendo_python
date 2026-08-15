# Pilas son listas ordinarias en Python

lista = [1,2,3,4]

# push -> agrega elementos al tope
lista.append(5) ; print(lista) # [1,2,3,4,5]

# pop -> quita elementos del tope

lista.pop() ; print(lista) # [1,2,3,4]

# Ambos son O(1), ya que no necesitan iterar entre elementos, siempre van a agregar o quitar al último elemento de la lista

# Si tratamos de hacer pop(índice), se volverá O(n), ya que debe recorrer toda la lista para buscar la posición. Por esto no se deben usar listas [] de Python para implementar colas.

# Queues (colas)

from collections import deque

cola = deque()

cola.appendleft(4)
cola.appendleft(3)
cola.appendleft(2)
cola.appendleft(1)
cola.popleft()
print(cola) # deque([2,3,4])


# En este caso se comporta de la misma manera que el pop() pero con los elementos al inicio de la cola, haciéndolo en O(n)

