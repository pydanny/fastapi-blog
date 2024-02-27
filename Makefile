

VERSION=v$(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)

tag:
	echo "Tagging version $(VERSION)"
	git tag -a $(VERSION) -m "Creating version $(VERSION)"
	git push origin $(VERSION)


ci:
	make ruff
	make mypy
	make test

ruff:
	ruff check . --fix
	ruff format .

mypy:
	mypy .

test:
	coverage run -m pytest .
	coverage report -m
	coverage html


install:
	pip install -e '.[dev]'
