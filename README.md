# FastAPI Blog README

A markdown-powered blog engine and light CMS for FastAPI.

## Planned features

- [ ] Ability to overload templates
- [ ] Ability to overload css
- [ ] Add standalone markdown pages
- [ ] Possible database support
- [ ] Documentation

## Releasing a new version

```
pip install -U build
python -m build
pip install -U twine
python -m twine upload dist/*
git commit -am "Release for vXYZ"
make tag
```