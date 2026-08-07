import libros

class Biblioteca:
    total_libros =0
    def __init__(self,nombre,autor,isbn):
        self.nombre = nombre
        self.autor = autor
        self.isbn = isbn
        Biblioteca.total_libros += 1
    @classmethod
    def crear_en_linea(cls,linea):
        nombre, autor, isbn = linea.split(",")
        return cls(nombre.strip(),autor.strip(),isbn.strip())
    @staticmethod
    def isbn_valido(isbn):
        return len(isbn) == 13
    @classmethod
    def cantidad_libros(cls):
        return cls.total_libros
      
# Creando libros a través del __init__ y confirmar cantidad      
for nombre,autor,isbn in libros.libros_normales:
    Biblioteca(nombre,autor,isbn)    
print(Biblioteca.cantidad_libros())

#Probando crear libros en línea y confirmar cantidad de libros
for libro_en_linea in libros.libros_string:
    Biblioteca.crear_en_linea(libro_en_linea)
print(Biblioteca.cantidad_libros())

# Validar isbn a través del @staticmethod
for isbn in libros.isbns_para_validar:
    print(Biblioteca.isbn_valido(isbn))
