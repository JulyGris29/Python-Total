vendedor = input("Cual es tu nombre? ")
ventas = int(input("Cuanto es el valor de ventas este  mes?"))
ventas = round(ventas * 13 / 100,2)
print(f"Ok {vendedor}, este mes ganaste $  {ventas} pesos")