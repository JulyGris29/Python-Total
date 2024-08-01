import random
from random import choice

def mezclar_palabras():
    lista_palabras = ['gato','perro','jirafa', 'leon', 'elefante']
    escoger_palabra = random.choice(lista_palabras)
    return escoger_palabra

def mostrar_tablero(palabra_secreta, letra_adivinada):
    tablero = ''

    for letra in palabra_secreta:
        tablero = ''
        for letra in palabra_secreta:
            if letra in letra_adivinada:
                tablero += letra
            else:
                tablero += ""
    print(tablero)

def ahorcado():
    palabra_secreta = mezclar_palabras()
    letra_adivinada =[]
    intentos_restantes = 6

    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta,letra_adivinada)
        letra = input("Introduce  una  letra: ").lower()

        if letra in letra_adivinada:
            print(f"Has adivinado una letra, prueba otra")
            continue

        if letra in palabra_secreta:
            letra_adivinada.append(letra)
            if set(letra_adivinada) == set(palabra_secreta):
                print(f"Has adivinado el juego, la palabra secreta era {palabra_secreta}")
                break
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta, te quedan {intentos_restantes}")
    if intentos_restantes == 0:
        print(f"Has  perdido, la  palabra secreta erag"
              f" {palabra_secreta}")
ahorcado()






















