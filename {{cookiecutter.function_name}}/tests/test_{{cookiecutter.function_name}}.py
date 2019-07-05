"""Test the main module."""
from {{cookiecutter.function_name}} import {{cookiecutter.function_name}}



def test_happy_path():
    response = {{cookiecutter.function_name}}.main()

    assert response["status_code"] == "200"

