@echo off
set /P sw=Enter r:replace with current jar only: 
if not "%sw%"=="r" (call mvn clean install -Dmaven.test.skip)
set /a count=0
FOR %%f in (target\gv-*.jar) do (set /a count=count+1
set fname=%%~nf.jar)
if %count%==1 (
if exist %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib (
del %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib\%fname%
copy target\%fname% %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib
del %CATALINA_HOME%\webapps\igv-rest\WEB-INF\lib\%fname%
copy target\%fname% %CATALINA_HOME%\webapps\igv-rest\WEB-INF\lib
del E:\igv-console\CONSOLE-INF\lib\%fname%
copy target\%fname% E:\igv-console\CONSOLE-INF\lib
pause
if exist %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib\%fname% (
echo %CATALINA_HOME%\bin\startup
echo launch console services? else exit
pause
echo start cmd -new_console /k E:\igv-console\launch ServiceController
echo timeout 5 > NUL
echo start cmd -new_console /k E:\igv-console\launch REF/StartReportRunner
)
) else ( echo Destination doesn't exist!)
) else ( echo War file doesn't exist!)
pause