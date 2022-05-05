#!/bin/bash

if [[ $# != 1 ]]; then
    echo "usage: $0 DIR"
    exit 1
fi

if [[ ! -d "$1" ]]; then
    echo "error: $1 is not a directory"
    exit 1
fi

for f in $1/*; do
    if [[ -d $f ]]; then
        echo $f: directory
    elif [[ -f $f ]]; then
        echo $f: file
    else
        echo $f: ??
    fi
done
