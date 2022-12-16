install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

run:
	poetry run gendiff 'tests/fixtures/json/file3.json' 'tests/fixtures/json/file4.json'

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vvvvv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build