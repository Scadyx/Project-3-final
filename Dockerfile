FROM python:3.10-slim-bullseye

RUN pip install --no-cache-dir --upgrade pip==22.3.1

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev
COPY sql_app ./sql_app
COPY sql_app/data ./data
COPY sql_app/app.py ./
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080

ENTRYPOINT ["/bin/sh", "-c" , "uvicorn app:app --host 0.0.0.0 --port 8080"]