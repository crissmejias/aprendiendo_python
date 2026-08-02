try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")

    # echo "Esto es una prueba de texto" > datos.txt
    # Esto es una prueba de texto
