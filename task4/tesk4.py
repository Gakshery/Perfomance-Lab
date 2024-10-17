import sys


file_nums = sys.argv[1]
nums = []
with open(file_nums, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))


nums.sort()
mediana = statistics.median(nums)

for num in nums:
    moves = sum(abs(num - mediana))

print(moves)