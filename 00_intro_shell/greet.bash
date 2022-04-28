#!/bin/bash
echo '[debug] $#:' $#
for name in $@; do
    echo "Hallo $name"
done