# PowerShell Sync Runner
Set-Location -Path "$PSScriptRoot\.."
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Checking YouTube Playlist for new episodes..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
python scripts\sync_new_episodes.py $args
