# Flask api template

A small template to use as a starting point for a Flask api.

# Table of Contents

- [Flask api template](#flask-api-template)
- [Table of Contents](#table-of-contents)
  - [Myapi Directory Structure](#myapi-directory-structure)
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
    │   ├── log.py                      : Logging thats straped to the gunicorn logger
    │   └── paginate.py                 : Pagination for querying
    └── models                          : Any database models
        ├── __init__.py
        └── product.py

## Testing

Tests are run using the `tox` testing framework along with pytest. First install `tox`:

```sh
pip install tox
```

Next run tox:

```sh
tox
```

## Credits

Code is based on:

  [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask.git)  
  [cookiecutter-flask-restful](https://github.com/karec/cookiecutter-flask-restful.git)