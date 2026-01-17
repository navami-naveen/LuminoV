# ========================================
# Groq API Key Setup for Windows
# ========================================
# 
# INSTRUCTIONS:
# 1. Replace YOUR_API_KEY_HERE with your actual Groq API key
# 2. Save this file
# 3. Run it in PowerShell with: .\setup_api_key.ps1
#
# To get your API key: https://console.groq.com
# ========================================

# YOUR API KEY - PASTE IT HERE:
$GROQ_API_KEY = "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"

# ========================================
# Set as persistent environment variable
# ========================================

if ($GROQ_API_KEY -eq "YOUR_API_KEY_HERE") {
    Write-Host "⚠️  ERROR: You must replace 'YOUR_API_KEY_HERE' with your actual Groq API key!" -ForegroundColor Red
    Write-Host "1. Get your key from: https://console.groq.com" -ForegroundColor Yellow
    Write-Host "2. Edit this file and paste your key in the `$GROQ_API_KEY line" -ForegroundColor Yellow
    Write-Host "3. Save and run this script again" -ForegroundColor Yellow
    exit
}

# Set for current session
[Environment]::SetEnvironmentVariable("GROQ_API_KEY", $GROQ_API_KEY, "User")

Write-Host "✅ Success! Your Groq API key has been set." -ForegroundColor Green
Write-Host "   Variable: GROQ_API_KEY" -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "You can now run: python TimeTravel_CareerAdvisor.py" -ForegroundColor Green
Write-Host "" -ForegroundColor Green
Write-Host "Note: You may need to restart your terminal/PowerShell for changes to take effect." -ForegroundColor Yellow
