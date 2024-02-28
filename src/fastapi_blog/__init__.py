import jinja2
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .router import get_blog_router


def add_blog_to_fastapi(
    app: FastAPI,
    prefix: str = "blog",
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
        extensions=jinja2_extensions,
    )
    templates = Jinja2Templates(env=env)

    router = get_blog_router(templates=templates)
    app.include_router(router, prefix=f"/{prefix}", tags=["blog"])
    app.mount(
        "/static", StaticFiles(packages=[("fastapi_blog", "static")]), name="static"
    )
    return app
