from collections import Counter

def procesar_texto(texto):
    try:
        conteo_de_caracteres = dict(Counter(texto[:50].split()))
        return conteo_de_caracteres
    except TypeError:
        return None
    
    
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pellentesque nulla non mattis mollis. Nullam ullamcorper turpis ut nisl tempor mollis. Nam fringilla venenatis lacus, et cursus ipsum commodo eget. Aliquam egestas vehicula ullamcorper. Etiam condimentum ante eget lacinia interdum. Aenean commodo mollis ligula, id lacinia lorem iaculis ac. Quisque rutrum lectus id dignissim sagittis. Donec vitae diam tempor, venenatis risus eu, lacinia nunc. Praesent commodo eu urna sed tincidunt. Sed ut massa tincidunt, pharetra turpis a, pharetra nibh. Curabitur ac consequat sapien. Mauris viverra finibus tortor, quis lacinia nulla posuere a. Duis ultricies venenatis ipsum et tincidunt. Nullam orci. "
prueba_error = 12312

print(procesar_texto(lorem))
print(procesar_texto(prueba_error))