"""lista = (58,96,62,74,95)

print(f"El menor es : {min(lista)} y el mayor es: {max(lista)}")"""

"""nombres = ["juan"," pablo","Alicia","Jose"]
print(min(nombres))"""

"""nombre = "Pablo"
print (min(nombre.lower()))"""

"""dic = {'C1':45,'C2': 11}
print(min(dic.values()))"""




"""lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)
"""

"""Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números,
 y almacénalo en una variable llamada rango:"""

"""lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
mayor = (max(lista_numeros))
menor = (min(lista_numeros))

rango = mayor-menor
print(rango)"""


"""Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a 
partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, 
"José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético,
 y almacénalo en una variable llamada ultimo_nombre.
"""
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
print(edad_minima)

ultimo_nombre = max(diccionario_edades).lower()
print(ultimo_nombre)