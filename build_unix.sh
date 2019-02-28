#bin/bash

if [[ "$OSTYPE" == "linux-gnu" ]]; then
        pyinstaller -y --clean --windowed OPEM.spec
elif [[ "$OSTYPE" == "darwin"* ]]; then
        pyinstaller -y --clean --windowed OPEM.spec
	pushd dist
	hdiutil create ./Opem.dmg -srcfolder OPEM -ov
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
