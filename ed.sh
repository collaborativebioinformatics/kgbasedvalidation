#!/bin/bash

echo "running esearch"
echo "Database: $1, Query: $2"

echo "Create a knowledge graph of $2 using the following abstracts: " > prompt.txt
esearch -db "$1" -query "$2" -retmax $3  | efetch -retype abstract -start 1 -stop $3 -format abstract> abstracts.txt
cat prompt.txt abstracts.txt >res2.txt



cat res2.txt > results.txt
