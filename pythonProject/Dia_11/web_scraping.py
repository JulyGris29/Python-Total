import bs4
import requests


resultado = requests.get('https://www.escueladirecta.com/courses')

print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()
