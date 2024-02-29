from fastapi_blog import helpers


def test_list_published_posts_success():
    posts = helpers.list_posts(posts_dirname="tests/examples/posts")
    assert len(posts) == 18
    assert posts[0]["title"] == "Three Years at Kraken Tech"
    assert posts[-1]["title"] == "Code, Code, Code"


def test_list_published_posts_failure():
    posts = helpers.list_posts(posts_dirname="blarg")
    assert len(posts) == 0


def test_load_content_from_markdown_file_success():
    import pathlib

    path = pathlib.Path("tests/examples/posts/2023-11-three-years-at-kraken-tech.md")
    page = helpers.load_content_from_markdown_file(path)
    assert page["metadata"]["title"] == "Three Years at Kraken Tech"
    assert '<a href="https://kraken.tech/">Kraken Tech</a>' in page["html"]
    assert "[Kraken Tech](https://kraken.tech/)" in page["markdown"]
    assert "Three Years at Kraken Tech" in page["metadata"]["title"]
    assert (
        "Kraken Tech, an Octopus Energy Group subsidiary"
        in page["metadata"]["description"]
    )
