import fastapi_blog
import jinja2
from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()
# TODO - fix this to use PackageLoader
app = fastapi_blog.add_blog_to_fastapi(
    app, jinja2_loader=jinja2.FileSystemLoader("src/fastapi_blog/templates")
)

client = TestClient(app)


def test_blog_index():
    response = client.get("/blog")
    assert response.status_code == 200
    assert "<title>Daniel Roy Greenfeld</title>" in response.content.decode()
