reports = []

with open("day2.txt", "r") as f:
    for line in f:
        reports.append([int(level) for level in line.strip().split(" ")])

num_safe = 0

def is_safe(report):
    if len(report) < 2:
        return True
    
    increasing = report[1] > report[0]

    for i in range(1, len(report)):
        # Check if strictly increasing/decreasing
        if increasing and report[i] <= report[i - 1]:
            return False
        if not increasing and report[i] >= report[i - 1]:
            return False
        
        # Check diff
        if abs(report[i] - report[i - 1]) > 3:
            return False
        
    return True

num_safe = 0
for report in reports:
    if is_safe(report) == True:
        num_safe += 1

print(num_safe)

