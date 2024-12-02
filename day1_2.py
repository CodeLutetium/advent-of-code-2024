left, right = [], {}

with open("day1_1.txt", "r") as f:
    for line in f:
        num1, num2 = line.strip().split("   ")
        left.append(int(num1))
        right[int(num2)] = right.get(int(num2), 0) + 1

total_similarity = 0

for num in left:
    total_similarity += (num * right.get(num, 0))

print(total_similarity)

"""
Time complexity: O(n)
Space complexity: O(n)
"""
