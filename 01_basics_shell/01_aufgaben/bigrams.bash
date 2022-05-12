#!/bin/bash

if [[ $# != 1 ]]; then
    echo "Usage $0 FILE" && exit 1
fi

cat $1 | tr -d '[:digit:]' | tr '[:punct:]' ' ' | tr -s ' ' '\n' > toks.txt
tail -n +2 toks.txt | paste -d " " toks.txt - | sort -f | uniq -ic | sort -nr

rm toks.txt
