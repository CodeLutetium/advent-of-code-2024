import re

input = ""

with open("day3.txt", 'r') as f:
    input = f.read()

# Remove don't()... from input
input = re.sub("don\'t\(\).*?(?:$|do\(\))", "", input, flags=re.DOTALL)

# Look for matches
matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", input)

res = 0

for match in matches:
    operands = match[4:-1].split(",")
    res += int(operands[0]) * int(operands[1])

print(res)
    
