@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYCMD=py -3"
) else (
    set "PYCMD=python"
)
%PYCMD% --version || (echo Install Python 3.11 or newer first. & pause & exit /b 1)
if not exist ".venv\Scripts\python.exe" (
    %PYCMD% -m venv .venv || (pause & exit /b 1)
)
call ".venv\Scripts\activate.bat"
python -m pip install -r requirements.txt || (echo Dependency installation needs internet access. & pause & exit /b 1)
streamlit run app.py --server.address 127.0.0.1
pause
