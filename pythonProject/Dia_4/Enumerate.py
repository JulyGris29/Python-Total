

"""lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1
"""
"""
lista = ['a','b','c']
for item in enumerate(lista):
    print(item)
"""
"""
lista = ['a','b','c']
for indice,item in enumerate(lista):
    print(indice,item)
    """

"""
lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples)
"""

"""
lista = ['a','b','c']
mis_tuples = list(enumerate(lista))
print(mis_tuples[2][1])
"""
"""
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
"""

"""Práctica Enumerador 2
Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices ."""

"""
lista_indices = "Python"
for indice, elemento in enumerate(lista_indices):

    print(indice,elemento)
    """
"""Práctica  enumerador 3"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)

