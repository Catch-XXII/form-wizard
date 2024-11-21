python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip list
SET ENV=C:\Users\cuneyd.kaya\dev\WebUIAutomation
call %ENV%\.venv\Scripts\activate.bat
pytest
