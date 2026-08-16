from typing import Optional
class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente: Optional["Nodo"]= None

class ListaEnlazada:
    def __init__(self):
        self.cabeza : Optional[Nodo] = None   # lista vacía al inicio
        self.cola : Optional[Nodo] = None
    def agregar_al_inicio(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            cabeza_anterior = self.cabeza
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = cabeza_anterior
    def buscar(self,valor):
        if self.cabeza is not None:
            actual : Optional[Nodo] = self.cabeza
            while actual is not None:
                if valor == actual.valor:
                    return True
                actual  = actual.siguiente
        return False
    def eliminar(self,valor):
        actual : Optional[Nodo] = self.cabeza
        anterior: Optional[Nodo] = None
        if self.cabeza is not None:
            while actual is not None:
                if actual.valor == valor:
                    if anterior is None:
                        if actual is self.cola:
                            self.cola = anterior
                        self.cabeza = actual.siguiente
                        return True
                    else:
                        if actual == self.cola:
                            self.cola = anterior    
                        anterior.siguiente = actual.siguiente
                    return True
                anterior = actual
                actual = actual.siguiente
            return False
    def agregar_al_final(self,valor):
        nuevo_nodo : Nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza  = nuevo_nodo
            self.cola = nuevo_nodo
            return True
        if self.cola is not None:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo   
    def imprimir(self):
        actual : Optional[Nodo] = self.cabeza
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

lista = ListaEnlazada()
lista.agregar_al_final("a")
lista.agregar_al_final("b")
lista.agregar_al_final("c")
lista.agregar_al_inicio("d")
lista.imprimir() # d -> a -> b -> c -> None

print(lista.buscar("b"))
print(lista.buscar("e"))
print(lista.buscar("a"))

lista.eliminar("d")
lista.imprimir()


lista.imprimir()
print(lista.eliminar("z"))


lista.agregar_al_inicio(None)
lista.imprimir()

lista.eliminar(None)
lista.imprimir()


