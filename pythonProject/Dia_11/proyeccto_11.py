import bs4
import requests

'''url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(len(sopa.select('.product_pod')))
'''

"""url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


libros = sopa.select('.product_pod')

ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)"""

# Crear url sin número de página
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

# Iterar páginas
for pagina in range(1, 51):

    #crear spa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar entre los libros
    for libro in libros:

        # chequear que tengan 4  o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Four')):

            # guardar titulo  en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver los  libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)



