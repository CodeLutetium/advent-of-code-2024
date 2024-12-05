#!/bin/bash

: '
This shell script was created for Advent of Code 2024. This script will:
- Pull the daily challenge into a markdown file
- Download the input as .txt
- Create a template python file to read the input file.

To use, retrieve the session cookie and store it the dotenv file. 

Session cookie can be retrieved by following these steps:
1. Going to the input page (of any day)
2. Click F12, go to the network tab, and refresh
3. Right click on the input, and copy the cookie from the request header

This script is fully written by me, no copilot :)
'
source ./.env

# Check if challenge period is valid
start=$(date +%s -d '01/12/2024')
end=$(date +%s -d '01/01/2025')
today=$(date +%s)
if [ $today -ge $end ] || [ $today -lt $start ]
then 
    echo "Challenge is over!"
    exit 1
fi

# Get today's day and create directory
DATE=$(date +%-d)
mkdir -p day_$DATE
cd day_$DATE

# Retrieve and save the input if not exists
if [ ! -f "day_$DATE.txt" ];
then
    echo "Input file does not exist, pulling input file"
    curl "https://adventofcode.com/2024/day/$DATE/input" --compressed  -H "Cookie: session=$TOKEN" >> day_$DATE.txt
else
    echo "Input file exist"
fi

# Generate template and open with VS code
template="with open('day_$DATE.txt', 'r') as f:"

if [ ! -f "day$DATE\_1.py" ];
then
    echo $template > day$DATE\_1.py
fi

if [ ! -f "day$DATE\_2.py" ];
then
    echo $template > day$DATE\_2.py
fi
code .

# Windows
start "https://adventofcode.com/2024/day/$DATE"
# MacOS
# open "https://adventofcode.com/2024/day/$DATE"