from typing import Any

import jinja2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .main import add_blog_to_fastapi
from .router import get_blog_router


__version__ = "0.6.0"
