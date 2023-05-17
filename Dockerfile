FROM bitnami/python:3.11.2

WORKDIR /app

COPY . .

RUN set -eux; \
    python -m pip install --upgrade pip; \
    python -m pip install -r requirements.txt 

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
