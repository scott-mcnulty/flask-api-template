FROM python:3.6-alpine

# https://github.com/psycopg/psycopg2/issues/684
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY myapi /app/myapi
WORKDIR /app

COPY requirements/requirements.txt /app
RUN pip install -r requirements.txt

CMD [ "gunicorn", "--config", "myapi/gunicorn_config.py", "myapi.app:create_app()" ]