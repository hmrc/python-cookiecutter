import os
import subprocess

is_lambda = "{{ cookiecutter.type }}" == "lambda"

if not is_lambda:
    os.remove("package.sh")
    os.remove("lambda_function.py")
    os.remove("Jenkinsfile")

subprocess.run(["git", "init", "."])
