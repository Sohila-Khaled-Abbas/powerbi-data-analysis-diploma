# PowerShell Repository Updater & Publisher
Set-Location -Path "$PSScriptRoot\.."
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Running Power BI Diploma Repository Updater & Publisher..." -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
python scripts\publish_updates.py $args
