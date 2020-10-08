@ECHO OFF
TITLE Python WEB application

SET CURR_DIR=%~dp0
SET PYTHON_EXE=%CURR_DIR%core\python\python.bat
SET APP_MAIN=%CURR_DIR%core\bootstrap.py
SET MYSQL_EXE=%CURR_DIR%core\mysql\start_mysql.bat
SET MYSQL_STOP=%CURR_DIR%core\mysql\stop_mysql.bat

ECHO Starting MySQL service
START "" "%MYSQL_EXE%"

ECHO Starting the application
"%PYTHON_EXE%" "%APP_MAIN%"

ECHO The application stopped.

ECHO Shuting down MySQL service
CALL "%MYSQL_STOP%"

PAUSE & EXIT
