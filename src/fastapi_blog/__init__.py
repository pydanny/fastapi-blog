from typing import Any

import jinja2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .router import get_blog_router


__version__ = "0.3.0"


def add_blog_to_fastapi(
    app: FastAPI,
    prefix: str | None = "blog",
    jinja2_loader: jinja2.BaseLoader = jinja2.PackageLoader(
        "fastapi_blog", "templates"
    ),
    jinja2_extensions: set[str] = {
        "jinja2_time.TimeExtension",
        "jinja2.ext.debug",
    },
) -> FastAPI:
    env = jinja2.Environment(
        loader=jinja2_loader,
        extensions=list(jinja2_extensions),
    )
    templates = Jinja2Templates(env=env)
    router = get_blog_router(templates=templates)
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}
    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"

    app.include_router(**router_kwargs)
    app.mount(
        "/static", StaticFiles(packages=[("fastapi_blog", "static")]), name="static"
    )
    return app
