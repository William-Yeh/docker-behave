#!/bin/bash

docker run -it --rm -v "$(pwd):/behave"  behave  "$@"
