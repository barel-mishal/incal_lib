import pathlib
from setuptools import setup, find_packages

# pip install --upgrade build twine
# python -m build
# python -m setup sdist
# twine check dist/*
# twine upload dist/*

HERE = pathlib.Path(__file__).parent

VERSION = '0.2.1'
PACKAGE_NAME = 'incal_lib'
AUTHOR = 'You'
AUTHOR_EMAIL = 'you@email.com'
URL = 'https://github.com/you/your_package'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Describe your package in one sentence'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    'numpy',
    'pandas'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
