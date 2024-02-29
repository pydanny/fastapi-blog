---
date: "2023-04-19T23:45:00.00Z"
published: true
slug: 2023-04-cookiecutter-options-pattern
tags:
  - cookiecutter
  - howto
  - python
  - tech.octopus.energy
time_to_read: 1
title: Cookiecutter Options Pattern
description: A technique I've used for years yet often forget. Placing it here for easy reference.
type: post
---

A way to simplify complicated Cookiecutters is the Options Pattern. If I step away from Cookiecutter for any duration, I forget about it. Thanks to [Mark Patricio](https://github.com/sammaritan12) for the reminder!

# Complex example we'll simplify:

Take a look at the arguments code:

```javascript
// cookiecutter.json
{
  "project_name": "thing",
  "volume": ["low", "medium", "high"]
}
```

And the template code (line breaks added so it fits on computer/tablet/mobile screens):

```django
# thing/config.py
# Volume: {% if cookiecutter.volume == "low" %}low
  {% elif cookiecutter.volume == "medium" %}medium
  {% elif cookiecutter.volume == "high" %}high{% endif %}
VOLUME_SETTING = {% if cookiecutter.volume == "low" %}5
  {% elif cookiecutter.volume == "medium" %}10
  {% elif cookiecutter.volume == "high" %}15{% endif %}
```

# Simplified example:

First the arguments code, which now contains a `__volume_options` field. 

``` javascript
// cookiecutter.json
{
  "project_name": "thing",
  "volume": ["low", "medium", "high"]
  "__volume_options": {
    "low": 5,
    "medium": 10,
    "high": 15
  }
}
```

By prefixing the `__volume_options` with double underscores, the field is now a [private variable](https://cookiecutter.readthedocs.io/en/stable/advanced/private_variables.html). This means it isn't displayed to the user during the arguments stage. Rather, it is just passed into the context of the template.

 This `__volume_options` field is also a [dict variable](https://cookiecutter.readthedocs.io/en/stable/advanced/dict_variables.html). It is a key/value type of object. This is important, as the Jinja renderer of Cookiecutter allows us to fetch the value of the pair by calling the key. 

Having `__volume_options` built around these two features allows us to simplify the template to the point where we don't need to add linebreaks to make it legible:

```django
# thing/config.py
# Volume: {{ cookiecutter.volume }}
VOLUME_SETTING = {{ cookiecutter.__volume_options[cookiecutter.volume] }}  
```

# Simplified result for easy reference

``` javascript
// cookiecutter.json
{
  "project_name": "thing",
  "volume": ["low", "medium", "high"]
  "__volume_options": {
    "low": 5,
    "medium": 10,
    "high": 15
  }
}
```

```django
# thing/config.py
# Volume: {{ cookiecutter.volume }}
VOLUME_SETTING = {{ cookiecutter.__volume_options[cookiecutter.volume] }}  
```



# Extra benefits to this approach

This puts more of the data into `cookiecutter.json` rather than the templates. Discovery of values is easier, smoothing the path for maintenance or new features.
