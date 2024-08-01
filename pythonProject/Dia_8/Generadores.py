"""def mi_funcio():
    lista = []
    for x in range (1, 5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range (1, 5):
        yield x * 10

print(mi_funcio())
print(mi_generador())

g = mi_generador()
print(next(g))
print(next(g))"""

"""
def mi_generador():
    x = 1
    yield x

    x +=1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))"""

"""Práctica Generadores 1
Crea un generador (almacenado en la variable generador) 
que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, y entregando un número consecutivo
superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio."""


"""def secuencia():
    n = 0
    while True:
        n += 1
        yield n

generador = secuencia()
print(next(generador))
print(next(generador))
print(next(generador))

print(next(generador))

print(next(generador))
"""
"""
Práctica Generadores 2
Crea un generador (almacenado en la variable generador)
que sea capaz de devolver de manera indefinida múltiplos de 7,
iniciando desde el mismo 7, y que cada vez que sea
llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
"""
"""def multiplos_7():
    n = 1
    while True:
        yield 7 * n
        n += 1
generador = multiplos_7()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))"""

"""Práctica Generadores 3
Crea un generador que reste una a una las
vidas de un personaje de videojuego, y devuelva un 
mensaje cada vez que sea llamado:



"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida"""

def restar_vida():
    vidas = "Te quedan 3 vidas"
    yield vidas

    vidas = "Te quedan 2 vidas"
    yield vidas

    vidas = "Te queda 1 vidas"
    yield vidas

    vidas = "Game  Over"
    yield vidas

vida_perdida = restar_vida()
print(next(vida_perdida))
print(next(vida_perdida))
print(next(vida_perdida))
print(next(vida_perdida))
print(next(vida_perdida))


