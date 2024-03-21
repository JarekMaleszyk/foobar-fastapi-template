FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#WORKDIR /usr/src/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]