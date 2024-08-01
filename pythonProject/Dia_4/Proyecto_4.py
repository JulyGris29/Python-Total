from random import *

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Cual es tu  nombre?: "),
print(f"Hola, {nombre}, he pensado un número entre el 1 y el 100\n y tienes 8 intentos para adivinarlo")

while intentos < 8:
    estimado = int(input("Ingresa un número: "))
    intentos += 1

    if estimado < numero_secreto:
        print("Di un número más alto")
    elif estimado > numero_secreto:
        print("Di un número más bajo")
    else:
        print(f"Felicitaciones {nombre} has adivinado el númmero en {intentos} intentos")
        break
    if estimado != numero_secreto:
        print(f" Lo  siento, se han agotado los  intentos. El  número secreto es {numero_secreto}")





