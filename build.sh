#!/bin/bash

# Ingresa a la carpeta de contruccion

cd src | echo 'Entrando en carpeta de construccion' || echo 'No se encontro la carpeta de construccion'

rm -vr /minecraft_launcher_cunstom/__pycache__/ | echo 'Eliminando carpeta de cache' || echo 'No hay carpetas de cache'
rm -vr /minecraft_launcher_cunstom/_internal_types/__pycache__/ | echo 'Eliminando carpeta de cache' || echo 'No hay carpetas de cache'
rm -vr /__pycache__/ | echo 'Eliminando carpeta de cache' || echo 'No hay carpetas de cache'

BUILD=2
VERSION='1.0.25'
PRODUCT='Kailand'
COPYRIGHT="Launcher de Kailand, by GatoArtStudio"
DESCRIPTION="Launcher Oficial de Kailand V"
COMPANY="By GatoArtStudio X Kailand V"
OUTPUT='/home/gatoartstudio/tools/kailand'

echo 'Argumentos de compilacion son ' $@

flet build linux -v --build-number $BUILD --build-version $VERSION --product $PRODUCT --copyright $COPYRIGHT --description $DESCRIPTION --company $COMPANY -o $OUTPUT