# Juego de Adivinanza (Expresión Booleana): Genera un número aleatorio entre 1 y 10 (usa
# `random.randint(1, 10)`) y pide al usuario que adivine el número. Evalúa si el número ingresado
# es igual al número secreto. Muestra el resultado de la expresión `adivinanza ==
# numero_secreto`.
# - Operadores utilizados: `==`

import random

numero_secreto = random.randint(1, 10)

adivinanza = float(input("Adivine el número: "))

print(f"El número {adivinanza} es igual al número secreto?: {adivinanza == numero_secreto}")
