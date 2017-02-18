@echo off

:: -----------------------------------------------------------------------------
:: this recives path from sublime text and forwards it to pymake.py for building
:: -----------------------------------------------------------------------------

:: {
::     "cmd": ["C:/Users/user/Source/Repo/pymake/run_me.bat", "$file"],
::     "variants": [
:: 		{ 
:: 			"name": "Run",
:: 			"cmd": ["C:/Users/user/Source/Repo/pymake/run_me.bat", "$file", "--alt"]
:: 		}
::     ]
:: }

echo -----------------------------------------------------
echo sublime_build batch script 
:: https://ss64.com/nt/syntax-args.html
echo 	%~f0


:: Check for Python Installation
:: echo checking python installation:
rem python --version 2>NUL
python -c "import sys; print('python version:\n\t{0[0]}.{0[1]}'.format(sys.version_info))"
if errorlevel 1 goto errorNoPython
:: Reaching here means Python is installed.


:: assume pymake.py beside this script
set "pymake=%~dp0pymake.py"


:: check if variant build requested
if "%2"=="--alt" echo variant build (CTRL+SHIFT+B to change build system)


:: print command line argument to be sent to pymake.py (path of current sublime)
echo argument: 
echo 	%1

:: redirect to pymake.py
:: echo redirecting to pymake.py
python %pymake% %1 %2
:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error^: Python not installed
