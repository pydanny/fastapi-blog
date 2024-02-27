# Dockerfile for building a FastAPI Blog image
# This is a multi-stage build
# The first stage is to build the application
# The second stage is to run the application

# Use the official image as a parent image
FROM python:3.12-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install make
RUN apk add --no-cache make

# Install fastapi-blog for local development
# This installs any needed packages specified in pyproject.toml
# as local development dependencies
RUN make install

# Run tests
RUN make test

# Configure the container to run the application
ENV PORT=8000

# Expose the port the app runs on
EXPOSE 8000

# Run the application
# RUN make run
# CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
CMD uvicorn tests.example.main:app --host 0.0.0.0 --port ${PORT}
