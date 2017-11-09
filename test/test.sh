#! /bin/bash
export PYTHONPATH=${PYTHONPATH}:../src:.
green3 -vvv --run-coverage -u */rdf2mw/* --clear-omit
