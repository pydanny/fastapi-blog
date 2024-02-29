import fastapi_blog
from fastapi import FastAPI


app = FastAPI()


@app.get("/api")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": "http://localhost:8000",
    }


# Because the prefix is None, the call to add_blog_to_fastapi
# needs to happen after the other view functions are defined.
app = fastapi_blog.add_blog_to_fastapi(app, prefix=None)
