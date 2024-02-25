import pathlib
from datetime import date

from feedgen.feed import FeedGenerator  # type: ignore[import-untyped]

from . import helpers


def generate_feed(tag: str) -> str:
    posts: list[dict] = helpers.list_posts()[:3]
    if tag != "atom":
        posts = [x for x in filter(lambda x: tag in x.get("tags", []), posts)]

    base_url: str = "https://daniel.feldroy.com"

    fg = FeedGenerator()
    fg.id(base_url + "/")
    fg.title(f"Posts tagged with {tag}")
    fg.author({"name": "Daniel Roy Greenfeld", "email": "daniel@feldroy.com"})
    fg.description("Inside the head of Daniel Roy Greenfeld")
    fg.link(href="http://daniel.feldroy.com", rel="alternate")
    fg.logo(f"{base_url}/images/pydanny-cartwheel.png")
    fg.image(f"{base_url}/images/pydanny-cartwheel.png")
    fg.copyright(f"All rights reserved {date.today().year}, Daniel Roy Greenfeld")
    fg.subtitle("Inside the head of pydanny")
    fg.link(href="http://daniel.feldroy.com", rel="self")
    fg.language("en")

    # Reverse the order of posts so feedgen orders things correctly
    posts.reverse()
    for post in posts:
        fe = fg.add_entry()
        fe.id(post["slug"])
        fe.title(post["title"])
        fe.link(href=f"http://daniel.feldroy.com/posts/{post['slug']}")
        path = pathlib.Path(f"posts/{post['slug']}.md")
        page = helpers.load_content_from_markdown_file(path)
        fe.content(f"<![CDATA[ { page['html'] } ]]>")

    return fg.atom_str(pretty=True)


# atomfeed = fg.atom_str(pretty=True) # Get the ATOM feed as string
# rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
# fg.atom_file('atom.xml') # Write the ATOM feed to a file
# fg.rss_file('rss.xml') # Write the RSS feed to a file
