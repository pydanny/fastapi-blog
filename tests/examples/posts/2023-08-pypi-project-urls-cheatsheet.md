---
date: "2023-08-04T15:45:00.00Z"
published: true
slug: 2023-08-pypi-project-urls-cheatsheet
tags:
  - howto
  - python
  - cheatsheet  
  - packaging
  - TIL
time_to_read: 2
title: PyPI Project URLs Cheatsheet
description: The PyPI project URLs spec is defined only in code. Here's my cheatsheet explaining how to configure them. I'll update this as I learn more (suggestions welcome!). Examples in several formats.
type: post
image: /logos/til-1.png
twitter_image: /logos/til-1.png
---

See these links in the image below? I want every PyPI project to have them in the left column.

![PyPI project URLs](/images/pypi-links-sidenav.png)

The challenge is the PyPI project URLs spec is [defined only in code](https://github.com/pypi/warehouse/blob/70eac9796fa1eae24741525688a112586eab9010/warehouse/templates/packaging/detail.html#L20-L62). Here's my cheatsheet explaining how to configure them. I'll update this as I learn more (suggestions welcome!). Examples in several formats.

# Example for pyproject.toml

The `[project.urls]` table shown below only works if there is a `[project]` table.


```toml
[project.urls]

# Project homepage, often a link to GitHub or GitLab
# Often specified in the [project] table
homepage = "https://example.com"

# The source code repository, don't use this if your homepage
# is the repo
repository = "https://github.com/me/spam.git"

# The changelog, really useful for ongoing users of your project
changelog = "https://github.com/me/spam/blob/master/CHANGELOG.md"

# Any long form docs
docs = "https://readthedocs.org"
documentation = "https://readthedocs.org"

# Bugs/issues/feature requests
bugs = "https://change/requests"
issues = "https://change/requests"
tracker = "https://change/requests"

# Really only useful if you have a binary download
download = "https://pypi.org/project/spam/#files"

# Funding requests, which hopefully you will get more than pizza money
sponsor = "https://please/give/me/money"
funding = "https://please/give/me/money"
donate = "https://please/give/me/money"

# Discussion areas
mastodon = "https://mastodon/server/@me"
twitter = "https://twitter/or/x"
slack = "https://server/on/slack"
reddit = "https://reddit/r/area"
discord = "https://discord/area"
gitter = "https://gitter/area"
```

# Example for poetry project

Poetry has its own location for `urls` in the [tool.poetry.urls] table. Per the [Poetry documentation on urls](https://python-poetry.org/docs/pyproject/#urls):

> "In addition to the basic urls (homepage, repository and documentation), you can specify any custom url in the urls section."

```toml
[tool.poetry.urls]

changelog = "https://github.com/mygithubusername/projectname/releases"
documentation = "https://mygithubusername.github.io/projectname/"
issues = "https://github.com/mygithubusername/projectname/issues"
```

# Example for setup.py

For legacy reasons, here's the same thing in `setup.py` format.

```python
# setup.py
from setuptools import setup

VERSION = "4.0.0"

setup(
    name="xocto",
    version=VERSION,
    url="https://github.com/octoenergy/xocto"
    # ...
    project_urls={
        "Documentation": "https://xocto.readthedocs.io",
        "Changelog": "https://github.com/octoenergy/xocto/blob/main/CHANGELOG.md",
        "Issues": "https://github.com/octoenergy/xocto/issues",
    },
)
```

# See also

As other resources from other people turn up, I'll add them here.

- [Patrick Arminio's PyPI project URLs demo](https://github.com/patrick91/links-demo) - Added August 7, 2023
