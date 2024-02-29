---
date: "2023-01-27T23:45:00.00Z"
published: true
slug: converting-markdown-headers-to-checklist
tags:
  - python
  - nodejs
  - javascript
  - markdown
  - howto
time_to_read: 5
title: Converting Markdown Headers to Checklist
description: For those times when you write out a long markdown document that you want to convert to a checklist.
type: post
image: /images/superhero-markdown-checklist.png
---

For those times when you write out a long markdown document that you want to convert to a checklist.

# Converting Markdown Headers to Checklist

Python:

```python
response = []
with open("sample.md") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("#"):
          indentation = line.count("#") - 1
          newline = f"{' ' * 2 * indentation}- [ ]{line.replace('#', '')}"
          response.append(newline)

with open("checklist.md", "w") as f:
    f.writelines(response)
```

JavaScript:

```javascript
const fs = require("fs");

function MarkdownHeadersToChecklist(markdown) {
  const lines = markdown.split("\n");
  const headers = lines.filter((line) => line.startsWith("#"));
  let checklist = [];
  for (const header of headers) {
    const indentation = header.split("#").length - 1;
    const spacer = " ".repeat(2 * indentation);
    const newline = `${spacer}- [ ]${header.replace("#", "")}`;
    checklist.push(newline);
  }
  return checklist.join("\n");
}

const markdown = fs.readFileSync("sample.md", "utf8");

const checklist = MarkdownHeadersToChecklist(markdown);

fs.writeFileSync("checklist.md", checklist);
```

![Converting Markdown Headers to Checklist](/images/superhero-markdown-checklist.png)
