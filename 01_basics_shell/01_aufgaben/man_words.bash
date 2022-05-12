#!/bin/bash
for p in "$@"; do
    if man $p > /dev/null 2>&1; then 
        echo $p: $(man $p | wc -w)
    else
        echo $p: ??
    fi
done
