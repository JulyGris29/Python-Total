
"""
archivo =open('prueba.txt', 'w')
archivo.write('''soy el nuevo
texto
de
aca ''')

"""


"""archivo =open('prueba.txt', 'w')
archivo.writelines(['hola', 'mmundo', 'aqui', 'estoy'])


archivo.close()"""


"""archivo =open('prueba.txt', 'w')
lista = ['hola', 'mundo', 'aqui', 'estoy']
for p  in lista:
    archivo.writelines(p + '\n')

archivo.close()
"""

archivo =open('prueba.txt', 'a')

archivo.write('bienbenido')

archivo.close()