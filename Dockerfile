# Use python-3.11-slim as base image
FROM python:3.11-slim as base

LABEL authors="codyconfer"

# Set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

# Install poetry
RUN pip install 'poetry==1.4.2'

# Disable virtualenv creation
RUN poetry config virtualenvs.create false

# Copy source
WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./
COPY ./src ./src

# Install dependencies
RUN poetry install

# Run
ENTRYPOINT ["poetry", "run", "python", "./src/main.py"]
