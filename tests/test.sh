#!/usr/bin/env bash
set -e

rm -rf lambda-test/ package-test/

function generate_and_tox {
    cookiecutter --no-input --config-file "${1}-config.yaml" ../ 
    pushd "${1}-test" 
    tox
    popd
    
    rm -rf "${1}-test"
}

generate_and_tox package
generate_and_tox lambda
