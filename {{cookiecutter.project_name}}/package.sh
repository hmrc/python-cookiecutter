#!/bin/bash

set -xeou
yum install -y zip python36

BASEDIR=/data
PIPPACKAGESDIR=${BASEDIR}/lambda-packages

cd ${BASEDIR}

zip {{ cookiecutter.project_name }}.zip lambda_function.py

mkdir -p ${PIPPACKAGESDIR}
pip-3.6 install -t ${PIPPACKAGESDIR} .
cd ${PIPPACKAGESDIR}
zip -r ../{{ cookiecutter.project_name }}.zip .

