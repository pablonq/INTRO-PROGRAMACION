# Suma de elementos en una lista
# Descripción: Calcular la suma de todos los elementos de una lista. El usuario debe ingresar
# diez números, los primeros cinco deben ser almacenados en una lista y los segundos cinco
# en otra, por pantalla se debe mostrar las dos listas, la suma de los elementos de cada lista
# y el numero mayor de cada lista.

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

numeros1 = [num1, num2, num3, num4, num5]
numeros2 = [num6, num7, num8, num9, num10]

suma1 = sum(numeros1)
suma2 = sum(numeros2)

print(f"La lista 1 es: {numeros1}")
print(f"La lista 2 es: {numeros2}")
print(f"La suma de la lista 1 es: {suma1}")
print(f"La suma de la lista 2 es: {suma2}")

mayor1 = max(numeros1)
mayor2 = max(numeros2)

print(f"El número mayor de la lista 1 es: {mayor1}")
print(f"El número mayor de la lista 2 es: {mayor2}")