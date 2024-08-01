class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('El animal  ha  nacido')

    def hablar(self):
        print('Este animal emite  un sonido')

class Pajaro(Animal):
    pass

piolin = Pajaro(2, 'amarillo')

print(piolin.color)

