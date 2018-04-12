#!/bin/bash
PYTHON="/Users/tibor/.virtualenvs/pdf-combine-env/bin/python"
SCRIPT_PATH="/Users/tibor/dev/pdfcombine/pdfcombine.py"
echo "The arguments are:"
echo $1 
echo $2

$PYTHON $SCRIPT_PATH $1 $2