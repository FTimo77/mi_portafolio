#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

rm -rf public
reflex init
reflex export --frontend-only

unzip frontend.zip -d public

# 👇 Esta línea es esencial para que el gif se suba
cp code.gif public/

rm -f frontend.zip
deactivate


