# Validación de email
# Descripción: Verificar si un email ingresado por el usuario contiene el carácter @ y
# termina en .com

email = input("Ingrese un email: ")

if "@" in email and email.endswith(".com"):
    print(f"El email {email} es valido")
else:
    print(f"El email {email} es invalido")