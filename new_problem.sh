#!/bin/bash

PROJECT_NAME=$1
if [ -z "$PROJECT_NAME" ]
then 
    echo "Need to specify project name"
else 
    poetry new $PROJECT_NAME --quiet
    cd $PROJECT_NAME
    poetry add pytest --group dev
    poetry install

    mkdir .vscode
    cp ../setup/base_vscode_settings.json .vscode/settings.json
    cp ../setup/main.py $PROJECT_NAME/main.py
    cp ../setup/test_main.py tests/test_main.py

    # This is MacOS specific. On linux, you can omit the '' at the beginning
    sed -i '' "s/PROJECT_NAME/$PROJECT_NAME/" tests/test_main.py
    code .
fi