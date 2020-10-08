@ECHO OFF
TITLE Shuting down MySQL service

:: Setting up the environment
CALL "%~dp0set_mysql_env.bat"

:: Launching MySQL in portable configuration
"%MYSQL_BASEDIR%bin\mysqladmin.exe" --port=%MYSQL_PORT% --user=%MYSQL_USER% shutdown %*

ECHO MySQL service has been stopped.
PAUSE & EXIT /B
