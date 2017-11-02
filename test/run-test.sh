#!/bin/bash

docker run -it -v "$(pwd):/behave:ro"  behave  "$@"
