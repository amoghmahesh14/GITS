#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

PROJECT_DIR=${SCRIPT_DIR%/*}

RELATIVE_GITS_PATH="code/gits.py"

# Check if python3 is available, otherwise use python
# if command -v python3 &> /dev/null; then
#     PYTHON_COMMAND="python3"
# else
    echo "Warning: python3 is not available, falling back to python."
    PYTHON_COMMAND="python"
# fi

GITS_EXEC_PATH="${PROJECT_DIR}/${RELATIVE_GITS_PATH}"

BASHRC=~/.bashrc
if [ -f "$BASHRC" ]; then
    echo "$BASHRC exists, appending gits commandline tool alias"
    echo "alias gits=\"$PYTHON_COMMAND $GITS_EXEC_PATH\"" >> $BASHRC
else
    echo "$BASHRC does not exist, creating a new file and adding gits commandline tool alias"
    echo "alias gits=\"$PYTHON_COMMAND $GITS_EXEC_PATH\"" >> $BASHRC
fi

echo "Initializing gits directory in user home directory"

GITS=~/.gits
GITS_LOG=~/.gits/logs

mkdir -p $GITS $GITS_LOG
