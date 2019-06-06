@echo off


setlocal enabledelayedexpansion
SET curdir=%cd%
echo "Switch between the different versions of JAVA present"
echo " "
echo "1 JAVA 6"
echo "2 JAVA 7"
echo "3 JAVA 8"

set a=0
set /p a=
echo %a%

IF %a% == 1 ( 
	echo "Setting JAVA 6 to path..."
	SETX -m JAVA_HOME "C:\Program Files\Java\jdk1.6.0_23"


	echo %JAVA_HOME%
	
	)
IF %a% == 2 ( 
	echo "Setting JAVA 7 to path..."
	SETX -m JAVA_HOME "C:\Program Files\Java\jdk1.7.0_80"


	echo %JAVA_HOME%
	
	)
IF %a% == 3 ( 
	echo "Setting JAVA 8 to path..."
	SETX -m JAVA_HOME "C:\Program Files\Java\jdk1.8.0_45"


	echo %JAVA_HOME%
	
	)


set /p a=