init:
	poetry install
start:
	poetry run flask --app app.py run