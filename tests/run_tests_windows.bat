@echo off
setlocal
set LOG_DIR=logs
if not exist %LOG_DIR% mkdir %LOG_DIR%

for /f %%I in ('powershell -command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set TIMESTAMP=%%I
set LOG_FILE=%LOG_DIR%\test_results_%TIMESTAMP%.log

echo Executando testes com pytest...
echo Log será salvo em: %LOG_FILE%

pytest -v test_legisweb_client.py > %LOG_FILE%
type %LOG_FILE%
