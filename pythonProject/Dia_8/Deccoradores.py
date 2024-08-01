def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada('Hola  july')

