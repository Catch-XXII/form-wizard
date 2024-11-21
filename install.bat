python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip list
SET ENV=YOUR_PATH_TO_PROJECT_WITHOUT_QUOTES
call %ENV%\.venv\Scripts\activate.bat
pytest
