from typing import Optional

class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.siguiente : Optional["Nodo"] = None
        
class LinkedList:
    def __init__(self):
        self.head : Optional[Nodo] = None
        self.tail : Optional[Nodo] = None
    def agregar_al_inicio(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            prev_head = self.head
            self.head = nuevo_nodo
            self.head.siguiente = prev_head
    def agregar_al_final(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            if self.tail is not None:
                prev_tail = self.tail
                self.tail = nuevo_nodo
                prev_tail.siguiente = self.tail
    def buscar(self,valor):
        actual : Optional[Nodo] = self.head
        while actual is not None:
            if actual.valor == valor:
                return "Valor encontrado"
            actual = actual.siguiente
        return "Valor no encontrado"
    def eliminar(self,valor):
        anterior : Optional[Nodo] = None
        actual : Optional[Nodo] = self.head
        while actual is not None:
            if actual.valor == valor and anterior is None:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                    return f"El valor {valor} fue eliminado"
                self.head = actual.siguiente
                return f"El valor {valor} fue eliminado"
            elif actual is self.tail and actual.valor == valor and anterior is not None:
                anterior.siguiente = None
                self.tail = anterior
                return f"El valor {valor} fue eliminado"
            elif actual.valor == valor and anterior is not None:
                anterior.siguiente = actual.siguiente
                return f"El valor {valor} fue eliminado"
            anterior = actual
            actual = actual.siguiente
        return f"El valor {valor} no se encuentra en la lista"                
            
lista_enlazada = LinkedList()

lista_enlazada.agregar_al_inicio(1)
lista_enlazada.agregar_al_inicio(2)
lista_enlazada.agregar_al_inicio(3)
lista_enlazada.agregar_al_inicio(4)
lista_enlazada.agregar_al_inicio(5)
lista_enlazada.agregar_al_inicio(6)
lista_enlazada.agregar_al_inicio(7)
lista_enlazada.buscar(4)

