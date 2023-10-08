#!/bin/bash

PROJECT_NAME=$1
if [ -z "$PROJECT_NAME" ]
then 
    echo "Need to specify project name"
else 
    poetry new $PROJECT_NAME --quiet --name src
    cd $PROJECT_NAME
    poetry add pytest --group dev
    poetry install

    mkdir .vscode
    cp ../setup/base_vscode_settings.json .vscode/settings.json
    cp ../setup/main.py src/main.py
    cp ../setup/test_main.py tests/test_main.py

    code .
fi