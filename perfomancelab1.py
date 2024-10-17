import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

lst = []
num = 1

for i in range(n):
    lst.append(num)
    num = 1 + (num + m - 2) % n
    if num == 1:
        break

print(''.join(map(str, lst)))

