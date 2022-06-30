#!/bin/bash

for d in "$@"; do
    if [[ ! -d "$d" ]]; then
        echo "not a dir: $d"
        exit 1
    fi
    size=$(ls -l "$d" | awk 'BEGIN{sum=0} /^-/{sum+=$5} END{print int(sum/1000)}')
    echo "$d: ${size}K"
done
