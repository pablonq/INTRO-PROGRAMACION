dato = "hola estoy estudiando python"
dato2 = 5
dato3 = 5.3


#Dir: Devuelve una lista con los nombres de todos los métodos y atributos del objeto
dir(dato)


#upper: Devuelve una cadena con todos los caracteres en mayúscula
dato.upper()


#lower: Devuelve una cadena con todos los caracteres en minúscula
dato.lower()


#capitalize: Devuelve una cadena con el primer carácter en mayúscula y el resto en minúscula
dato.capitalize()

#find: Devuelve el índice del primer carácter de la cadena
dato.find("h")

#index: Devuelve el índice del primer carácter de la cadena
dato.index("h")

#isnumeric: Devuelve True si todos los caracteres de la cadena son numéricos
dato.isnumeric()

#isalpha: Devuelve True si todos los caracteres de la cadena son alfabéticos
dato.isalpha()

#count: Cuenta el número de veces que aparece una cadena
dato.count("h")

#len: Devuelve el número de caracteres de la cadena
dato.len()

#endswith: Devuelve True si la cadena termina con una cadena
dato.endswith("python")

#startswith: Devuelve True si la cadena comienza con una cadena
dato.startswith("hola")

#replace: Reemplaza una cadena por otra
dato.replace("hola", "hola2")

#split: Divide la cadena en una lista de cadenas
dato.split(" ")

#strip: Elimina los espacios en blanco al inicio y al final de la cadena
dato.strip()

#join: Une una lista de cadenas en una cadena
dato.join(["hola", "estoy", "estudiando", "python"])


