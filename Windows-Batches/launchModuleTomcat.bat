set /P sw=Enter r:replace with current jar only: 
if not "%sw%"=="r" (call mvn clean install -Dmaven.test.skip)
set /a count=0
cd /d %~dp0
FOR %%f in (target\gv-*.jar) do (set /a count=count+1
set fname=%%~nf.jar)
if %count%==1 (
if exist %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib (
del %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib\%fname%
copy target\%fname% %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib
del %CATALINA_HOME%\webapps\igv-rest\WEB-INF\lib\%fname%
copy target\%fname% %CATALINA_HOME%\webapps\igv-rest\WEB-INF\lib
if exist %CATALINA_HOME%\webapps\igv-tomcat\WEB-INF\lib\%fname% (
%CATALINA_HOME%\bin\startup
pause
)
) else ( echo Destination doesn't exist!)
) else ( echo War file doesn't exist!)
pause