init:
	pip install -r requirements.txt

test:
	py.test tests

update:
	pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

requirements:
	pip freeze --exclude-editable > requirements.txt

.PHONY: init test update requirements