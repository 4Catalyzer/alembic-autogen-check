# alembic-autogen-check

[![Latest version](https://badgen.net/pypi/v/alembic-autogen-check)](https://pypi.org/project/alembic-autogen-check/)
[![Travis-CI](https://badgen.net/travis/4Catalyzer/alembic-autogen-check/master)](https://travis-ci.org/4Catalyzer/alembic-autogen-check)

Command to check that alembic migrations are in sync with SQLAlchemy models.

![screenshot](https://user-images.githubusercontent.com/2379650/57626497-02765680-7564-11e9-8854-fc3a469919af.png)

## Install

```
pip install alembic-autogen-check
```

## Usage

```
PYTHONPATH=. alembic-autogen-check
```

This assumes that an `alembic.ini` file exists in the current working
directory. You can explicitly pass a config file:

```
PYTHONPATH=. alembic-autogen-check --config path/to/alembic.ini
```
