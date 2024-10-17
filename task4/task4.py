import sys
import statistics

file_nums = sys.argv[1]
nums = []

with open(file_nums, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))

nums.sort()
mediana = statistics.median(nums)

moves = 0  
for num in nums:
    moves += abs(num - mediana)  

print(int(moves))