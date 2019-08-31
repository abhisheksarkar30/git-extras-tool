@echo off
set JAVA_HOME=C:\Program Files\Java\jdk1.6.0_23
setlocal
REM cd /d %CODEBASE%
if not "%1"=="r" (call build clean install -Dmaven.test.skip -Dall -Ddeployments=gv-aus)
if exist gv-deployments\gv-dist\target\igv-tomcat.war (
del %CATALINA_HOME%\webapps\igv-*.war
rd /s/q %CATALINA_HOME%\webapps\igv-tomcat
rd /s/q %CATALINA_HOME%\webapps\igv-rest
copy gv-deployments\gv-dist\target\igv-*.war %CATALINA_HOME%\webapps
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
)