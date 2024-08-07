@echo off

REM Eliminar carpetas de cache
rmdir /s /q "%CD%\src\minecraft_launcher_custom\__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en minecraft_launcher_custom
) else (
    echo Eliminando carpeta de cache en minecraft_launcher_custom
)

rmdir /s /q "%CD%\src\minecraft_launcher_custom\_internal_types\__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en minecraft_launcher_custom\_internal_types
) else (
    echo Eliminando carpeta de cache en minecraft_launcher_custom\_internal_types
)

rmdir /s /q "%CD%\src\__pycache__"
if %errorlevel% neq 0 (
    echo No hay carpetas de cache en la raiz
) else (
    echo Eliminando carpeta de cache en la raiz
)

mkdir "%CD%\build"
if %errorlevel% neq 0 (
    echo Carpeta de build creada
) else (
    echo Ya existe una carpeta de build
)

REM Definir variables de entorno
setlocal
set BUILD=2
set VERSION="2.0.1"
set PRODUCT="Kailand"
set COPYRIGHT="Launcher de Kailand, by GatoArtStudio"
set DESCRIPTION="Launcher Oficial de Kailand V"
set COMPANY="By GatoArtStudio X Kailand V"
set OUTPUT="%CD%\build"

REM Mostrar argumentos de compilacion
echo Argumentos de compilacion son %*

REM Ejecutar comando de compilacion
cd src & flet build windows -v --build-number %BUILD% --build-version %VERSION% --product %PRODUCT% --copyright %COPYRIGHT% --description %DESCRIPTION% --company %COMPANY% -o %OUTPUT% -vv

endlocal
