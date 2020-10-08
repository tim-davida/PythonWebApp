@ECHO OFF
TITLE Python 3.7.8

:: Setting up the environment
CALL "%~dp0set_python_env.bat"

:: Launching Python program in configured environment
"%PY_HOME%python.exe" %*

ECHO Python stopped.
PAUSE & EXIT
