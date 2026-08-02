datos = ["10", "20", "abc", "30", "xyz", "40"]
suma =0
for i in range(len(datos)):
    try:
        suma += int(datos[i])
    except ValueError:
        continue
print(suma)