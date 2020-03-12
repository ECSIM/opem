#!/bin/bash
py_version=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.+)')
echo "Your Python Version : $py_version"
echo "Recommended Python Version : >= 3.5"
echo "-----"
echo "-----"
pip3 install –upgrade pip
pip3 install -r requirements.txt
pip3 install "PyInstaller>=3.3"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        pyinstaller -y --clean --windowed OPEM.spec
elif [[ "$OSTYPE" == "darwin"* ]]; then
        pyinstaller -y --clean --windowed OPEM.spec
	pushd dist
	hdiutil create ./OPEM.dmg -srcfolder OPEM -ov
	popd
elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo "You are usign $OSTYPE, that means you are using windows OS, so please run build_exe.bat instead."
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "You are usign $OSTYPE, that means you are using windows OS, so please run build_exe.bat instead."
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "You are usign $OSTYPE, that means you are using windows OS, so please run build_exe.bat instead."
else
        echo "$OSTYPE is not compatiable. please add an issue for opem."
fi
