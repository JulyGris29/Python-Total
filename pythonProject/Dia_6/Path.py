from pathlib import Path

'''base = Path.home()
guia = Path(base,"Barcelona", "Sagrad_Familia")
print(base)
print(guia)'''

'''Práctica Path 1
Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home()'''




'''ruta_base = Path.home()

guia = ("Barcelona", "España")

print(guia)'''

'''Práctica Path 2
Implementa y crea una ruta relativa que nos permita llegar
 al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:


Almacena el directorio obtenido en la variable ruta. No olvides importar Path.'''

guia = Path("Curso Python","Día 6","practicas_path.py")
curso = guia.relative_to(Path("Curso Python"))
dia6 = guia.relative_to(Path("Curso Python", "Dia_6"))

print(curso)
print(dia6)

#practica = guia.relative_to(Path("practicas_path.py"))

