# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Coletar arquivos estáticos no build (opcional)
docker-compose run web python manage.py collectstatic --noinput
# RUN python manage.py collectstatic --noinput
