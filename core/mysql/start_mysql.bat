@ECHO OFF
TITLE MySQL portable

:: Setting up the environment
CALL "%~dp0set_mysql_env.bat"

:: MySQL launch options
SET _ARGS=        --datadir="%MYSQL_DATADIR%"
SET _ARGS=%_ARGS% --sql-mode=%MYSQL_MODE%
SET _ARGS=%_ARGS% --lower-case-table-names=2
SET _ARGS=%_ARGS% --port=%MYSQL_PORT%
SET _ARGS=%_ARGS% --user=%MYSQL_USER%
SET _ARGS=%_ARGS% --console

:: Launching MySQL in portable configuration
"%MYSQL_BASEDIR%bin\mysqld.exe" %_ARGS% %*

ECHO MySQL stopped.
PAUSE & EXIT
