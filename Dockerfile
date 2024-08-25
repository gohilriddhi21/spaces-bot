FROM python:3.11-slim-buster

WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY src/app.py /app.py

CMD ["python", "/app.py"]