set JAVA_HOME=C:\Program Files\Java\jdk1.6.0_23
setlocal
cd /d %CODEBASE%
set /P sw=Enter r:replace with current war only: 
if not "%sw%"=="r" (call build clean install -Dmaven.test.skip -Dall -Ddeployments=gv-aus)
if exist gv-deployments\gv-dist\target\igv-tomcat.war (
del %CATALINA_HOME%\webapps\igv-*.war
rd /s/q %CATALINA_HOME%\webapps\igv-tomcat
rd /s/q %CATALINA_HOME%\webapps\igv-rest
copy gv-deployments\gv-dist\target\igv-tomcat.war %CATALINA_HOME%\webapps
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\OPM-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\OPM-jdbc-csp.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\OPM-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-csp.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
pause
)
if exist %CATALINA_HOME%\webapps\igv-tomcat.war (
%CATALINA_HOME%\bin\startup
)
pause