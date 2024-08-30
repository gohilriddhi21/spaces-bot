start-hello:
	poetry run functions-framework --target=hello --source=src/app.py --port=8080

start-bot:
	poetry run functions-framework --target=chat --source=src/app.py --port=8080