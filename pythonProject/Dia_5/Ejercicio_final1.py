
'''Crea una función llamada devolver_distintos() que reciba 3integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio.
'''

def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
print(devolver_distintos(20,5,7))



