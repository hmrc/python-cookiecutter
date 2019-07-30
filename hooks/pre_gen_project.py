import re
import sys

PROJECT_REGEX = r"^[a-z][-a-z0-9]+$"
MODULE_REGEX = r"^[a-z][_a-z0-9]+$"

module_name = "{{ cookiecutter.module_name }}"
project_name = "{{ cookiecutter.project_name }}"

if not re.match(PROJECT_REGEX, project_name):
    print(
        'ERROR: "%s" is not a valid Python project name! (should-look-like-this)'
        % module_name
    )
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    print(
        'ERROR: "%s" is not a valid Python module name! (should_look_like_this)'
        % module_name
    )
    sys.exit(1)
