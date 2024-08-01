'''Escribe una función
(puedes ponerle cualquier nombre quequieras)
que reciba cualquier palabra como parámetro,
y que devuelva todas sus letras únicas
(sin repetir)
pero en ordenalfabético.
Por ejemplo si al invocar esta función pasamos
la palabra"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
'''

def letras_unicas(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)
    mis_lista = list(mi_set)
    mis_lista.sort()

    return mis_lista

print(letras_unicas("entretenido"))