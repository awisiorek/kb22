#!/bin/bash
# sed & awk 2nd Edition, Dale Dougherty & Arnold Robbins, O'Reilly

if [[ $# -lt 3 ]]; then
    echo "Usage $0 PATTERN REPLACEMENT FILE" >&2
    exit 1
fi

pattern=$1
replacement=$2

if [[ -f "$3" ]]; then
    file=$3
else
    echo $3 is not a file. >&2
    exit 1
fi
sed -n -e "s/$pattern/$replacement/gp" "$file"
#sed -n -e "s#$pattern#$replacement#gp" "$file"

#A="$(echo | tr '\012' '\001')"
#sed -n -e "s$A$pattern$A$replacement${A}gp" "$file"
