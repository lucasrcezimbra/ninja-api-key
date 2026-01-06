.DEFAULT_GOAL := build

install: # Install dependencies
	uv sync --all-extras
	pre-commit install
	pre-commit install-hooks

fmt format: # Run code formatters
	isort --profile black .
	black .

test: # Run tests
	uv run pytest --ds=sample_project.settings -v sample_project ninja_apikey/tests

cov test-cov: # Run tests with coverage
	uv run pytest --ds=sample_project.settings --cov=ninja_apikey --cov-report=term-missing --cov-report=xml -v sample_project ninja_apikey/tests

build: # Build project
	make install
	make cov
