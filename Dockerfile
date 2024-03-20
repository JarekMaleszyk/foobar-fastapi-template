#https://hub.docker.com/_/python
FROM python:3
ENV SECRET_KEY=dsj7x2odxqctpdclfx28f2zfix2hi8tqdce7qfaqepdclfx287fp7th5btpdclfx28 \
    ALGORITHM=HS256 \
    ACCESS_TOKEN_EXPIRE_MINUTES=30
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]