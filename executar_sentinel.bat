@echo off
title SENTINEL - Global Solution FIAP

echo ==========================================
echo        INICIANDO SENTINEL
echo ==========================================

REM Cria a venv se ela ainda nao existir
if not exist ".venv" (
    echo Criando ambiente virtual...
    python -m venv .venv
)

REM Ativa a venv
call .venv\Scripts\activate

REM Atualiza pip
echo Atualizando pip...
python -m pip install --upgrade pip

REM Instala dependencias
echo Instalando dependencias...
python -m pip install -r requirements.txt

REM Executa o sistema
echo Iniciando sistema...
python src\sistema.py

pause