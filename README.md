# FastAPI Blog README

A markdown-powered blog engine and light CMS for FastAPI.

## Releasing a new version

```
pip install -U build
python -m build
pip install -U twine
python -m twine upload dist/*
git commit -am "Release for vXYZ"
make tag
```
