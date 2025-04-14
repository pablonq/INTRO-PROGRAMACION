# Actualizar valores en un diccionario
# Descripción: Aumentar el valor de una clave específica en un diccionario. El usuario
# deberá ingresar la clave a actualizar y luego la cantidad. Por consola se debe mostrar el
# diccionario actualizado.
# inventario = {"manzanas": 10, "peras": 5, "uvas": 20}

inventario = {"manzanas": 10, "peras": 5, "uvas": 20}

clave = input("Ingrese la clave a actualizar: ")
cantidad = float(input("Ingrese la cantidad a agregar: "))

if clave in inventario:
    inventario[clave] += cantidad
else:
    inventario[clave] = cantidad

print(f"El inventario actualizado es: {inventario}")