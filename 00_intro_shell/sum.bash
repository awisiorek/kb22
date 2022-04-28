#!/bin/bash
SUM=0
CAT=''

while [[ $# -ge 1 ]]; do
    case $1 in
        --help | -h)
            echo "Verwendung $0 [-N NUMBER]... [-S STRING]..."
            exit 0
            ;;
        -N)
            shift
            SUM=$((SUM + $1))
            ;;
        -S)
            shift
            CAT="$CAT$1"
            ;;
        *)
          echo "Verwendung $0 [-N NUMBER]... [-S STRING]..." 
          exit 1
          ;;
    esac
    shift
done
echo "SUMME: $SUM"
echo "STRING: $CAT"
