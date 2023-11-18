# El script analiza un directorio en concreto y organizara los archivos en su interior siguiendo las siguientes reglas:
# si el archivo no tiene una extension contemplada por el script ira a la carpeta otros y las carpetas que no esten dentro del diccionario tambien iran a otros

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import sys
from pathlib import Path
from shutil import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class OrganizadorService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'OrganizadorArchivosService'
    _svc_display_name_ = 'Organizador de Archivos Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(120)
        self.is_alive = True

    def SvcStop(self, args):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()

    def main(self):
        ruta_directorio_raiz = Path(r'C:\Users\denis\OneDrive\Documentos')
        handler = Organizador_de_archivos_handler(ruta_directorio_raiz)
        observer = Observer()
        observer.schedule(handler, path=ruta_directorio_raiz, recursive=False)
        observer.start()

        try:
            while self.is_alive:
                    observer.join(timeout=1)
        except KeyboardInterrupt:
                observer.stop()

        observer.join()

class Organizador_de_archivos_handler(FileSystemEventHandler):
    def __init__(self, directorio_raiz):
        super().__init__()
        self.directorio_raiz = directorio_raiz

    def on_created(self, event):
        print(f'Nuevo archivo detectado: {event.src_path}')
        organizador_archivos(self.directorio_raiz)

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
        if elemento.is_file():
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

    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(OrganizadorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(OrganizadorService)