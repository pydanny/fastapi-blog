import fastapi_blog
from fastapi import FastAPI


app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app)


@app.get("/")
async def index() -> dict:
    return {"message": "Hello World"}
