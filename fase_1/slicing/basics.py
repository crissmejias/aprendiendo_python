# [inicio:fin:paso]
 
# -> Inicio indica donde empieza el string
# -> Fin indica donde termina, no incluye el elemento en el que termina.
# -> Paso indica la dirección y la cantidad de saltos entre caracteres que da el string
texto = "programación"

print(texto[0:4]) # del indice 0 al 3

print(texto[4:]) # a partir del indice 4

print(texto[:4]) # del inicio hasta el indice 3

print(texto[:]) # texto completo

print(texto[-3:]) # últimos 3 caracteres

print(texto[::2]) # cada dos caracteres desde el inicio.

print(texto[::-1]) # texto al revés


