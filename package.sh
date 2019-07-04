#!/bin/bash

set -xeou
yum install -y zip python36

BASEDIR=/data
PIPPACKAGESDIR=${BASEDIR}/lambda-packages

cd ${BASEDIR}

zip grant_ssh_access.zip grant_ssh_access/*

mkdir -p ${PIPPACKAGESDIR}
pip-3.6 install -t ${PIPPACKAGESDIR} -r requirements.txt
cd ${PIPPACKAGESDIR}
zip -r ../grant_ssh_access.zip .
