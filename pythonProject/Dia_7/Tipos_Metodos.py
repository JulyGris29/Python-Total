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




piolin = Pajaro('amarillo', 'canario')

#piolin.pintar_negro() ACCEDE Y MODIFICA atributos  del  objeto

#piolin.volar(50) ACCEDE A  OTROS METODOS

piolin.alas = False
print(piolin.alas) #MODIFICAR ALGO  QUE CORRESPONDE A LA  CLASE