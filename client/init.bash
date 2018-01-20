#!/bin/bash

filename="$1"
while read -r line
do
    clue="$line"
    ./spot_dwords ${clue}
done < "$filename"
