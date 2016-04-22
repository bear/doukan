
help:
	@echo "  dev         install all dev dependencies (virtualenv is assumed)"
	@echo "  clean       remove unwanted stuff"
	@echo "  lint        check style with flake8"
	@echo "  test        run tests"
	@echo "  coverage    run tests with code coverage"

dev:
	pip install -r requirements-test.txt
	pip install --editable .

info:
	python --version
	pyenv --version
	pip --version

clean:
	python setup.py clean

lint:
	flake8 doukan > violations.flake8.txt

test: lint
	python setup.py test

coverage: clean
	coverage run --source=doukan setup.py test --addopts "--ignore=venv"
	coverage html
	coverage report

check: clean lint
	check-manifest
	python setup.py check

build: check
	python setup.py sdist
	python setup.py bdist_wheel

upload: check
	python setup.py sdist upload
	python setup.py bdist_wheel upload
