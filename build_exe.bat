@echo off
python --version | find /i "Python 3.4" > nul
echo -----
if errorlevel 1 (
	echo Warning : Please use Python 3.4.x
) else (
	echo Python version check done!
)
echo -----
python -m pip install –upgrade pip
python -m pip install -r requirements.txt
python -m pip install "PyInstaller>=3.3"
python -m PyInstaller OPEM.spec
pause