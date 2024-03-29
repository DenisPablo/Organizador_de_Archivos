# El script analiza un directorio en concreto y organizara los archivos en su interior siguiendo las siguientes reglas:
# si el archivo no tiene una extension contemplada por el script ira a la carpeta otros y las carpetas que no esten dentro del diccionario tambien iran a otros

from pathlib import Path
from shutil import move

def organizador_archivos(directorio_raiz):
    carpetas_extensiones = {
        '.jpg': 'Imagenes',
        '.png': 'Imagenes',
        '.jpeg': 'Imagenes',
        '.pdf': 'Documentos',
        '.txt': 'Documentos',
        '.doc': 'Documentos', 
        '.docx': 'Documentos', 
        '.xlsx': 'Documentos', 
        '.mp3': 'Audio',
        '.ogg': 'Audio', 
        '.vma': 'Audio', 
        '.m4r': 'Audio', 
        '.cpp': 'Codigo', 
        '.py': 'Codigo',
        '.rar': 'Comprimido', 
        '.zip': 'Comprimido', 
    }

    # Crea las carpetas incluidas en el diccionario para cada clasificacion de archivos.
    for carpeta in set(carpetas_extensiones.values()):
        (directorio_raiz / carpeta).mkdir(exist_ok = True)

    # Crea la carpeta "Otros" donde iran todo aquellos archivos con extensiones no contempladas asi como carpetas ajenas al script 
    carpeta_otros = 'Otros'
    (directorio_raiz / carpeta_otros).mkdir(exist_ok=True)


    for elemento in directorio_raiz.iterdir():
        if elemento.is_file() and elemento.name == "organizador.py" :
            carpeta_destino = carpetas_extensiones.get(elemento.suffix, carpeta_otros)
        elif elemento.is_dir() and elemento.name not in set(carpetas_extensiones.values()) and elemento.name != 'Otros':
            carpeta_destino = carpeta_otros
        else:
            continue

        # Crea la ruta de destino
        destino = directorio_raiz / carpeta_destino / elemento.name

        try:
            if not destino.exists():
                move(elemento, destino)
        except Exception as e:
            print(f'Error al mover {elemento.name}: {e}')

if __name__ == '__main__':
        ruta_directorio_raiz = Path.cwd()
        organizador_archivos(ruta_directorio_raiz)