#!/bin/bash

echo "running esearch"


esearch -db "pubmed" -query "$1" | efetch -format json 
