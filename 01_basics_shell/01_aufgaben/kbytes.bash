#!/bin/bash
for f in "$@"; do

#    if [[ ! -f $f ]]; then
#        echo "not a dir: $f"
#        exit 1
#    fi

    bytes=$(cat $f | wc -c)
    kbytes=$((bytes/1000))
    echo $f: ${kbytes}K
done
