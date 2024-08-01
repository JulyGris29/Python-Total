'''Práctica Archivos y Funciones 1
Crea una función llamada abrir_leer() que abra
(open) un archivo indicado como parámetro,
y devuelva su contenido (read).
'''
'''def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.open
'''

'''Práctica Archivos y Funciones 2
Crea una función llamada sobrescribir() que abra
(open) un archivo indicado como parámetro, y sobrescriba
cualquier contenido anterior por el texto "contenido eliminado
'''
'''def sobreescribir(archivo):
    archivo_sobrescribir = open(archivo,'w')
    archivo_sobrescribir.write("contenido eliminado")'''

'''Práctica Archivos y Funciones 3
Crea una función llamada registro_error() que abra
(open) un archivo indicado como parámetro, y lo actualice 
añadiendo una línea al final que indique ("se ha registrad"
 " un error de ejecución").
Finalmente, debe cerrar el archivo abierto.'''

'''def registro_error(archivo):
    mi_archivo = open(archivo,'a')
    mi_archivo.write("se ha registrad un error de ejecución")
    mi__archivo.close()'''

