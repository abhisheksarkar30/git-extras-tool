set /P sw=Enter r:replace with current jar only: 
if not "%sw%"=="r" (call mvn clean install -Dmaven.test.skip)
set /a count=0
cd /d %~dp0
FOR %%f in (target\gv-*.jar) do (set /a count=count+1
set fname=%%~nf.jar)
if %count%==1 (
if exist E:\igv-console\CONSOLE-INF\lib (
del E:\igv-console\CONSOLE-INF\lib\%fname%
copy target\%fname% E:\igv-console\CONSOLE-INF\lib
if exist E:\igv-console\CONSOLE-INF\lib\%fname% ( 
start cmd -new_console /k E:\igv-console\launch ServiceController
timeout 5 > NUL
start cmd -new_console /k E:\igv-console\launch REF/StartReportRunner
pause
)
) else ( echo Destination doesn't exist!)
) else ( echo War file doesn't exist!)
pause