# Invertir una cadena
# Descripción: Invertir una cadena de texto usando métodos de cadenas. El usuario debe
# ingresar una palabra y por pantalla debe aparecer invertida.

palabra = input("Ingrese una palabra: ")
palabra_invertida = ""
for letra in palabra:
     palabra_invertida = letra + palabra_invertida

print(f"La palabra invertida es: {palabra_invertida}")



