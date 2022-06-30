#!/bin/bash

for d in "$@"; do
    if [[ ! -d "$d" ]]; then
        echo "not a dir: $d"
        exit 1
    fi
    for f in $d/*; do
        if [[ -f $f ]]; then
            size=$(cat "$f" | wc -c)
            sum=$((sum + size))
        elif [[ -d $f ]]; then
            size=$(bash $0 $f | awk '{print $NF}' | tr -d K)
            sum=$((sum + size * 1000))
        fi
    done
    echo "$d: $((sum/1000))K"
done
