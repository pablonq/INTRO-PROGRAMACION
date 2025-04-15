conjunto = set([1, 2, 3, 4, 5])
conjunto2 = {4, 5, 6, 7, 8}
conjunto3 = {5, 2}

#Teoria de conjuntos
#verificacion de subconjunto con issubset()
# subconjunto = conjunto3.issubset(conjunto)

#verificacion de superconjunto con con operadores de comparacion

#verificacion de superconjunto con issuperset()
superconjunto = conjunto.issuperset(conjunto3)
print(superconjunto)
#verificacion de superconjunto con operadores de comparacion
superconjunto = conjunto > conjunto3

#verificacion de elementos en comun con isdisjoint()

