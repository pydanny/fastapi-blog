---
date: "2023-01-14T22:20:50.52Z"
published: true
tags:
  - python
  - django
  - fastapi
  - flask
time_to_read: 2
title: Practice Python Web Projects
description: Python web projects taken from my personal history to practice on to improve your skills.
image: /images/Practice-Python-Web-Projects.png
og_url: https://daniel.feldroy.com/posts/2023-01-practice-python-web-projects
---

I firmly believe that substantial improvement in any skill can only be achieved through [practice](https://daniel.feldroy.com/posts/code-code-code). With that in mind, I have compiled a list of projects I have built over the years to practice my skills with web frameworks. I hope that these projects, which have proven effective for me in learning frameworks, will also assist you in your growth.

These projects are framework-agnostic and can be implemented using [Django](https://djangoproject.com), [Flask](https://flask.palletsprojects.com/), [FastAPI](https://fastapi.tiangolo.com/), or any other framework of your choice. While some projects may be better suited for certain frameworks, all of them provide valuable practice. All of these projects can be completed using either the default frontend templating system or a frontend framework like React or Vue.

# The Projects

## 1. API to Data

Creating a web application to present data can be a lot of work. An alternative option is to build an API that returns the data in a well-structured format. This project is a great opportunity to practice using Django REST Framework, Flask, or FastAPI. In fact, it is my understanding that FastAPI was specifically designed for this purpose. Nevertheless, this project can be implemented using any framework and is a valuable practice.

Bonus points: Don't create the data that you are working with. Instead, request for data from someone else. This will not only give you practice in creating an API but also in working with data provided by others, which is an important skill to have.

## 2. Show me the charts

Graphviz is a powerful command-line tool for generating graphical representations of data. This project involves creating a simple API that takes a Graphviz file as input, and returns a PNG image of the generated graph. The API can be built using HTML form that accepts Graphviz dot format, saves it as a file on the server, and renders the resulting image for the user to view.

I have built this project several times in the past, with my first implementation in 2006 using web.py. It is a great project to practice file handling and working with command-line tools in a web environment.

Bonus points: Saving changes to files over time so the user can go back and see what they've created in the past.

## 3. Wiki

Build a wiki with the following requirements:

- Users can create pages, edit pages, and delete pages
- Content is stored as Markdown and served as HTML
- Persistence can be a database or a set of markdown files
- Slugs for pages are automatically generated from the title
- If someone tries to create a page with a slug that already exists, they are redirected to the existing page
- Any and all changes to content pages have to be tracked in an audit log viewable by any user
- Include search functionality

Bonus points: Add the ability to report pages as spam, and have a moderation queue for pages that have been reported.

## 4. Social Network

Build a social network with the following features:

- User registration
- Event stream like Twitter, Facebook, or Mastodon
- Ability to become friends with other users, friendship comes with an approval process. Friendship allows DMs
- Ability to follow other users' stream, no permission needed
- Direct messaging system

Historical note: My first professional Django Project was this project, it was a great way to learn the framework. It resulted in the creation of what is now known as [django-crispy-forms](https://pypi.org/project/django-crispy-forms/). Alas, the social network we built, "Spacebook", hasn't been online for over a decade.

Bonus points: Add public and private groups for people who share a similar interest.

## 5. Turn-based game

Build a turn-based game that uses a web interface. It can be as simple as tic-tac-toe or something more sophisticated with multiple players.

Bonus points: Use websockets to notify players when it's their turn.

## 6. Advert-free story-lite recipe site

Searching for recipes can be frustrating, often requiring one to sift through lengthy personal anecdotes and ads before finding the desired information. Build a website that allows users to easily search for recipes and presents only the recipe without any additional distractions such as ads or personal stories. Requirements:

- Visitors can search for recipes
- Users can create their own accounts
- Users can create their own recipes
- The description/history of a recipe has to be limited to 500 characters
- Provide an API for searching, listing, and examining recipes

Bonus points: Provide ability for users to upload images for recipes. These images need to be stored in a CDN and not on the server.

## 7. Third-party Package

> _You don't really know a framework or its configuration until you build an installable package deployed to PyPI._

> _-- Someone at the 2009 PyCon US sprint_

Requirements:

- Must be installable via pip
- Must be usable with Django, Flask, or FastAPI
- Includes extensive documentation
- Docs hosted on Read the Docs or other documentation hosting service

This is a great project to practice with Django, Flask, or FastAPI.

Bonus points: Package can be used with all three web frameworks: Django, Flask, and FastAPI.

![https://daniel.feldroy.com/posts/2023-01-practice-python-web-projects](/images/Practice-Python-Web-Projects.png)
