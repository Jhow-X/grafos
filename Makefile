all: run

run:
	python3 main.py

save:
	pip freeze > requirements.txt

import:
	pip install -r requirements.txt