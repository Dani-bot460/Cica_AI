@echo off
title Cica AI Launcher

echo ==========================
echo Cica AI INDUL
echo ==========================
echo.

REM Projekt mappa
cd /d "C:\Users\dorma\Downloads\Cica_AI_Tiny"

echo Python csomagok ellenorzese...
echo.

pip install requests >nul 2>&1
pip install numpy >nul 2>&1
pip install pillow >nul 2>&1
pip install opencv-python >nul 2>&1
pip install customtkinter >nul 2>&1

echo.
echo Cica AI inditasa...
echo.

python main.py

echo.
echo ==========================
echo A program leallt
echo ==========================
pause