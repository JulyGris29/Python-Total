'''Práctica Métodos 1
Crea una clase Perro. Dicho perro debe poder ladrar.

Crea el método ladrar() y ejecútalo en una instancia de Perro.
 Cada vez que ladre, debe mostrarse en pantalla "Guau!".'''

'''class Perro:

    def ladrar(self):
        print("Guau")

firulais = Perro()
firulais.ladrar()
'''

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
mi_libro = Libro('El dia  y la  noche' ,' Joaquin' ,23)

print(len(mi_libro))