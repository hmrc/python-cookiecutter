#!/usr/bin/env python3
"""{{ cookiecutter.description }}."""
{% if cookiecutter.type == "lambda" %}
import traceback


def lambda_handler(event, context):
    return main(event["user_name"])


def main(user_name):
    try:
        if user_name != "oops":
            return {"status_code": "200"}
        raise Exception("oops")
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}
{% elif cookiecutter.type == "package" %}
import sys


def main():
    print("Hello, " + sys.argv[1] + "!")
{% endif -%}
