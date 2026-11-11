@echo off
REM ============================================================
REM One-Click Repository Updater & Publisher for Windows
REM ============================================================
cd /d "%~dp0\.."
echo ============================================================
echo Running Power BI Diploma Repository Updater & Publisher...
echo ============================================================
python scripts\publish_updates.py %*
echo.
echo Process finished.
pause
