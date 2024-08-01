from random import *
equipos = ['Den Bosh', 'Roda JC', 'Telstar', 'Dordrecht', 'Helmond']
apuestas = [ 2.5, 'Tiros de  esquina', 'Ambos Marcan', 'Gana Local','Empate', 'Visitante' ]

def equipos_futbol(lista):
    shuffle (lista)
    return lista
print(equipos_futbol(equipos,apuestas))