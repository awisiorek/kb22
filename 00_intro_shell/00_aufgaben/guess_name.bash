#!/bin/bash

secret="Homer Simpson"

for n in "$@"; do
    echo $n
    if [[ $n == $secret ]]; then
        exit 0 # return success
    fi
done
exit 1 # return error

