#!/usr/bin/env sh
set -euo pipefail

python3 -m venv venv
. ./venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install pip-tools
pip install -r requirements.txt
