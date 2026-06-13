REM Sets up the local Python environment so a new developer can run the toolkit.
@echo off
python -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
