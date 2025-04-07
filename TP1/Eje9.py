# Número Positivo y Par (Expresión Booleana): Pide al usuario un número y evalúa si es positivo
# y par. Muestra el resultado de la expresión `numero > 0 and numero % 2 == 0`.
# - Operadores utilizados: `>`, `%`, `and`


numero = float(input("Ingrese un número: "))

print(f"El número {numero} es par y mayor a 0?: {numero % 2 == 0 and numero > 0}")
