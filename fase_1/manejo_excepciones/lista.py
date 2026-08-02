numeros = [10, 20, 30]


try:
    indice = int(input("Ingresa un indice:"))
    print(numeros[indice])
except ValueError:
    print("El valor no es válido")
except IndexError:
    print("El indice no es válido")

# Ingresa un indice:3
# El indice no es válido

# Ingresa un indice:2
# 30