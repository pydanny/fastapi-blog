---
date: "2023-01-19T22:20:50.52Z"
published: true
tags:
  - octopus
  - kraken
  - python
  - django
  - howto
time_to_read: 10
title: Configuring Sphinx Auto-Doc with projects having Django dependencies
description: How to make it so projects with Django as a dependency benefit from Sphinx's auto-documentation features.
image: /images/cute-octo-plushie-200x200.png
twitter_image: /images/cute-octo-plushie-200x200.png
og_url: https://daniel.feldroy.com/posts/2023-01-configuring-sphinx-auto-doc-with-django
---

How to make it so projects with Django as a dependency benefit from Sphinx's auto-documentation features.

# The Problem

I want to be able to document open source packages with Sphinx (ex. [xocto](https://github.com/octoenergy/xocto)) and have Sphinx automatically document the Django helpers. This isn't quite the same as documenting a Django project, so I wasn't sure if the otherwise awesome [sphinxcontrib-django](https://sphinxcontrib-django.readthedocs.io/) would be the right tool. Fortunately, there's a solution that doesn't require any additional packages.

# The Solution

## Configuration

First, in the Sphinx docs folder, create a file called `django_settings.py` and add the following:

```python
"""
Minimal file so Sphinx can work with Django for autodocumenting.

Location: /docs/django_settings.py
"""

# INSTALLED_APPS with these apps is necessary for Sphinx to build
# without warnings & errors
# Depending on your package, the list of apps may be different
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
]
```

Next, at the top of Sphinx's `conf.py`, add the following:

```python
# docs/conf.py
import os
import sys

import django

# Note: You may need to change the path to match
# your project's structure
sys.path.insert(0, os.path.abspath(".."))  # For discovery of Python modules
sys.path.insert(0, os.path.abspath("."))  # For finding the django_settings.py file

# This tells Django where to find the settings file
os.environ["DJANGO_SETTINGS_MODULE"] = "django_settings"
# This activates Django and makes it possible for Sphinx to
# autodoc your project
django.setup()
```

## Usage

In one of your documentation files, perhaps `docs/localtime.rst`:

```plaintext

.. automodule:: xocto.localtime
   :members:
   :undoc-members:
   :show-inheritance:
```

Or if you are using [myst-parser](https://myst-parser.readthedocs.io/) to use Markdown with Sphinx. In this case, the file would be at `docs/localtime.md`:

````markdown
```{eval-rst}
.. automodule:: xocto.localtime
  :members:
  :undoc-members:
  :show-inheritance:
```
````

# Come and work with me

My employer is hiring! We've got dozens of roles and hundreds of positions open across multiple fields in several countries (USA, UK, Germany, France, Australia, Japan, Italy, Spain, and more). Our mission is to address climate change through decarbonization, electrification, and being good citizens. We're a growing group of companies with a big mission, and we're looking for people who want to make a difference. Check out our [careers page](https://octopus.energy/careers/) to see if what we do excites you and our [open roles page](https://octopus.energy/careers/join-us/) to discover if there's a role that you find interesting.

[![](/images/cute-octo-plushie-200x200.png)](https://octopus.energy/careers/)
