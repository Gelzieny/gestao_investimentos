@echo off
REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Sobe o servidor FastAPI com Uvicorn
uvicorn app.main:app --reload --host 127.0.0.1 --port 8080

REM Desativa o ambiente virtual
deactivate