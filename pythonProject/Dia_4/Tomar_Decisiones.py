"""
mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se que animal tienes')


edad = 16
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >=7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')
 """
"""
num1 = input("Ingresa el primer número ")
num2 = input("Ingresa el segundo número ")

if num1 > num2:
    print(num1, 'es mayor que', num2)

num1 = input("Ingresa el primer número ")
num2 = input("Ingresa el segundo número ")

if num2 > num1:
    print(num2, 'es mayor que', num1)

num1 = input("Ingresa el primer número ")
num2 = input("Ingresa el segundo número ")

if num1 == num2:
    print(num1, 'y', num2, 'son iguales')"""
    
num1 = input("Ingresa el primer número ")
num2 = input("Ingresa el segundo número ")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")

elif num2 > num1:
    print(f"{num2} es mayor que {num1}")


elif num1 == num2:
    print(f"{num1} y {num2} son iguales")







    num1 = input("Ingresa el primer número ")
num2 = input("Ingresa el segundo número ")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")

elif num2 > num1:
    print(f"{num2} es mayor que {num1}")


elif num1 == num2:
    print("num1 y num2 son iguales")









    num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else: