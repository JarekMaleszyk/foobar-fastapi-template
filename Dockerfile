FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip install -q --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]