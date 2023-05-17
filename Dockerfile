FROM bitnami/python:3.11.2

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y libpq-dev

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000
