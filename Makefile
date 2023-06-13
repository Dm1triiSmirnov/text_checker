tests:
	poetry run pytest text_checker/tests.py -vvv

lint:
	poetry run flake8 text_checker

format:
	poetry run black text_checker
	poetry run isort text_checker