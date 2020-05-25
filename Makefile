init:
	pip install -r requirements.txt

test:
	py.test tests

lint:
	flake8 etlutils tests

update:
	pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

requirements:
	pip freeze --exclude-editable > requirements.txt

build:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	name '*~' -exec rm -f  {}

.PHONY: init test update requirements clean lint build
