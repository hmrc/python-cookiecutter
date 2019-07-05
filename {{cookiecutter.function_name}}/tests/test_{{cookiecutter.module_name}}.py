"""Test the main module."""
from {{cookiecutter.module_name}} import {{cookiecutter.module_name}}


def test_happy_path():
    response = {{cookiecutter.module_name}}.main("")

    assert response["status_code"] == "200"


def test_failure():
    response = {{cookiecutter.module_name}}.main("oops")

    assert "error" in response


def test_lambda():
    response = {{cookiecutter.module_name}}.lambda_handler({"user_name": "okay"}, {})

    assert response["status_code"] == "200"
