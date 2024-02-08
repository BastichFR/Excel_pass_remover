# Excel Password Remover

## Description
This program is designed to remove passwords from secure Excel files. 
It lets you select the files you wish to unprotect via a graphical interface. 
The selected files will be saved in the "out/" directory under the same name.

## Prerequisites
- Python 3.x must be installed on your system.

## All

### Installation
1. Clone this repository on your local machine.
2. Make sure Python 3.x is installed.
3. Run `python3.x solver.py` to launch the application.

### Usage
1. Run the `python3.x solver.py` command in the project root directory.
2. Select the Excel files you wish to unprotect.
3. The selected files will be saved in the "out/" directory under the same unprotected name.

## Under Linux

### Installation
1. Clone this repository on your local machine.
2. Make sure Python 3.x is installed.
3. Run `make` to check that Python is installed and to launch the application.

### Usage
1. Run the `make` command in the project root directory.
2. Select the Excel files you wish to unprotect.
3. The selected files will be saved in the "out/" directory under the same unprotected name.

## Under Windows

### Installation
1. Clone this repository on your local machine.
2. Make sure Python 3.x is installed.
3. Start `launcher.bat` to launch the application.

### Usage
1. Run `launcher.bat` to launch the application.
2. Select the Excel files you wish to unprotect.
3. The selected files will be saved in the "out/" directory under the same unprotected name.

## Project structure
- `solver.py`     : Main script which manages the de-protection of Excel files.
- `src/`          : Directory containing the Python modules used by the main script.
- `out/`          : Directory where unprotected Excel files will be saved.
- `Makefile`      : **<LINUX>**   Make  file to automate verification of Python installation and application execution.
- `launcher.bat`  : **<WINDOWS>** Batsh file to automate verification of Python installation and application execution.
- `README.md`     : This file.

## Author
[BastichFR](https://github.com/BastichFR/)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
