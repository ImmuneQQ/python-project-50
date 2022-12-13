install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

run:
	poetry run gendiff 'json/file1.json' 'json/file2.json'

lint:
	poetry run flake8 gendiff