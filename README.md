# alembic-autogen-check

[![Travis-CI](https://badgen.net/travis/4Catalyzer/alembic-autogen-check/master)](https://travis-ci.org/4Catalyzer/alembic-autogen-check)

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
