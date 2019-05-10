# Releasing

1. Bump the version in `alembic_autogen_version.py`.
2. Commit with the version number as the message: `git commit -m "x.y.z"`
3. Tag the commit: `git tag x.y.z`
4. Push the tag: `git push --tags origin master`

Travis will take care of releasing to PyPI.
