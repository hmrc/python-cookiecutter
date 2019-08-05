
# python-cookiecutter

This is a [cookiecutter](https://cookiecutter.readthedocs.io/) repo to 
bootstrap Python projects - either an installable package or an AWS Lambda.

### Out of the Box
* Could be either a lambda or a standard python package
* CI ready - see README.md in generated repo
* `tox` manages testing and releasing
* `pytest` test runner
* Coverage reporting and enforcement
* Enforce `black` formatting
* Enforce `flake8`

### Requirements
Install `cookiecutter` and `tox`:
```
pip install cookiecutter tox
```

You might need to run a pyenv rehash so the command-line utils become available:
```
pyenv rehash
```

### Usage
Generate a new Cookiecutter template layout:
```
cookiecutter gh:hmrc/python-cookiecutter
```

### License

This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
