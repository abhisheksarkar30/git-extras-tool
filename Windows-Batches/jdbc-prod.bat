REM igv-tomcat
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\GMO-jdbc-prod.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-prod.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
REM igv-console
copy E:\Console.bat E:\igv-console
del E:\igv-console\CONSOLE-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\igv-console\CONSOLE-INF\classes\log4j.properties
del E:\igv-console\CONSOLE-INF\classes\META-INF\spring\GMO-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\GMO-jdbc-prod.properties E:\igv-console\CONSOLE-INF\classes\META-INF\spring\GMO-jdbc.properties
del E:\igv-console\CONSOLE-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-prod.properties E:\igv-console\CONSOLE-INF\classes\META-INF\spring\xenos-jdbc.properties
pause
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat.war
del E:\apache-tomcat-7.0.57\webapps\igv-rest.war
E:\apache-tomcat-7.0.57\bin\startup.bat