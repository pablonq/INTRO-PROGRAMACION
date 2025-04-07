edad = 25
tiene_licencia = True

puede_conducir = (edad >= 18) and tiene_licencia
  

# ----------

esta_lloviendo = False
es_frio = True

quiere_quedarse_en_casa = esta_lloviendo or es_frio  

# ----------

numero = 15

es_multiplo_de_3 = (numero % 3 == 0)
es_multiplo_de_5 = (numero % 5 == 0)

es_multiplo_de_3_o_5 = es_multiplo_de_3 or es_multiplo_de_5 
es_multiplo_de_3_y_5 = es_multiplo_de_3 and es_multiplo_de_5
no_es_multiplo_de_3 = not es_multiplo_de_3 