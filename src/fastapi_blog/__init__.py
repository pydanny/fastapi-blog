from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import router


def add_blog_to_fastapi(app: FastAPI, prefix: str = "blog") -> FastAPI:
    app.include_router(router, prefix=f"/{prefix}", tags=["blog"])
    app.mount(
        "/static", StaticFiles(packages=[("fastapi_blog", "static")]), name="static"
    )
    return app
