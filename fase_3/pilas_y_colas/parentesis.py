def balanceado(cadena):
    pila = []
    for i in range(len(cadena)):
        if cadena[i] in '([{':
            pila.append(cadena[i])
        elif cadena[i] in ')]}':
            try:
                if pila[len(pila) -1] == '(' and cadena[i] == ')':
                    pila.pop()
                elif pila[len(pila) -1] == '[' and cadena[i] == ']':
                    pila.pop()
                elif pila[len(pila) -1] == '{' and cadena[i] == '}':
                    pila.pop()
                else:
                    return "No balanceado"
            except IndexError:
                 return "No balanceado"
    if len(pila) > 0:
        return "No balanceado" 
    else:
        return f"¡Balanceado!"
# Pruebas

print(balanceado("((()))")) # Balanceado
print(balanceado("(([]))")) # Balanceado

print(balanceado("))(())")) # No balanceado
print(balanceado("[)")) # No balanceado

print(balanceado("({})")) # Balanceado
