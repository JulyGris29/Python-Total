

'''def suma(**kwargs):

    total = 0

    for clave,  valor in kwargs.items():
        print(f'{clave} = {valor}')
        total  += valor

    return total
print(suma(x=3, y=5, z=2))
'''
'''
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de 
parémetros que se entregan, y devuelva esa cantidad como resultado.
'''
'''
def cantidad_atributos(**kwargs):
    cantidad = 0

    for i in kwargs.items():
        cantidad += 1
        return cantidad
'''

'''
Práctica sobre Argumentos Indefinidos (**kwargs) 2
Crea una función llamada lista_atributos que devuelva 
en forma de lista los valores de los atributos entregados 
en forma de palabras clave (keywords). La función debe preveer
recibir cualquier cantidad de argumentos de este tipo.
'''
'''def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return valor
'''

'''
Práctica sobre Argumentos Indefinidos (**kwargs) 3
Crea una función llamada describir_persona, 
que tome como parámetros su nombre y luego una
 cantidad indetermida de argumentos. Esta función 
 deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
'''

def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}')
    for clave, valor in kwargs.items():
        print(f'{clave}, {valor}')



describir_persona(nombre = 'María', Color_ojos =  'Azules', Color_pelo = 'rubio')
