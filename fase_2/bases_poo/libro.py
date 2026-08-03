class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def info(self):
        print(f"{self.titulo} de {self.autor} ({self.paginas} páginas)")
        
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
libro2 = Libro("1984","George Orwell",400)

libro1.info()
libro2.info()
print(libro1.autor)