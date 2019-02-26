@echo off
python --version | find /i "Python 3.4" > nul
echo -----
if errorlevel 1 (
	echo Warning : Please use Python 3.4.x
) else (
	echo Python version check done!
)
echo -----
python -m PyInstaller OPEM.spec
pause