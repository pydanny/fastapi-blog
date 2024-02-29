# FastAPI Blog

A simple, easy-to-use blog application built with FastAPI.

## Features

- Write blog posts in Markdown
- Syntax highlighting for code blocks
- Responsive design
- Dark mode
- Overloadable templates
- [Live, working configuration examples](https://github.com/pydanny/fastapi-blog/tree/main/tests/examples)
- RSS feed
- SEO-friendly
- Sitemap
- Docker support

## Basic Usage

1. Import the `add_blog_to_fastapi` function
2. Run the instantiated FastAPI app throught the `add_blog_to_fastapi` function

This all you need to do:

```python
from fastapi_blog import add_blog_to_fastapi
from fastapi import FastAPI


app = FastAPI()
app = add_blog_to_fastapi(app)


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/blog",
    }
```

## Advanced Usage

fastapi_blog is configurable through the `add_blog_to_fastapi` function.

### Replacing the default templates

This example is Django-like in that your local templates will overload the default ones.

```python
import fastapi_blog
import jinja2
from fastapi import FastAPI


django_style_jinja2_loader = jinja2.ChoiceLoader(
    [
        jinja2.FileSystemLoader("templates"),
        jinja2.PackageLoader("fastapi_blog", "templates"),
    ]
)

app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(
    app, prefix=prefix, jinja2_loader=django_style_jinja2_loader
)


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": f"http://localhost:8000/blog",
    }
```


### Changing the location of the blog url

Perhaps you want to have the blog at the root?

```python
import fastapi_blog
from fastapi import FastAPI


app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(
    app, prefix="change"
)


@app.get("/api")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/change",
    }
```


## Installation and Running Example Sites

### Option 1: Local Virtualenv

You can install this into a virtualenv using the pyproject.toml file:

```bash
pip install fastapi-blog
make run
```

### Option 2: Docker (Local Dockerfile)

Or into a Docker container using the local Dockerfile:

```bash
docker build -t fastapi-blog .
docker run -d -p 8000:8000 fastapi-blog
```

### Option 3: Docker (Prebuilt)

Or using a prebuilt Docker image from GitHub Container Registry:

```bash
docker run -d -p 8000:8000 ghcr.io/aroygreenfeld/fastapi-blog:latest
```

This is if you just want to run the application without building it yourself.

## Releasing a new version

1. Update the version in `pyproject.toml` and `fastapi_blog/__init__.py`

2. Build the distribution locally:

```bash
pip install -U build
python -m build
```

3. Upload the distribution to PyPI:

```bash
pip install -U twine
python -m twine upload dist/*
```

4. Create a new release on GitHub and tag the release:

```bash
git commit -am "Release for vXYZ"
make tag
```
