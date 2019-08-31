@echo off
set JAVA_HOME=C:\Program Files\Java\jdk1.6.0_23
setlocal
if not "%1"=="r" (call mvn clean install -Dmaven.test.skip)
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
) else ( echo Destination doesn't exist!)
) else ( echo War file doesn't exist!)