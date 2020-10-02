@echo off
color 0c
mode 20,20

echo Are you sure you want to enter the matrix? (Y/N)
set/p "cho=>"
if %cho%==y goto :a
if %cho%==Y goto :a
if %cho%==n goto :END
if %cho%==N goto :END
:a
color 47
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
ping > nul
ping > nul
ping > nul

goto a  


:END
