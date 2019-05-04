@echo off
set logFile=C:\Users\abhisheksa\Desktop\Batch-Files\logs\autoUpdateBuildProdLog.txt
set branchPath=E:\THAGMO\THAGMO-PROD
echo ---------------------------------------------------------------------------UPDATING----------------------------------------------------------------------- > %logFile%
date /t >> %logFile%
time /t >> %logFile%
pushd %branchPath%\istar-gv\devel\gv-core
cvs update -P -d >> %logFile%
pushd %branchPath%\istar-gv\devel\gv-deployments\gv-th
cvs update -P -d >> %logFile%
pushd %branchPath%\istar-gv\devel\gv-deployments\gv-dist
cvs update -P -d >> %logFile%
time /t >> %logFile%
echo ---------------------------------------------------------------------------BUILDING----------------------------------------------------------------------- >> %logFile%
pushd %branchPath%\istar-gv\devel
"%branchPath%\istar-gv\devel\build" clean install -Dmaven.test.skip -Dall -Drest -Ddeployments=gv-th >> %logFile%
exit