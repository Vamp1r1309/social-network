FROM python:3.11-slim
WORKDIR /code
COPY requierements.txt .
RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && pip install -r requierements.txt
COPY . ./
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000