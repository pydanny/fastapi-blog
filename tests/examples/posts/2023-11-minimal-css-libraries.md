---
date: "2023-11-20T17:30:00.00Z"
published: true
slug: til-2023-11-minimal-css-libraries
tags:
  - blog
time_to_read: 1
title: "Minimal CSS libraries"
description: Minimal CSS frameworks do not use classes, rather modifying the look of HTML components. That means that any CSS classes added are easier to discover and read.

---

Minimal CSS frameworks do not use classes, rather modifying the look of HTML components. That means that any CSS classes added are easier to discover and read.

I'm someone who struggles with CSS and the custom CSS of this site combined with complex non-obvious HTML (example being `<ul>` and `<li>` for content sections) partially obscured by React components has been hard on me. I've wanted to make changes but kept running into walls when I wanted to do things like add dark mode. I tried bringing in heavy CSS frameworks, but having to fix/change hundreds of tags was not someting I wanted to do.

Enter the minimal approach. With minimal CSS the updates are easy, as is migrating to new tools as current ones go out of style. I took out the worst offenders (`<ul>` and `<li>` for content) and replaced them more appropriate `<h2>` and `<p>` tags.

The result is closer to the HTML specification and hence easier to read. Definately fits in with the concepts of [HTML First](https://html-first.com/).

One feature I can't wait to implement is a dark mode controlled by media query (or a toggle). Before it meant tracking down all the CSS components, now it's just pointing at different Sakura themes. 

As for how it looks, check out the before and after images below:

**Old 100% handcrafted CSS**

I was never happy with the spacing between elements, and struggled with all the CSS bits to make it work.

![Old custom CSS](/images/css-before.png)

**Minimal CSS library + a few custom classes**

In the new version the default spacing is really nice, and my only challenge was getting my avatar image to come down `2.5 rem`.

![New CSS](/images/css-after.png)

## Resources:

- [Sakura](https://github.com/oxalorg/sakura) - CSS framework now helping to style this site
- [Drop-in Minimal CSS comparison framework site](https://dohliam.github.io/dropin-minimal-css/?sakura)

