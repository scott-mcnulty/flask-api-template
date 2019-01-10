# Flask api template

A small template to use as a starting point for a Flask api.

# Table of Contents

- [Flask api template](#flask-api-template)
- [Table of Contents](#table-of-contents)
  - [Myapi Directory Structure](#myapi-directory-structure)
  - [Running the Application](#running-the-application)
  - [Deployment](#deployment)
  - [Testing](#testing)
    - [Credits](#credits)

## Myapi Directory Structure

    myapi
    ├── __init__.py
    ├── app.py                          : Main entrypoint for the app
    ├── config.py                       : Flask application configuration settings
    ├── gunicorn_config.py              : Gunicorn configuration settings
    ├── database.py                     : Database convenience functions
    ├── extensions.py                   : Flask extensions and middleware
    ├── api                             : Main flask-restful api
    │   ├── endpoints.py                : Different api classes mapped to http endpoints
    │   ├── __init__.py
    │   └── modules                     : Flask-restful api classes
    │       ├── __init__.py
    │       ├── auth.py
    │       ├── hello.py
    │       └── product.py
    ├── commons                         : Any common modules
    │   ├── __init__.py
    │   ├── log.py                      : Logging thats strapped to the gunicorn logger
    │   └── paginate.py                 : Pagination for querying
    └── models                          : Any database models
        ├── __init__.py
        └── product.py

## Running the Application

The app can be run using either the Dockerfile, docker-compose file, or by intsalling the packages locally and using the run.sh file. The application will be running on port `8000` with api url endpoints specified in the [myapi/api/endpoints.py](myapi/api/endpoints.py) file. At `/metrics` you'll see application metrics being exported that can be pulled in by a monitoring system such as prometheus.

## Deployment

The application can be deployed using a self hosting service with the `Dockerfile`. As an example this code was deployed using Heroku at the url `https://myapi-flask-template.herokuapp.com`.

## Testing

Tests are run using the `tox` testing framework along with pytest. First install `tox`:

```sh
pip install tox
```

Next run tox:

```sh
tox
```

### Credits

Code is based on:

- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask.git)
- [cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful.git)