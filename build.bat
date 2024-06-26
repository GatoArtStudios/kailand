@echo off

REM Ingresa a la carpeta de construcción
cd src
if %errorlevel% neq 0 (
    echo No se encontro la carpeta de construccion
) else (
    echo Entrando en carpeta de construccion
)

REM Eliminar carpetas de cache
rmdir /s /q "minecraft_launcher_custom\__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en minecraft_launcher_custom
) else (
    echo Eliminando carpeta de cache en minecraft_launcher_custom
)

rmdir /s /q "minecraft_launcher_custom\_internal_types\__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en minecraft_launcher_custom\_internal_types
) else (
    echo Eliminando carpeta de cache en minecraft_launcher_custom\_internal_types
)

rmdir /s /q "__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en la raiz
) else (
    echo Eliminando carpeta de cache en la raiz
)

REM Definir variables de entorno
setlocal
set BUILD=2
set VERSION=1.0.25
set PRODUCT=Kailand
set COPYRIGHT="Launcher de Kailand, by GatoArtStudio"
set DESCRIPTION="Launcher Oficial de Kailand V"
set COMPANY="By GatoArtStudio X Kailand V"
set OUTPUT="C:\Users\%USERNAME%\Documents\GitHub\kailand\build"

REM Mostrar argumentos de compilacion
echo Argumentos de compilacion son %*

REM Ejecutar comando de compilacion
flet build windows -v --build-number %BUILD% --build-version %VERSION% --product %PRODUCT% --copyright %COPYRIGHT% --description %DESCRIPTION% --company %COMPANY% -o %OUTPUT%

endlocal
