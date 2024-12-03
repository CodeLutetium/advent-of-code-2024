import re

input = ""

with open("day3.txt", 'r') as f:
    input = f.read()

# Look for matches
matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", input)

res = 0

for match in matches:
    operands = match[4:-1].split(",")
    res += int(operands[0]) * int(operands[1])

print(res)
    
