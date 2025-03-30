def mi_funcion():
    variable_local = "Hola Mundo"
    print(variable_local)

mi_funcion()
# print(variable_local)  # Esto generaría un error

variable_global = "Soy global"

def imprimir_global():
    print(variable_global)

imprimir_global()  # Resultado: Soy global
print(variable_global)  # También es accesible fuera de la función

variable_global = "Soy global"

def modificar_global():
    global variable_global
    variable_global = "Modificado dentro de la función"
    print(variable_global)

modificar_global()  # Resultado: Modificado dentro de la función
print(variable_global)  # Ahora la variable global ha sido modificada

def funcion_externa():
    variable_externa = "Soy de la función externa"

    def funcion_interna():
        nonlocal variable_externa
        variable_externa = "Modificado por la función interna"
        print("Desde función interna:", variable_externa)

    funcion_interna()
    print("Desde función externa:", variable_externa)

funcion_externa()

