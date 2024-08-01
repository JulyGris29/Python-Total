from collections import Counter
from collections import defaultdict
from  collections import namedtuple


"""numeros = [8,9,6,5,4,3,4,5,6,8,5,5,5]
print(Counter(numeros))
"""

"""frase = "al pan, pan y al vino, vino"
print(Counter(frase.split()))"""


"""serie = Counter([1,1,1,1,1,3,3,3,3,4])
print(serie.most_common())"""

"""mi_dic = {'uno':'verde', 'dos': 'azul',  'tres': 'rojo'}
print(mi_dic['dos'])"""


#defaultdict

"""mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dod'])
print(mi_dic)"""

"""mi_tupla = (500, 18,  100)
print(mi_tupla)"""

"""Persona= namedtuple('Persona', ['nommbre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 76)
print(ariel.peso)"""

"""lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)"""

"""  mi_diccionario = defaultdict(lambda: "Valor no hallado")
    mi_dic = {'edad': 44}
"""
lista_ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades.appendleft('italia')