#!/bin/bash

rm -rf _build/
mkdir _build

python build.py

cp _src/styles.css _build/styles.css
cp -r _src/images/ _build/images