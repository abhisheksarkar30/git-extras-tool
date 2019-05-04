@echo off
pushd %GIT_IGV_THAI%
set branch1=PSMS-REL-7
set branch2=PSMS-REL-8

echo Branch1-process
set branch=%branch1%
set destination=C:\Users\abhisheksa\Desktop\Batch-Files\builds
git checkout %branch% > %destination%\%branch%.txt
for /f "tokens=2" %%I in ('git.exe branch 2^> NUL ^| findstr /b "* "') do set GITBRANCH=%%I
if %GITBRANCH%==%branch% (
git pull >> %destination%\%branch%.txt
call build clean install -Dmaven.test.skip -Dall -Drest -Ddeployments=gv-th >> %destination%\%branch%.txt
if exist gv-deployments\gv-dist\target\igv-tomcat.war (
rd /s/q %destination%\%branch%
md %destination%\%branch%
copy gv-deployments\gv-dist\target\igv-* %destination%\%branch%
)
)

echo Branch2-process
set branch=%branch2%
set destination=C:\Users\abhisheksa\Desktop\Batch-Files\builds
git checkout %branch% > %destination%\%branch%.txt
for /f "tokens=2" %%I in ('git.exe branch 2^> NUL ^| findstr /b "* "') do set GITBRANCH=%%I
if %GITBRANCH%==%branch% (
git pull >> %destination%\%branch%.txt
call build clean install -Dmaven.test.skip -Dall -Drest -Ddeployments=gv-th >> %destination%\%branch%.txt
if exist gv-deployments\gv-dist\target\igv-tomcat.war (
rd /s/q %destination%\%branch%
md %destination%\%branch%
copy gv-deployments\gv-dist\target\igv-* %destination%\%branch%
)
)