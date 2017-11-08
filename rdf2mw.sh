#! /bin/bash
export PYTHONPATH=${PYTHONPATH}:src/
python3 src/rdf2mw.py "$@"
