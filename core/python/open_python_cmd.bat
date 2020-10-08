@ECHO OFF
TITLE Command prompt (Python 3.7.8)

:: Setting up the environment
CALL "%~dp0set_python_env.bat"

:: Launching Command Prompt in python environment
CLS & ECHO Command prompt for Python environment
CMD.EXE /K CD "%~dp0"
