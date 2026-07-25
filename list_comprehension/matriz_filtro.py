matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_par = [y for x in matriz for y in x if y % 2 ==0]
print(lista_par)