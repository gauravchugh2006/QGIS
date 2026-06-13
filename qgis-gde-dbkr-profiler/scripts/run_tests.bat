REM Runs the automated tests so changes can be checked before profiling runs.
@echo off
call .venv\Scripts\activate
pytest
