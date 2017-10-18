#! /bin/bash
export PYTHONPATH=${PYTHONPATH}:../src:.
green -vvv --run-coverage -u */pyMwImportOWL/* --clear-omit
