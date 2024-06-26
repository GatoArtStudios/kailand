cd src
setlocal
set BUILD=26
set VERSION="1.0.0"
set PRODUCT="Kailand"
set COPYRIGHT="Launcher de Kailand, by GatoArtStudio"
set DESCRIPTION="Launcher Oficial de Kailand V"
set COMPANY="By GatoArtStudio X Kailand V"

flet build windows -v --build-number %BUILD% --build-version %VERSION% --product %PRODUCT% --copyright %COPYRIGHT% --description %DESCRIPTION% --company %COMPANY% -o "C:\Users\%USERNAME%\Documents\GitHub\kailand\build"
@REM flet build linux -v --build-number %BUILD% --build-version %VERSION% --product %PRODUCT% --copyright %COPYRIGHT% --description %DESCRIPTION% --company %COMPANY%
@REM flet build macos -v --build-number %BUILD% --build-version %VERSION% --product %PRODUCT% --copyright %COPYRIGHT% --description %DESCRIPTION% --company %COMPANY%