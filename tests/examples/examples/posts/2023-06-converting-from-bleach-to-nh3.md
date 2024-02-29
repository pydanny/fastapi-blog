---
date: "2023-06-09T23:45:00.00Z"
published: true
slug: 2023-06-converting-from-bleach-to-nh3
tags:
  - howto
  - python
  - rust-lang
time_to_read: 1
title: Converting from bleach to nh3
description: Bleach is deprecated, here's how to come close to replicating bleach.clean() with no arguments with nh3.
type: post
---

[Bleach is deprecated](https://github.com/mozilla/bleach/issues/698), here's how to come close to replicating `bleach.clean()` using the [nh3](https://github.com/messense/nh3) version of `.clean()`.

```python
import nh3

def clean_string(string: str) -> str:
    # The arguments below being passed to `nh3.clean()` are
    # the default values of the `bleach.clean()` function. 
    return nh3.clean(
        string,
        tags={
            "a",
            "abbr",
            "acronym",
            "b",
            "blockquote",
            "code",
            "em",
            "i",
            "li",
            "ol",
            "strong",
            "ul",
        },
        attributes={
            "a": {"href", "title"},
            "abbr": {"title"},
            "acronym": {"title"},
        },
        url_schemes={"http", "https", "mailto"},
        link_rel=None,
    )
```

The big difference is unlike the safing of HTML done by bleach, nh3 removes the offending tags altogether. Read the comments below to see what this means.

Results:

```python
>>> input_from_user = """<b>
<img src="">
I\'m not trying to XSS you <a href="https://example.com">Link</a>
</b>"""
>>>
>>> # By default, bleach version safes the HTML
>>> # rather than remove the tags altogether.
>>> bleach.clean(input_from_user)
'<b>&lt;img src=""&gt;I\'m not trying to XSS you <a href="https://example.com">Link</a></b>'
>>>
>>> # In contrast, nh3 removes the offending tags entirely
>>> # while also preserving whitespace.
>>> clean_string(input_from_user)
'<b>\n\nI\'m not trying to XSS you <a href="https://example.com">Link</a>\n</b>'
```

# Advantages of switching to nh3 are:

1. nh3 is actively maintained, bleach is officially deprecated. 
2. I believe the nh3 technique of stripping tags rather than allowing safing is more secure. The idea of safing is great, but I've always wondered if a creative attacker could find a way to exploit it. So I think it is better to remove the offending tags altogether.
3. The preservation of whitespace is really useful for preserving content submitted in a textarea. This is especially true for Markdown content.
4. nh3 is a binding to the [rust-ammonia project](https://github.com/rust-ammonia/ammonia). They claim a 15x speed increase over bleach's binding to the html5lib project. Even if that is a 3x exaggeration, that's still a 5x speed increase.

# nh3 + Django

If you're coding in Django, you owe it to yourself and all your users to read Adam Johnson's [fantastic article on using nh3 with Django](https://adamj.eu/tech/2023/12/13/django-sanitize-incoming-html-nh3/). 

# Update

- 2023/12/14 - Added mention of Adam Johnson's article on nh3 + Django