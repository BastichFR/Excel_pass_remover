all: info check_python run

run:
	@python3 solver.py

info:
	@echo ""
	@echo " =========== Excel Password Remover =========== "
	@echo " This program is used to remove password from secured excel file."
	@echo " You need to select the files you want to remove protection via a graphical interface."
	@echo " Selected files will be saves under out/ directory and under the same name."
	@echo " ============================================== "

check_python:
	@python3 --version >/dev/null 2>&1 || { echo >&2 "Python is not installed !"; exit 1; }
	@echo " Python is installed."
	@echo " ============================================== "
	
.PHONY: run info check_python
