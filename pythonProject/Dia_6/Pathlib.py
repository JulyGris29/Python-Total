from pathlib import Path, PureWindowsPath

'''carpeta = Path("C:/Users/Julian/OneDrive/Escritorio/PROYECTOS PROGRAMACION/pruebasPython.txt")

print(carpeta.read_text())'''

carpeta = Path("C:/Users/Julian/OneDrive/Escritorio/PROYECTOS PROGRAMACION/pruebasPython.txt")

ruta_windows = PureWindowsPath(carpeta)

print(carpeta)