#!/bin/bash

echo "running esearch"
echo "Database: $1, Query: $2"
esearch -db "$1" -query "$2" -retmax $3 | efetch -start 1 -stop $3 -format abstract> results.txt 
