# Concatenación de cadenas
# Descripción: Unir todas las palabras de una lista en una sola cadena separada por
# espacios. El usuario debe ingresar cinco palabras y por consola se debe mostrar la lista de
# las cinco y una cadena separada por espacios.

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")
palabra4 = input("Ingrese la cuarta palabra: ")
palabra5 = input("Ingrese la quinta palabra: ")

palabras = [palabra1, palabra2, palabra3, palabra4, palabra5]
cadena = " ".join(palabras)

print(f"La lista completa es: {palabras}")
print(f"La cadena es: {cadena}")