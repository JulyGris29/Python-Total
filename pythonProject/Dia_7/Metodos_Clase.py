class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio,')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el  pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)# NO MODIFICA LOS DE INSTANCIA PERO SI LOS  DE  CLASE

Pajaro.poner_huevos(3)


