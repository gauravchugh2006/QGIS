REM Runs only the DBKR sample profiles for a quicker targeted check.
@echo off
call .venv\Scripts\activate
python -c "import sys; sys.path.insert(0, 'src'); from dbkr.profile_dbkr_frontend import profile_dbkr_frontend_task; from dbkr.profile_dbkr_backend import profile_dbkr_backend_task; profile_dbkr_frontend_task(); profile_dbkr_backend_task()"
