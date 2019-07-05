# {{ cookiecutter.function_name }}

{{ cookiecutter.description }}

### Development environment
1. Install pipenv and pre-commit
```
pip install pipenv pre-commit
```

2. Clone the repository
```
git clone git@github.com:hmrc/{{ cookiecutter.function_name }}.git
cd {{ cookiecutter.function_name }}
pre-commit install && pre-commit autoupdate
pipenv install && pipenv install tox
```

3. To run linters and tests
```
pipenv run tox
```

4. To run formatter
```
tox -e black
```

### Adding dependencies

- Runtime dependencies should be pinned in `requirements.txt`
- Testing dependencies should be added to `tox.ini`

### License

This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
