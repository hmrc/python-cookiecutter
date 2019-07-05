
# {{cookiecutter.function_name}}

{{cookiecutter.description}}

### Development environment
1. Install pipenv
```
pip install pipenv
```

2. Clone the repository
```
git clone git@github.com:hmrc/{{cookiecutter.function_name}}.git
cd {{cookiecutter.function_name}}
pipenv install
pipenv shell
pip install tox
```

3. Run linters and tests
```
tox
```

4. Run formatter
```
tox -e black
```


### License

This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
