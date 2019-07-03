## Installation		

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.5)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 1.1](https://github.com/ecsim/opem/archive/v1.1.zip) or [Latest Source ](https://github.com/ecsim/opem/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install opem` or `pip3 install opem` (Need root access)

### Easy Install

- Run `easy_install --upgrade opem` (Need root access)

### Conda

- Check [Conda Managing Package](https://conda.io)
- `conda install -c ecsim opem` (Need root access)

### GUI

- OPEM GUI is available [here](https://github.com/ECSIM/gopem)			

### Exe Version (Only Windows)
- Download [Exe-Version 1.1](https://github.com/ECSIM/opem/releases/download/v1.1/OPEM-1.1.exe)
- Run `OPEM.exe`


### DMG Version (MacOS)
- Download [DMG-Version 1.1](https://github.com/ECSIM/opem/releases/download/v1.1/OPEM-1.1.dmg)
- Open DMG file
- Copy `OPEM` into your system
- Run `OPEM`

### MATLAB
- Download and install [MATLAB](https://www.mathworks.com/products/matlab.html) (>=8.5, 64/32 bit)
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.5, 64/32 bit) 
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Run `pip install opem` or `pip3 install opem` (Need root access)
- Configure Python interpreter
```matlab
>> pyversion PYTHON_EXECUTABLE_FULL_PATH
```
- Visit [MATLAB Examples](https://github.com/ECSIM/opem/tree/master/MATLAB)			

### Exe Version Note
For OPEM <= 0.5 targeting Windows < 10, the user needs to take special care to include the Visual C++ run-time .dlls: Python 3.5 uses Visual Studio 2015 run-time, which has been renamed into “Universal CRT“ and has become part of Windows 10. For Windows Vista through Windows 8.1 there are Windows update packages, which may or may not be installed in the target-system. So you have the following options:

1. Download OPEM >= 0.6 (Recommended)
2. Download and install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)


### System Requirements
OPEM will likely run on a modern dual core PC. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 2GB of RAM

Note that it may run on lower end equipment though good performance is not guaranteed.