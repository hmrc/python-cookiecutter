#!/usr/bin/env python3
"""{{ cookiecutter.description }}."""
import os
import traceback

import requests



def lambda_handler(event, context):
    return main()


def main():
    try:
        return {"status_code": "200"}
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}

