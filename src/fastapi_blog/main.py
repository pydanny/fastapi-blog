from typing import Any

import jinja2
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from .router import get_blog_router


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
    favorite_post_ids: set[str] = set(),
    posts_directory: str = "posts",
    pages_directory: str = "pages",
    mount_statics: bool = True,
) -> FastAPI:
    # Prep the templates
    env = jinja2.Environment(
        loader=jinja2_loader,
        extensions=list(jinja2_extensions),
    )
    templates = Jinja2Templates(env=env)

    # Router controls
    router = get_blog_router(
        templates=templates,
        favorite_post_ids=favorite_post_ids,
        posts_directory=posts_directory,
        pages_directory=pages_directory,
    )
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}
    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"
    app.include_router(**router_kwargs)

    return app
