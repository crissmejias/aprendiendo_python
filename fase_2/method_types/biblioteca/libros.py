libros_normales = [
    ("Cien años de soledad", "Gabriel García Márquez", "9780307474728"),
    ("1984", "George Orwell", "9780451524935"),
    ("El principito", "Antoine de Saint-Exupéry", "9780156012195"),
]

libros_string = [
    "Rayuela, Julio Cortázar, 9788437604572",
    "Fahrenheit 451, Ray Bradbury, 9781451673319",
    "Crónica de una muerte anunciada, Gabriel García Márquez, 9780307387922",
]

isbns_para_validar = [
    "9780307474728",   # válido — 13 caracteres
    "978030747",        # inválido — muy corto
    "97803074747281234", # inválido — muy largo
    "9780451524935",     # válido
]