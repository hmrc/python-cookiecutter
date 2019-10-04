#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
import os


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


install_requires = read("requirements.txt")

setup(
    name="{{ cookiecutter.project_name }}",
    author="HMRC Platform Security",
    version=read(".version"),
    description="{{ cookiecutter.short_description }}",
    url="https://github.com/hmrc/{{ cookiecutter.project_name }}",
    long_description=read("README.md"),
    platforms=["Linux"],
    packages=find_packages(),
    install_requires=install_requires,
    {%- if cookiecutter.type == "package" %}
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_name }} = {{ cookiecutter.module_name }}.{{ cookiecutter.module_name }}:main"
        ]
    },
    {%- endif %}
)
