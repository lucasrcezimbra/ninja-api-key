.DEFAULT_GOAL := build

install: # Install dependencies
	flit install --deps develop --symlink

fmt format: # Run code formatters
	isort --profile black .
	black .

test: # Run tests
	pytest --ds=sample_project.settings -v sample_project ninja_apikey/tests.py

cov test-cov: # Run tests with coverage
	pytest --ds=sample_project.settings --cov=ninja_apikey --cov-report=term-missing --cov-report=xml -v sample_project ninja_apikey/tests.py

build: # Build project
	make install
	make cov
