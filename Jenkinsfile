#!/usr/bin/env groovy
pipeline {
  agent any

  stages {
    stage('Prepare') {
      steps {
        step([$class: 'WsCleanup'])
        checkout(scm)
        sh("""virtualenv -p python3.6 venv
        . venv/bin/activate
        pip install -r requirements-tests.txt
        pytest --cov=grant_ssh_access --cov-fail-under=90
        flake8 grant_ssh_access
        deactivate""")
      }
    }
    stage('Build artefact') {
      steps {
        sh('docker run -t -v $(pwd):/data amazonlinux:2018.03.0.20180424 /data/package.sh')
      }
    }
    stage('Generate sha256') {
      steps {
        sh('openssl dgst -sha256 -binary grant_ssh_access.zip | openssl enc -base64 > grant_ssh_access.zip.base64sha256')
      }
    }
    stage('Upload to s3') {
      steps {
        sh("""for env in sandbox integration; do
                #development qa staging externaltest production; do
                aws s3 cp grant_ssh_access.zip s3://mdtp-lambda-functions-\${env}/grant_ssh_access.zip --acl=bucket-owner-full-control
                aws s3 cp grant_ssh_access.zip.base64sha256 s3://mdtp-lambda-functions-\${env}/grant_ssh_access.zip.base64sha256 --content-type text/plain --acl=bucket-owner-full-control
                done
        """)
      }
    }
  }
}
