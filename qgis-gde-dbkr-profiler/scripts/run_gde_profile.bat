REM Runs only the GDE sample profiles for a quicker targeted check.
@echo off
call .venv\Scripts\activate
python -c "import sys; sys.path.insert(0, 'src'); from gde.profile_gde_frontend import profile_gde_frontend_task; from gde.profile_gde_backend import profile_gde_backend_task; profile_gde_frontend_task(); profile_gde_backend_task()"
