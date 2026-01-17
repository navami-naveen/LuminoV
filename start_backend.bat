@echo off
echo ========================================
echo LuminaV Backend Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Python found:
python --version
echo.

REM Install dependencies
echo Installing dependencies...
python -m pip install --user --quiet fastapi uvicorn groq python-multipart 2>nul
if errorlevel 1 (
    echo Warning: Some packages may already be installed
)
echo.

REM Start the server
echo Starting backend server on http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

cd /d "%~dp0"
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

pause
