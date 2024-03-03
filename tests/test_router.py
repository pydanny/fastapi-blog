import fastapi_blog
from fastapi import FastAPI
from fastapi.testclient import TestClient


app = FastAPI()
app = fastapi_blog.add_blog_to_fastapi(app)

client = TestClient(app)


def test_blog_index():
    response = client.get("/blog")
    assert response.status_code == 200
    assert "<title>Daniel Roy Greenfeld</title>" in response.content.decode()
