import re

from setuptools import setup

INSTALL_REQUIRES = ["alembic", "click>=7.0"]
EXTRAS_REQUIRE = {
    "tests": ["pytest"],
    "lint": ["fourmat~=0.4.3", "pre-commit"],
}
EXTRAS_REQUIRE["dev"] = (
    EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]
)
PYTHON_REQUIRES = ">=3.6"


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="alembic-autogen-check",
    version=find_version("alembic_autogen_check.py"),
    description="CLI to check if alembic migrations are in sync with your SQLAlchemy models.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="4Catalyzer",
    author_email="sloria@butterflynetinc.com",
    url="https://github.com/4Catalyzer/alembic-autogen-check",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=PYTHON_REQUIRES,
    license="MIT",
    zip_safe=False,
    keywords="sqlalchemy alembic",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    py_modules=["alembic_autogen_check"],
    entry_points={
        "console_scripts": [
            "alembic-autogen-check = alembic_autogen_check:main"
        ]
    },
)
