#!/bin/bash
PYTHON="/Users/Tibor/.virtualenvs/pdf-combine-env/bin/python"
# echo "The dirname is `dirname $0`"
SCRIPTDIR=`dirname $0`
# echo $SCRIPTDIR
SCRIPT_PATH=$SCRIPTDIR"/pdfcombine.py"
# echo $SCRIPT_PATH
ARGS="$@"
# echo $ARGS

$PYTHON $SCRIPT_PATH $ARGS