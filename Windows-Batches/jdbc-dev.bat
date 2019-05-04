REM igv-tomcat
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\log4j.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\GMO-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\NRI-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\NRI-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-tomcat\WEB-INF\classes\META-INF\spring\NRI-jdbc.properties
REM igv-rest
del E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\log4j.properties
del E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\GMO-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\GMO-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\xenos-jdbc.properties
del E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\NRI-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\NRI-jdbc-dev.properties E:\apache-tomcat-7.0.57\webapps\igv-rest\WEB-INF\classes\META-INF\spring\NRI-jdbc.properties
REM igv-console
del E:\igv-console\CONSOLE-INF\classes\log4j.properties
copy "C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\log4j-debug.properties" E:\igv-console\CONSOLE-INF\classes\log4j.properties
del E:\igv-console\CONSOLE-INF\classes\META-INF\spring\GMO-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\GMO-jdbc-dev.properties E:\igv-console\CONSOLE-INF\classes\META-INF\spring\GMO-jdbc.properties
del E:\igv-console\CONSOLE-INF\classes\META-INF\spring\xenos-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\xenos-jdbc-dev.properties E:\igv-console\CONSOLE-INF\classes\META-INF\spring\xenos-jdbc.properties
del E:\igv-console\CONSOLE-INF\classes\META-INF\spring\NRI-jdbc.properties
copy C:\Users\abhisheksa\Desktop\Batch-Files\Exchange-Files\NRI-jdbc-dev.properties E:\igv-console\CONSOLE-INF\classes\META-INF\spring\NRI-jdbc.properties
pause
del E:\apache-tomcat-7.0.57\webapps\igv-tomcat.war
del E:\apache-tomcat-7.0.57\webapps\igv-rest.war
E:\apache-tomcat-7.0.57\bin\startup.bat