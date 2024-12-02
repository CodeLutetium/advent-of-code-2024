l1, l2 = [], []

with open("day1_1.txt", "r") as f:
    for line in f:
        num1, num2 = line.strip().split("   ")
        l1.append(int(num1))
        l2.append(int(num2))

dist = 0
l1.sort()
l2.sort()

for i in range(len(l1)):
    dist += abs(l1[i] - l2[i])

print(dist)

"""
Time complexity: O(n log n)
Space complexity: O(n)

Alternatively, heap can be used (same time complexity)
"""
