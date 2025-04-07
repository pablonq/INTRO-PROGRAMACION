# Par o Impar (Expresión Booleana): Pide al usuario un número y evalúa si es par usando el
# operador módulo (`%`). Muestra el resultado de la expresión `numero % 2 == 0`.
# - Operadores utilizados: `%`, `==`

numero = float(input("Ingrese un número: "))

print(f"El número {numero} es par?: {numero % 2 == 0}")
print(f"El número {numero} es impar?: {numero % 2 != 0}")
