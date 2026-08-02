matriz = [[1, 2, 3], [4, 5, 6]]

nueva_matriz = []

for i in range(len(matriz[0])):
    nueva_matriz.append([])
    for j in range(len(matriz)):
        nueva_matriz[i].append(matriz[j][i])
print(nueva_matriz)