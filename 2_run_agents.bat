@echo off
cd /d "%~dp0"

echo ===================================================
echo   PORTABLE ENVIRONMENT CHECK
echo ===================================================

:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed on this computer!
    echo Please install Python from python.org before running your agents.
    pause
    exit
)

:: 2. Check and force install ALL required dependencies to this active Python instance
echo Checking for required AI framework and UI dependencies...
python -c "import crewai, langchain_openai, streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo [ALERT] Required libraries are missing on this Python instance.
    echo Installing crewai[tools], langchain-openai, and streamlit now...
    python -m pip install --upgrade pip
    python -m pip install crewai[tools] langchain-openai streamlit
    echo Dependencies successfully installed!
    echo ---------------------------------------------------
) else (
    echo [OK] Framework and UI dependencies already installed.
)

:: 3. Wait for the llamafile model server to be fully ready
echo Waiting 5 seconds for your Local AI Server to finish loading...
timeout /t 5

:: 4. Kick off your manager script via the module wrapper
echo Launching your Multi-Agent Management Crew browser app...
python -m streamlit run usb_agent_manager.py
pause
