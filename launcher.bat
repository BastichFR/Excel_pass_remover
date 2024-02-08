@echo off

rem Display information about the program
echo.
echo =========== Excel Password Remover ===========
echo This program is used to remove password from secured excel file.
echo You need to select the files you want to remove protection via a graphical interface.
echo Selected files will be saved under out/ directory and under the same name.
echo ============================================== 
echo.
pause

rem Run the Python script
python solver.py
if errorlevel 1 (
    echo Error: Failed to execute solver.py
    pause
    exit /b 1
)
pause
