class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Padre, Madre):
    pass

mi_hija = Padre()
mi_hija.reir()
mi_hija1 = Madre()
mi_hija1.trabajar()