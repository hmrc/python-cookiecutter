#!/bin/bash

set -xeou
yum install -y zip python36

BASEDIR=/data
PIPPACKAGESDIR=${BASEDIR}/lambda-packages

cd ${BASEDIR}

zip {{ cookiecutter.function_name }}.zip {{ cookiecutter.module_name }}.py

mkdir -p ${PIPPACKAGESDIR}
pip-3.6 install -t ${PIPPACKAGESDIR} -r requirements.txt
cd ${PIPPACKAGESDIR}
zip -r ../{{ cookiecutter.function_name }}.zip .

