# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.12

FROM python:${PYTHON_VERSION}-alpine

LABEL fly_launch_runtime="flask"

WORKDIR /code

COPY . .

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base \
    && pip install --upgrade pip \
    && pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--debug", "--host=0.0.0.0", "--port=5000"]
