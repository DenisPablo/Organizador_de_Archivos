# Organizador de Archivos

Este script se creó con el objetivo de organizar de forma rápida y cómoda archivos sueltos dentro de una carpeta. El script crea automáticamente las carpetas y mueve los archivos a las carpetas específicas según su extensión.

**ADVERTENCIA:** Es importante no cambiar el nombre de los archivos antes de ejecutar el script ya que esto puede causar que los archivos no sean movidos correctamente. El script debe ser ejecutado desde la raíz de la carpeta que desea organizar. Si se encuentran archivos repetidos, primero se moverán a la carpeta "Otros" y si ya existen en esa carpeta, se ignorarán y no serán movidos.

## Carpetas creadas

- Imagenes
- Documentos
- Audio
- Codigo
- Comprimidos
- Isos
- Otros

## Extensiones soportadas

- Extensiones de imagen: .jpg, .png, .jpeg
- Extensiones de documentos: .pdf, .txt, .doc, .docx, .xlsx
- Extensiones de audio: .mp3, .ogg, .vma, .m4r
- Extensiones de codigo: .cpp, .py
- Extensiones comprimidos: .rar, .zip

## Como usar

1. Descargue el script y colóquelo en la carpeta raíz que desea organizar
2. Ejecute el script
3. Siga las instrucciones en pantalla

## Requisitos

- Python 3.x
- shutil
- pathlib
