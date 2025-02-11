@echo off
title Configuracion del Entorno Virtual de Django

:: Colores
set RED=[91m
set GREEN=[92m
set YELLOW=[93m
set BLUE=[94m
set RESET=[0m

:: Mensaje de bienvenida
echo %BLUE%**************************************************
echo *    Bienvenido al Script de Configuracion de Django   *
echo *            Creando su Entorno Virtual               *
echo **************************************************%RESET%
echo.

:: Verificar si virtualenv esta instalado
echo %YELLOW%Verificando si virtualenv esta instalado...%RESET%
where virtualenv >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo %RED%virtualenv no esta instalado.%RESET%
    echo %YELLOW%Instalando virtualenv...%RESET%
    pip install virtualenv
    if %ERRORLEVEL% neq 0 (
        echo %RED%Error: No se pudo instalar virtualenv.%RESET%
        pause
        exit /b %ERRORLEVEL%
    )
    echo %GREEN%virtualenv instalado exitosamente.%RESET%
) else (
    echo %GREEN%virtualenv ya esta instalado.%RESET%
)
echo.

:: Verificar si el entorno virtual ya existe
echo %YELLOW%Verificando si el entorno virtual ya existe...%RESET%
if exist .venv (
    echo %GREEN%El entorno virtual ya existe.%RESET%
) else (
    echo %YELLOW%Creando el entorno virtual...%RESET%
    python -m venv .venv
    if %ERRORLEVEL% neq 0 (
        echo %RED%Error: No se pudo crear el entorno virtual.%RESET%
        pause
        exit /b %ERRORLEVEL%
    )
    echo %GREEN%Entorno virtual creado exitosamente.%RESET%
)
echo.

:: Activar el entorno virtual
echo %YELLOW%Activando el entorno virtual...%RESET%
call .venv\Scripts\activate
if %ERRORLEVEL% neq 0 (
    echo %RED%Error: No se pudo activar el entorno virtual.%RESET%
    pause
    exit /b %ERRORLEVEL%
)
echo %GREEN%Entorno virtual activado.%RESET%
echo.

:: Instalar dependencias desde requirements.txt
echo %YELLOW%Instalando dependencias desde requirements.txt...%RESET%
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo %RED%Error: No se pudieron instalar las dependencias.%RESET%
    pause
    exit /b %ERRORLEVEL%
)
echo %GREEN%Dependencias instaladas exitosamente.%RESET%
echo.

:: Mensaje final
echo %BLUE%**************************************************
echo *           Configuracion Completada!                *
echo *  El entorno virtual esta activado y listo para     *
echo *            usar con todas las dependencias.        *
echo **************************************************%RESET%
pause