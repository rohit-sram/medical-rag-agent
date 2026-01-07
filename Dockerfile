FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml /app/
COPY uv.lock /app/uv.lock

RUN uv sync --system --no-dev || uv pip install --system --no-cache-dir .

COPY . /app

EXPOSE 8080

CMD ["python", "app.py"]