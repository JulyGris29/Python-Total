'''
def multiplicar(num1, num2):
    return num1 * num2


resultado = multiplicar(4, 5)
print(resultado)
'''

'''
def potencia(num1,num2):
    return num1**num2

resultado = potencia(3,4)
print(resultado)'''


'''def usd_a_eur(dinero):
    return dinero * 0.90


valor = usd_a_eur(50)
print(valor)'''

'''Práctica Return 3
Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada
como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y
en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"

También, deberás crear una variable llamada palabra, que contenga el 
string que tú prefieras, para sumisitrarle como argumento a la función creada.'''


'''palabra = "Python"


def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = (palabra.upper)
    return palabra
print(palabra)'''


palabra = "Curso de Python"

def invertir_palabra(texto):
    palabra = texto[::-1]
    palabra = texto.upper
    return palabra
print(palabra)


