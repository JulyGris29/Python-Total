import re


"""
texto = "Si necessitas  ayudallama al (658)-598-9977 
las 24 horas al servicio de ayuda  online"

patron = 'ayuda'

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
"""

"""
texto = "llama al 545-535-6588 ya  mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'

resultado = re.search(patron,  texto)
print(resultado.group())
"""



"""
texto = "llama al 545-535-6588 ya  mismoss"

patron = r'\d{3}-\d{3}-\d{4}'

resultado = re.search(patron,  texto)

print(resultado.group()) """



clave = input("Clave: ")

patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)

print(chequear)