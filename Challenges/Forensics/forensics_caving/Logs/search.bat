@echo off
setlocal

REM Define the path to the folder containing your .evtx files
set evtxPath="D:\Users\curtismechling\Documents\CTFs\Hack The Box\Business CTF 2024\Forensics\forensics_caving\Logs"

REM Get a list of all .evtx files in the specified folder
for %%F in (%evtxPath%\*.evtx) do (
    echo Searching in file: %%F
    LogParser "SELECT * FROM %%F WHERE Message LIKE '%HTB%'" -i:evt -o:CSV
)

endlocal
