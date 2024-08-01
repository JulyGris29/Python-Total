'''class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1,oveja1]

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)'''

'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
'''
'''class Samurai():
    def atacar(self):
        print("Ataque con katana")

tuerquita= Mago()
higuita = Arquero()
bruce_lee = Samurai()

personajes = [tuerquita,higuita,bruce_lee]

for i in personajes:
    i.atacar()'''


class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

tuerquita= Mago()
higuita = Arquero()
bruce_lee = Samurai()

personajes = [tuerquita,higuita,bruce_lee]

def personaje_defender(personaje):
    personaje.defender()

tuerquita.defender()

