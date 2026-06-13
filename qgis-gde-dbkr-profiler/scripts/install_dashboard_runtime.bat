REM Installs the optional PyQt5 runtime needed for the standalone dashboard demo.
@echo off
call .venv\Scripts\activate
pip install -r requirements-dashboard.txt
