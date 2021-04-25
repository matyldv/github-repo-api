FROM python:3.9.1-alpine3.12

WORKDIR /code
ENV FLASK_APP=/code/run_server.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./code/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./code .

LABEL maintainer Olga Matyla
LABEL Project=github-repo-api