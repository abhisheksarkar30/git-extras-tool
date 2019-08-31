@echo off
REM igv-tomcat
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\%1 E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\*
REM igv-console
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\igv-console\CONSOLE-INF\classes\log4j.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\%1 E:\igv-console\CONSOLE-INF\classes\META-INF\spring\*
del E:\apache-tomcat-7.0.57\webapps\igv-*.war