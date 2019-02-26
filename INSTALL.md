## Installation		

### Source Code
- Download [Python3.x](https://www.python.org/downloads/) (>=3.4)
- Download [Version 1.0](https://github.com/ecsim/opem/archive/v1.0.zip) or [Latest Source ](https://github.com/ecsim/opem/archive/master.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install opem` or `pip3 install opem` (Need root access)

### Easy Install

- Run `easy_install --upgrade opem` (Need root access)


### Exe Version (Only Windows)
- Download [Exe-Version 1.0](https://github.com/ECSIM/opem/releases/download/v1.0/OPEM-1.0.exe)
- Extract Zip file
- Run `OPEM.exe`


### DMG Version (MacOS)
- Download [DMG-Version 1.0](https://github.com/ECSIM/opem/releases/download/v1.0/OPEM-1.0.dmg)
- Open DMG file
- Copy `OPEM` into your system
- Run `OPEM`


### Exe Version Note
For OPEM <= 0.5 targeting Windows < 10, the user needs to take special care to include the Visual C++ run-time .dlls: Python 3.5 uses Visual Studio 2015 run-time, which has been renamed into “Universal CRT“ and has become part of Windows 10. For Windows Vista through Windows 8.1 there are Windows update packages, which may or may not be installed in the target-system. So you have the following options:

1. Download OPEM >= 0.6 (Recommended)
2. Download and install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)


### System Requirements
OPEM will likely run on a modern dual core PC. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 2GB of RAM

Note that it may run on lower end equipment though good performance is not guaranteed.