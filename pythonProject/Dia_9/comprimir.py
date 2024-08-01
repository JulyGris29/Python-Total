#import zipfile
import shutil

"""mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()"""


#Otra forma de decomprimr
"""zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','r')

zip_abierto.extractall()"""

#Shutil Comprimir

"""capeta_origen = 'C:\\Users\\Julian\\Desktop\\Carpeta_Superior'

archivo_destino = 'Todo_Comprimido'

shutil.make_archive(archivo_destino, 'zip', capeta_origen)"""

#Shutil DEsComprimir

shutil.unpack_archive('Todo_Comprimido.zip', 'Extracccion Terminada', 'zip')