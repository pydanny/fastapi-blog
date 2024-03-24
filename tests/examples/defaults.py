import fastapi_blog
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/blog",
    }
