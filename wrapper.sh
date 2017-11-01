#!/bin/bash
#
# Simple wrapper for executing behave within Docker.
#
# ENVIRONMENT VARIABLES:
#
#    - REQUIREMENTS_PATH: requirements fullpath;
#          default = "features/steps/requirements.txt"
#


#
# install Python packages for testing purpose, if any.
#

if [ -z "$REQUIREMENTS_PATH" ]; then
    REQUIREMENTS_PATH=features/steps/requirements.txt
fi

if [ -f "$REQUIREMENTS_PATH" ]; then
    pip3 install --no-cache-dir -r $REQUIREMENTS_PATH
fi


#
# execute behave
#

exec behave "$@"