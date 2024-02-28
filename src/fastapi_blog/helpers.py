import functools
import pathlib

import markdown as md  #  type: ignore[import-untyped]
import yaml
from pymdownx import emoji  # type: ignore


@functools.lru_cache
def list_posts(published: bool = True) -> list[dict]:
    posts: list[dict] = []
    for post in pathlib.Path(".").glob("posts/*.md"):
        raw: str = post.read_text().split("---")[1]
        data: dict = yaml.safe_load(raw)
        data["slug"] = post.stem
        posts.append(data)

    posts = [x for x in filter(lambda x: x["published"] is True, posts)]

    posts.sort(key=lambda x: x["date"], reverse=True)
    return [x for x in filter(lambda x: x["published"] is published, posts)]


def load_content_from_markdown_file(path: pathlib.Path) -> dict[str, str | dict]:
    raw: str = path.read_text()
    # Metadata is the first part of the file
    page = {}
    page["metadata"] = yaml.safe_load(raw.split("---")[1])

    # Content is the second part of the file
    content_list: list = raw.split("---")[2:]
    page["markdown"] = "\n---\n".join(content_list)
    page["html"] = markdown(page["markdown"])

    return page


extensions = [
    "markdown.extensions.tables",
    "pymdownx.magiclink",
    "pymdownx.betterem",
    "pymdownx.tilde",
    "pymdownx.emoji",
    "pymdownx.tasklist",
    "pymdownx.superfences",
    "pymdownx.saneheaders",
]

extension_configs = {
    "pymdownx.magiclink": {
        "repo_url_shortener": True,
        "repo_url_shorthand": True,
        "provider": "github",
        "user": "facelessuser",
        "repo": "pymdown-extensions",
    },
    "pymdownx.tilde": {"subscript": False},
    "pymdownx.emoji": {
        "emoji_index": emoji.gemoji,
        "emoji_generator": emoji.to_png,
        "alt": "short",
        "options": {
            "attributes": {"align": "absmiddle", "height": "20px", "width": "20px"},
            "image_path": "https://github.githubassets.com/images/icons/emoji/unicode/",
            "non_standard_image_path": "https://github.githubassets.com/images/icons/emoji/",
        },
    },
}

markdown = functools.partial(
    md.markdown, extensions=extensions, extension_configs=extension_configs
)
