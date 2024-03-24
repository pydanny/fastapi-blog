# FastAPI Blog

A simple, easy-to-use blog application built with FastAPI.

## Features

- Write blog posts in Markdown
- Syntax highlighting for code blocks
- Responsive design
- Dark mode
- Overloadable templates
- [Live, working configuration examples](https://github.com/pydanny/fastapi-blog/tree/main/tests/examples)
- SEO-friendly
- Sitemap
- Docker support

## Basic Usage

1. Import the `add_blog_to_fastapi` function
2. Run the instantiated FastAPI app through the `add_blog_to_fastapi` function

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

3. Add the first blog entry

Assuming your FastAPI app is defined in a `main.py` module at the root of your project, create a file at `posts/first-blog-post.md`:

```markdown
---
date: "2024-03-21T22:20:50.52Z"
published: true
tags:
  - fastapi
  - fastapi-blog
title: First blog post
description: This is the first blog post entry.
---

Exciting times in the world of fastapi-blog are ahead!

## This is a markdown header

And this is a markdown paragraph with a [link](https://github.com/pydanny/fastapi-blog).
```

4. Add the first page

Assuming your FastAPI app is defined in a `main.py` module at the root of your project, create a file at `pages/about.md`:

```markdown
---
title: "About Me"
description: "A little bit of background about me"
author: "Daniel Roy Greenfeld"
---

[TOC]

## Intro about me

I'm probably best known as "[pydanny](https://www.google.com/search?q=pydanny)", one of the authors of Two Scoops of Django.

I love to hang out with my [wife](https://audrey.feldroy.com/), play with my [daughter](/tags/uma), do [Brazilian Jiu-Jitsu](https://academyofbrazilianjiujitsu.com/), write [books](/books), and read books.

- [Mastodon](https://fosstodon.org/@danielfeldroy)
- [LinkedIn](https://www.linkedin.com/in/danielfeldroy/)
- [Twitter](https://twitter.com/pydanny)

## About this site

This site is written in:

- Python
- FastAPI
- fastapi-blog
- Sakura minimal CSS framework
- Markdown
- Vanilla HTML
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

## Blog at root URL

This is for when your blog/CMS needs to be at the root of the project

```python
import fastapi_blog
from fastapi import FastAPI


app = FastAPI()


@app.get("/api")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000",
    }

# Because the prefix is None, the call to add_blog_to_fastapi
# needs to happen after the other view functions are defined.
app = fastapi_blog.add_blog_to_fastapi(app, prefix=None)
```


## Add favorite articles to the homepage

```python
import fastapi_blog
from fastapi import FastAPI


favorite_post_ids = {
    "code-code-code",
    "thirty-minute-rule",
    "2023-11-three-years-at-kraken-tech",
}

app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app, favorite_post_ids=favorite_post_ids)


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/blog",
    }
```

### Add page not in the blog list of posts

In the `pages` directory of your blog, add markdown files with frontmatter. You can then find it by going to the URL with that name. For example, adding this `pages/about.md` to the default config would make this appear at http://localhost:8000/blog/about.

```markdown
---
title: "About Daniel Roy Greenfeld"
description: "A little bit of background about Daniel Roy Greenfeld"
author: "Daniel Roy Greenfeld"
---

I'm probably best known as "[pydanny](https://www.google.com/search?q=pydanny)", one of the authors of [Two Scoops of Django](/books/tech).
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

2. Update changelog.md

3. Build the distribution locally:

```bash
rm -rf dist
pip install -U build
python -m build
```

4. Upload the distribution to PyPI:

```bash
pip install -U twine
python -m twine upload dist/*
```

5. Create a new release on GitHub and tag the release:

```bash
git commit -am "Release for vXYZ"
make tag
```

## Contributors

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/pydanny">
            <img src="https://avatars.githubusercontent.com/u/62857?v=4" width="100;" alt="pydanny"/>
            <br />
            <sub><b>Daniel Roy Greenfeld</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/audreyfeldroy">
            <img src="https://avatars.githubusercontent.com/u/74739?v=4" width="100;" alt="audreyfeldroy"/>
            <br />
            <sub><b>Audrey Roy Greenfeld</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->
