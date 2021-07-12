install:
	pip install -e .['dev']

init_db:
	FLASK_APP=flask_wallet/app.py flask create-db
	FLASK_APP=flask_wallet/app.py flask db upgrade