from typing import Any

import jinja2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
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
    mount_statics: bool = True,
) -> FastAPI:
    # Prep the templates
    env = jinja2.Environment(
        loader=jinja2_loader,
        extensions=list(jinja2_extensions),
    )
    templates = Jinja2Templates(env=env)

    # Router controls
    router = get_blog_router(templates=templates, favorite_post_ids=favorite_post_ids)
    router_kwargs: dict[str, Any] = {"router": router, "tags": ["blog"]}
    if prefix is not None:
        router_kwargs["prefix"] = f"/{prefix}"
    app.include_router(**router_kwargs)

    # Statics controls
    if mount_statics is True:
        app.mount(
            path="/static",
            app=StaticFiles(
                directory="static",
                packages=[("fastapi_blog", "static")],
                check_dir=False,
            ),
            name="static",
        )
    return app
