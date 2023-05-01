# 
FROM python:3.10

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]