# Lista de números pares
# Descripción: Dada una lista de números, filtrar solo los números pares. El usuario debe
# ingresar diez números, y por consola se debe mostrar la lista entera y una lista con solo los
# números pares.

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
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print(f"La lista completa es: {numeros}")
print(f"La lista de números pares es: {numeros_pares}")        
