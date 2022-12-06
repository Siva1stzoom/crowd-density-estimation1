#!/bin/sh

set -o errexit
set -o nounset

# Absolute path to this script
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in
SCRIPTPATH=$(dirname "$SCRIPT")
cd $SCRIPTPATH
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
