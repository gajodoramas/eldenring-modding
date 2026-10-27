@echo off

cd /d "%~dp0"

:: Elden Ring executables
python -m PyInstaller "..\\profiles\\eldenring-enhanced.py" --name "ELDEN RING ENHANCED" --onefile --distpath ".\\" --icon "..\\resources\\icons\\eldenring-enhanced.ico" --noconsole

:: NightReign executables
python -m PyInstaller "..\\profiles\\nightreign-enhanced.py" --name "ELDEN RING NIGHTREIGN ENHANCED" --onefile --distpath ".\\" --icon "..\\resources\\icons\\nightreign-enhanced.ico" --noconsole
