@echo off
set "Service=MSSQLSERVER"
rem Make sure service exists
echo looking for MS SQL Server service: 
echo %Service%
sc query %Service% | (findstr "does not exist" && goto :Done)

for /f "tokens=1,2,3,4" %%A in ('sc query %Service%') do (
echo token %%A
if /I %%A == STATE (

if /i not %%D == RUNNING (
echo(%Service% STATE is %%D.  It should be RUNNING.
rem openfiles requires admin
openfiles >nul 2>&1 || (Color E0 & ECHO(You must run with Administrative priveleges to start the service. & goto :Done)
echo(Starting it now...
sc start %Service%
)
)
)
)

if /i not %%D == RUNNING (
echo(%Service% STATE is %%D.  It should be RUNNING.)
)
:Done
pause