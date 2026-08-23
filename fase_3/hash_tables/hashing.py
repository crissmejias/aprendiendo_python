import timeit
import random
import string

def generar_datos(n):
    return [''.join(random.choices(string.ascii_letters, k=8)) for _ in range(n)]

def comparar(n, buscar_n_veces=1000):
    datos = generar_datos(n)
    lista = datos.copy()
    diccionario = {valor: True for valor in datos}

    # elegir algunos valores que sí existen para buscar
    valores_a_buscar = random.sample(datos, min(buscar_n_veces, n))

    def buscar_en_lista():
        for v in valores_a_buscar:
            v in lista

    def buscar_en_dict():
        for v in valores_a_buscar:
            v in diccionario

    tiempo_lista = timeit.timeit(buscar_en_lista, number=5)
    tiempo_dict = timeit.timeit(buscar_en_dict, number=5)

    return tiempo_lista, tiempo_dict

print(f"{'n elementos':>12} | {'tiempo list (s)':>16} | {'tiempo dict (s)':>16} | {'list / dict':>12}")
print("-" * 65)
for n in [100, 1_000, 10_000, 100_000]:
    t_lista, t_dict = comparar(n)
    print(f"{n:>12} | {t_lista:>16.6f} | {t_dict:>16.6f} | {t_lista/t_dict:>11.1f}x")   
