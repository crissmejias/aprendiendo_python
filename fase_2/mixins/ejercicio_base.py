import datetime
class TimestampMixin:
    def marca_de_tiempo(self):
        return f"Creado: {datetime.datetime.now()}"

class SerializableMixin:
    def a_diccionario(self):
        return self.__dict__
    
class Post(TimestampMixin,SerializableMixin):
    def __init__(self,titulo,autor,texto):
        self.titulo = titulo
        self.autor = autor
        self.texto = texto
        
post1 = Post("Prueba","Criss", "Esto es un texto de prueba para un post")
print(post1.marca_de_tiempo()) # Creado: 2026-08-07 17:22:24.030278
print(post1.a_diccionario()) # {'titulo': 'Prueba', 'autor': 'Criss', 'texto': 'Esto es un texto de prueba para un post'}