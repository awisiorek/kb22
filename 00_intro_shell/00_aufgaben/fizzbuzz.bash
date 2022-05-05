#!/bin/bash

if [[ $# != 1 ]]; then
    echo "usage: $0 N"
    exit 1
fi

if [[ ! $1 =~ [0-9]+ ]]; then
    echo "error: not a number: $1"
    exit 1
fi

for n in $(seq $1); do
    if [[ $((n%15)) == 0 ]]; then
        echo fizzbuz
    elif [[ $((n%3)) == 0 ]]; then
        echo fizz
    elif [[ $((n%5)) == 0 ]]; then
        echo buzz
    else
        echo $n
    fi
done
