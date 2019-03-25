#!/bin/sh


SCRIPTNAME="rmlc.sh"
IFS=""

if [ $# -lt 3 ]; then
    echo "Usage:"
    echo "$SCRIPTNAME [-more|-less] [numlines] file1 file2..."
    exit 
fi

if [ $1 == "-more" ]; then
    COMPARE="-gt" 
elif [ $1 == "-less" ]; then
    COMPARE="-lt" 
else
    echo "First argument must be -more or -less"
    exit 
fi

LINECOUNT=$2

shift 2

for filename in $*; do
    if [ ! -f "$filename" ]; then
        echo "Ignoring $filename"
        continue
    fi

    if [ "$filename" == "$SCRIPTNAME" ]; then
        continue
    fi

    lines=`cat "$filename" | wc -l`

    if [ $lines $COMPARE $LINECOUNT ]; then
        echo "Deleting $filename"
        rm "$filename"
    fi 
done
