import fastapi_blog
from fastapi import FastAPI


favorite_post_ids = {
    "code-code-code",
    "thirty-minute-rule",
    "2023-11-three-years-at-kraken-tech",
}

app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app, favorite_post_ids=favorite_post_ids)


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000/blog",
    }

