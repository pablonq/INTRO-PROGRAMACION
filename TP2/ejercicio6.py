# Conteo de vocales
# Descripción: Contar cuántas vocales hay en una cadena de texto. El usuario debe ingresar
# una frase.

frase = input("Ingrese una frase: ").lower()
vocales = "aeiou"

contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales")