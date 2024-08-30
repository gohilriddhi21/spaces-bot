FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY . .

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

ENV PORT=8080
EXPOSE $PORT

CMD ["sh", "-c", "poetry run functions-framework --target=chat --source=src/app.py --port=${PORT}"]