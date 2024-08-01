"""nombres = ['Ana', 'Hugo','Valeria']
edades = [65,29,30]
ciudad = 'Lima', 'barranquilla', 'Medellín'

combinados = list(zip(nombres, edades,ciudad))
for nombres,edades,ciudad in combinados:
    print(f'{nombres} tiene {edades} y vive e
    n {ciudad}')

"""

"""  P´ractica zip 1
  """

"""capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinar = (list(zip(capitales,paises)))
for capitales,paises in combinar:
    print(f'La capital de {paises} es {capitales}')
    """

"""Práctica 2"""

"""marcas = ['Reebook', 'Polito','Diesel']
productos = ['Tenis', 'Ropa','Loción']

mi_zip = zip(marcas,productos)
for marcas,productos in mi_zip:
  print (mi_zip)"""


espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espaniol, portugues, ingles))


print(numeros)
