#!/bin/bash

# Definir colores
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

# Ingresa a la carpeta de contruccion

rm -vr $PWD/src/minecraft_launcher_cunstom/__pycache__ | echo -e "${GREEN}Eliminando carpeta de cache${NC}" || echo -e "${RED}No hay carpetas de cache${NC}"
rm -vr $PWD/src/minecraft_launcher_cunstom/_internal_types/__pycache__ | echo -e "${GREEN}Eliminando carpeta de cache${NC}" || echo -e "${RED}No hay carpetas de cache${NC}"
rm -vr $PWD/src/__pycache__ | echo -e "${GREEN}Eliminando carpeta de cache${NC}" || echo -e "${RED}No hay carpetas de cache${NC}"

mkdir $PWD/build | echo -e "${GREEN}Carpeta de build creada${NC}" || echo -e "${RED}Ya existe una carpeta de build${NC}"

BUILD=1
VERSION="2.0.1"
PRODUCT="Kailand"
COPYRIGHT="Launcher de Kailand, by GatoArtStudio"
DESCRIPTION="Launcher Oficial de Kailand V"
COMPANY="By GatoArtStudio X Kailand V"
OUTPUT="$PWD/build"

echo -e "${GREEN}Argumentos de compilacion son $BUILD $VERSION $PRODUCT $COPYRIGHT $DESCRIPTION $COMPANY $OUTPUT${NC}"

cd src && flet build linux -v --build-number $BUILD --build-version "$VERSION" --product "$PRODUCT" --copyright "$COPYRIGHT" --description "$DESCRIPTION" --company "$COMPANY" -o "$OUTPUT"