# Eliminar duplicados de una lista
# Descripción: Eliminar elementos duplicados de una lista. El usuario debe ingresar 10
# numeros, el programa debe eliminar los duplicados, por consola se debe mostrar la lista
# con los números restantes.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))  
num3 = float(input("Ingrese el tercer número: "))  
num4 = float(input("Ingrese el cuarto número: "))  
num5 = float(input("Ingrese el quinto número: "))  
num6 = float(input("Ingrese el sexto número: "))  
num7 = float(input("Ingrese el septimo número: "))  
num8 = float(input("Ingrese el octavo número: "))  
num9 = float(input("Ingrese el noveno número: "))  
num10 = float(input("Ingrese el decimo número: "))  

numeros = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
numeros_unicos = []

for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

print(f"La lista completa es: {numeros}")
print(f"La lista sin duplicados es: {numeros_unicos}")