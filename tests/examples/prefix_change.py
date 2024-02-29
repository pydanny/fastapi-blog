import fastapi_blog
from fastapi import FastAPI


app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app, prefix="/change")


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/change",
    }
