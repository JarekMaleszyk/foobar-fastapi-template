## pip
pip freeze > requirements.tx
pip install -f .\requirements.txt
pip install -r requirements.txt --upgrade


## uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


