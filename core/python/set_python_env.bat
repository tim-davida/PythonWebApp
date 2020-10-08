@ECHO OFF
ECHO Configuring environment variables for embeded Python bundle

SET PY_HOME=%~dp0
SET PY_LIBS=%PY_HOME%Lib;%PY_HOME%Lib\site-packages
SET PY_PIP=%PY_HOME%Scripts

SET PATH=%PY_HOME%;%PY_LIBS%;%PY_PIP%;%PATH%
