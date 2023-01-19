from pathlib import Path
from shutil import move
from os import mkdir

carpetas = {'Imagenes', 'Documentos', 'Audio', 'Codigo', 'Comprimidos', 'Isos', 'Otros'}
ruta = Path().absolute()
directorio = Path(ruta)


def crear_carpetas():
    carpetas_existentes = set()

    for fichero in directorio.iterdir():
        carpetas_existentes.add(fichero.name)

    try:
        for carpeta in carpetas:
            if carpeta not in carpetas_existentes:
            
                mkdir(carpeta)
    except Exception as e:
        print(f'Ocurrio un error al crear las carpetas :( {e}')


def verificar_directorios():
    contador = 0

    for fichero in directorio.iterdir():
        if fichero.name in carpetas:
            contador += 1

    if contador != len(carpetas):
        if input("Faltan Carpetas desea crearlas: [Y]es / [N]o: ").upper() == 'Y':
            crear_carpetas()
        else:
            return False

    return True


def mover_archivos():
    c_imagenes = 0
    c_documentos = 0
    c_audio = 0
    c_codigo = 0
    c_comprimidos = 0
    c_isos = 0
    desconocidos = 0

    ext_imagenes = ['.jpg', '.png', '.jpeg']
    ext_documetos = ['.pdf', '.txt', '.doc', '.docx', '.xlsx']
    ext_audio = ['.mp3', '.ogg', '.vma', '.m4r']
    ext_codigo = ['.cpp', '.py']
    ext_comprimidos = ['.rar', '.zip']

    for fichero in directorio.iterdir():
        if fichero.suffix in ext_imagenes and not Path.exists(ruta / 'Imagenes' / fichero.name):
                try:
                    move(fichero, Path('Imagenes'))
                    c_imagenes += 1
                except Exception as e:
                    print(f'Ocurrio un error al mover los archivos :( {e}')
        elif fichero.suffix in ext_documetos and not Path.exists(ruta / 'Documentos' / fichero.name):
            try:
                move(fichero, Path('Documentos'))
                c_documentos += 1
            except Exception as e:
                    print(f'Ocurrio un error al mover los archivos :( {e}')
        elif fichero.suffix in ext_audio and not Path.exists(ruta / 'Audios' / fichero.name):
            try:
                move(fichero, Path('Audios'))
                c_audio += 1
            except Exception as e:
                    print(f'Ocurrio un error al mover los archivos :( {e}')
        elif fichero.suffix in ext_codigo and fichero.name != 'organizador.py' and not Path.exists(
                ruta / 'Codigo' / fichero.name):
            try:
                move(fichero, Path('Codigo'))
                c_codigo += 1
            except Exception as e:
                    print(f'Ocurrio un error al mover los archivos :( {e}')
        elif fichero.suffix in ext_comprimidos and not Path.exists(ruta / 'Comprimidos' / fichero.name):
            try:
                move(fichero, Path('Comprimidos'))
                c_comprimidos += 1
            except Exception as e:
                print(f'Ocurrio un error al mover los archivos :( {e}')

        elif fichero.suffix == '.iso' and not Path.exists(ruta / 'Isos' / fichero.name):
            try:
                move(fichero, Path('Isos'))
                c_isos += 1
            except Exception as e:
                print(f'Ocurrio un error al mover los archivos :( {e}')

        elif fichero.name not in carpetas and fichero.name != 'organizador.py' and not Path.exists(
                ruta / 'Otros' / fichero.name) and fichero.suffix != "":
            try:
                move(fichero, Path('Otros'))
                desconocidos += 1
            except Exception as e:
                print(f'Ocurrio un error al mover los archivos :( {e}')

    print("Operacion finalizada:")
    print(f"Total de Imagenes movidas: [{c_imagenes}]")
    print(f"Total de Documentos movidos: [{c_documentos}]")
    print(f"Total de Audios movidos: [{c_audio}]")
    print(f"Total de archivos de Codificacion movidos: [{c_codigo}].")
    print(f"Total de archivos Comprimidos movidos: [{c_comprimidos}]")
    print(f"Total de archivos Isos movidos: [{c_isos}]")
    print(f"[{desconocidos}] No pudieron ser identificados.")
    print(
        f"Total de archivos movidos: [{c_imagenes + c_isos + c_documentos + c_audio + c_codigo + c_comprimidos + desconocidos}]")

if __name__ == "main":
    if verificar_directorios():
        mover_archivos()
    else:
        print("Error al ejercutar")