import fastapi_blog
import jinja2
from fastapi import FastAPI


prefix = "/content"
django_style_jinja2_loader = jinja2.ChoiceLoader(
    [
        jinja2.FileSystemLoader("templates"),
        jinja2.PackageLoader("fastapi_blog", "templates"),
    ]
)

app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(
    app, prefix=prefix, jinja2_loader=django_style_jinja2_loader
)


@app.get("/")
async def index() -> dict:
    return {
        "message": "Check out the blog at the URL",
        "url": f"http://localhost:8000/{prefix}",
    }
