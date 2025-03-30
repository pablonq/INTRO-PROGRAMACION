# Potencia y Módulo: Pide al usuario dos números. Calcula y muestra la potencia del primero
# elevado al segundo, así como el residuo de la división entre ambos.
# - Operadores utilizados: `**`, `%`

x = float(input("Ingrese un número: "))
y = float(input("Ingrese otro número: "))

potencia = x**y

residuo = x%y

print(f"La potencia de {x} elevado a {y} es {potencia}")
print(f"El residuo de {x} entre {y} es {residuo}")
