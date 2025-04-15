num1 = input("Ingrese un numero: ")
num2 = input("Ingrese otro numero: ")


lista_numeros = []
#una forma de guardarlo
lista_numeros.append(num1)
lista_numeros.append(num2)

#otra forma de guardarlo
lista_numeros = [num1, num2]

lista_pares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)

print(f"La lista completa es: {lista_numeros}")
print(f"La lista de numeros pares es: {lista_pares}")