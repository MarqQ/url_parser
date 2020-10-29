#Base image
FROM python:3.8

# work directory
WORKDIR /core

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBUG 0

# psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# collect static files
RUN python manage.py collectstatic --noinput

# copy project
COPY . .

# gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT