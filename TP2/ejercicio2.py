# Número par o impar
# Descripción: Determinar si un número es par o impar. El usuario debe ingresar un numero
# y por consola debe aparecer la determinación.

num = float(input("Ingrese un número: "))

if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar")