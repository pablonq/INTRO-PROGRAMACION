# Buscar clave en un diccionario
# Descripción: Buscar una clave en un diccionario e imprimir su valor si existe.
# diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Neuquen"}

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Neuquen"}

clave = input("Ingrese la clave a buscar: ")

if clave in diccionario:
    print(f"El valor de la clave '{clave}' es: {diccionario[clave]}")
else:
    print(f"La clave '{clave}' no existe en el diccionario.")