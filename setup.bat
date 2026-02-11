@echo off
echo =======================================
echo   Starting environment setup...
echo =======================================

REM Step 1 Create venv
echo Creating virtual environment...
python -m venv venv

REM Step 2 Activate venv
echo Activating virtual environment...
call venvScriptsactivate

REM Step 3 Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel

REM Step 4 Install requirements
echo Installing dependencies...
pip install -r requirements.txt

echo =======================================
echo Setup complete!
echo Virtual environment is ready.
echo =======================================

pause
