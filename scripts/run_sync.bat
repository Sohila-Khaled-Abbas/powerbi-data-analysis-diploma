@echo off
REM ============================================================
REM One-click Sync Runner for Windows
REM ============================================================
cd /d "%~dp0\.."
echo ============================================================
echo Checking YouTube Playlist for new episodes...
echo ============================================================
python scripts\sync_new_episodes.py %*
echo.
echo Sync process finished.
pause

