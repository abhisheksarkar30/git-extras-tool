if exist E:\igv-console (
start cmd -new_console /k E:\igv-console\launch ServiceController
timeout 5 > NUL
start cmd -new_console /k E:\igv-console\launch REF/StartReportRunner
)
pause