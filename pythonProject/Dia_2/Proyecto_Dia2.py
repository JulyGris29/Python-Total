nombre = input("Cual es tu nombre?: ")
ventas = (input(" Cuanto es el valor de ventas este  mes?: "))

ventas = int(ventas)

comision = ventas * 13 / 100

comision= round(comision)

print(f"Hola  {nombre}, tus comisiones de este mes son de $ {comision}")
