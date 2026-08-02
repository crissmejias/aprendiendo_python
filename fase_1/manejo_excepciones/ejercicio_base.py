try:
    numero = int(input("Ingresa un número:"))
    print(100 / numero)
except ValueError:
    print("No es un número válido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")

try:
    numero = int(input("Dame un número:"))
except ValueError:
    print("No es un número válido")
else:
    print("Perfecto, el número es:",numero)
finally:
    print("Esto siempre se ejecuta")

