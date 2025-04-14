# Palabras más largas que 5 caracteres
# Descripción: Filtrar palabras de una lista que tengan más de 5 caracteres. El usuario debe
# ingresar cinco palabras y por consola se debe mostrar la lista de las cinco y una lista
# conformada por las que tengan cinco letras o mas.

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")
palabra4 = input("Ingrese la cuarta palabra: ")
palabra5 = input("Ingrese la quinta palabra: ")

palabras = [palabra1, palabra2, palabra3, palabra4, palabra5]
palabras_largas = []

for palabra in palabras:
    if len(palabra) >= 5:
        palabras_largas.append(palabra)

print(f"La lista completa es: {palabras}")
print(f"La lista de palabras largas es: {palabras_largas}")