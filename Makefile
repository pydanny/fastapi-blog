

VERSION=v$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

tag:
	echo "Tagging version $(VERSION)"
	git tag -a $(VERSION) -m "Creating version $(VERSION)"
	git push origin $(VERSION)

install:
	pip install uv
	uv pip install -e '.[dev]'

all:
	make lint
	make mypy
	make test

lint:
	ruff check .
	ruff format . --check

format:
	ruff check . --fix
	ruff format .

mypy:
	mypy .

test:
	coverage run -m pytest .
	coverage report -m
	coverage html

test-pdb:
	pytest --pdb .

run:
	make run_defaults

run_defaults:
	cd tests/examples && uvicorn defaults:app --reload	

run_modified_all:
	cd tests/examples && uvicorn modified_all:app --reload	

run_prefix_change:
	cd tests/examples && uvicorn prefix_change:app --reload		

run_prefix_none:
	cd tests/examples && uvicorn prefix_none:app --reload

run_favorite_post_ids:
	cd tests/examples && uvicorn favorite_post_ids:app --reload