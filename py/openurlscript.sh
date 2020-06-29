#!/bin/bash
while read SITE
do
    open -a Safari "$SITE"
done < ./1.txt
