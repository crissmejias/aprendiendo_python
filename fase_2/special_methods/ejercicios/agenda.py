class Agenda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.contactos = {}
    def agregar_contacto(self,nombre,numero):
        self.contactos[nombre] = numero
    def __len__(self):
        return len(self.contactos)
    def __delitem__(self,key):
        del self.contactos[key]
    def __contains__(self,valor):
        return valor in self.contactos
    def __repr__(self):
        return f"Agenda(nombre={self.nombre!r}, total_contactos={len(self.contactos)!r})"
    


# Pruebas

mi_agenda = Agenda("criss")

# Agregar contactos
mi_agenda.agregar_contacto("lisa",12345)
mi_agenda.agregar_contacto("garfield",45678)

# Imprimir cantidad de contactos
print(len(mi_agenda))

# Eliminar un registro
del mi_agenda["garfield"]

# Validar si existe un contacto
print("lisa" in mi_agenda)
print("garfield" in mi_agenda)

# Formato de agenda con nombre y total de contactos
print(mi_agenda)