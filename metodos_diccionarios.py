mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Neuquen"}

#keys: Devuelve una lista con las claves del diccionario, tambien sirve para recorrer el diccionario
mi_diccionario.keys()
# print(mi_diccionario.keys())

#get: Devuelve el valor de una clave
mi_diccionario.get("nombre")
# print(mi_diccionario.get("nombre"))

#clear: Elimina todos los elementos del diccionario
mi_diccionario.clear()
# print(mi_diccionario)

#pop: Elimina un elemento del diccionario por clave
mi_diccionario.pop("nombre")
# print(mi_diccionario)

#popitem: Elimina el último elemento del diccionario
mi_diccionario.popitem()
# print(mi_diccionario)

#update: Actualiza el diccionario con los elementos de otro diccionario
mi_diccionario.update({"nombre": "Juan", "edad": 30, "ciudad": "Neuquen"})
# print(mi_diccionario)

#values: Devuelve una lista con los valores del diccionario
mi_diccionario.values()
# print(mi_diccionario.values())

#items: Devuelve una lista con los pares clave-valor del diccionario
mi_diccionario.items()
# print(mi_diccionario.items())
        