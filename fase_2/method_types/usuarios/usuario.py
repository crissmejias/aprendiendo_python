class Usuario:
    contar_usuarios = 0
    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
    @classmethod
    def crear_string(cls,string):
        nombre,email = string.split(":")
        cls.contar_usuarios += 1
        return cls(nombre,email)
    @classmethod
    def leer_usuarios(cls):
        return cls.contar_usuarios
    @staticmethod
    def validar_email(email):
        return "@" in email and "." in email
    
class Admin(Usuario):
    contar_usuarios = 0
    def __init__(self,nombre,email):
        super().__init__(nombre,email)

class Cliente(Usuario):
    contar_usuarios = 0
    def __init__(self,nombre,email):
        super().__init__(nombre,email)

Usuario.crear_string("criss:criss@gmail.com")
Usuario.crear_string("criss:criss@gmail.com")
Usuario.crear_string("criss:criss@gmail.com")
Admin.crear_string("criss:criss@gmail.com")
Admin.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")
Cliente.crear_string("criss:criss@gmail.com")



print(Usuario.leer_usuarios())
print("---------------------")
print(Admin.leer_usuarios())
print("---------------------")
print(Cliente.leer_usuarios())
