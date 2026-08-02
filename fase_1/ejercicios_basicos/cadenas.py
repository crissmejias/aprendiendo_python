# Ingresar una oracion que puede tener letras mayusculas y minusculas. Contar la cantidad de vocales. Crear un string con toda la oracion en minusculas.

oracion = input("Ingrese una oración: ").lower()
vocales = "aeiou"
contador_vocales = 0

for letra in oracion:
    if letra in vocales:
        contador_vocales += 1

print(f"La cantidad de vocales en la oración es: {contador_vocales}")
