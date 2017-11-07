#! /bin/bash
export PYTHONPATH=${PYTHONPATH}:../src:.
green3 -vvv --run-coverage -u */pyMwImportOWL/* --clear-omit
