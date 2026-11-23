
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

ARG EMBEDDING_MODEL
ENV EMBEDDING_MODEL=${EMBEDDING_MODEL}

RUN python -m rag.embeddings.build_index

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 4 --timeout 120 app.main:app"]
