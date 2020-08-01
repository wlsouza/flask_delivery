install:
	pip install -e .["dev"]

clean:
	clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .["dev"] --upgrade --no-cache

init_db:
	FLASK_APP=devlivery/app.py flask create-db
	FLASK_APP=devlivery/app.py flask db upgrade

test:
	SET FLASK_ENV=test pytest  tests/ --cov=devlivery



