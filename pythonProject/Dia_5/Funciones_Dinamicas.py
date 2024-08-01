'''def chequear_n3_cifras(numero):
    return numero in range(100,100)

suma = 455+545

resultado = chequear_n3_cifras(suma)
print(resultado)'''

'''def chequear_n3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras

resultado = chequear_n3_cifras([333,44,755])
print(resultado)'''

'''def chequear_n3_cifras(lista):

    for n in lista:
        if n in range(100,100):
            return True
        else:
            pass

    return False

resultado = chequear_n3_cifras([33,44,55])
print (resultado)'''


'''Práctica Funciones Dinámicas 1
Crea una función (todos_positivos) que reciba una lista de números como 
parámetro, y devuelva True si todos los valores de una lista son positivos, 
y False si al menos uno de los valores es negativo.
Crea una lista llamada lista_numeros con valores positivos y negativos.'''



'''lista_numeros = [1,2,3-2-3,55,4,66,-12,-45]


def todos_positivos(lista_numeros):

    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True'''



'''lista_numeros = [1,50,500,5000,750,600]

def suma_menores(lista_numeros):
    suma = 0

    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma
print(suma_menores(lista_numeros))'''

'''Práctica Funciones Dinámicas 3
Crea una función (cantidad_pares) que cuente la cantidad de números pares
que existen en una lista (lista_numeros), 
y devuelva el resultado de dicha cuenta.'''

lista_numeros = [1,2,3,4,5,6,8,6,12,1,16,18,20,22,24,26,28]

def cantidad_pares(lista_numeros):

    pares = []

    for n in lista_numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            pass
    return pares
print(cantidad_pares(lista_numeros))

