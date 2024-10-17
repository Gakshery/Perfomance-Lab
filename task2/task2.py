import sys
import math


with open(sys.argv[1], 'r') as file1:
    x_centr, y_centr = map(float, file1.readline().split())
    radius = float(file1.readline())


with open(sys.argv[2], 'r') as file2:
    for line in file2:
        x_dot, y_dot = map(float, line.split())
        
        place = math.sqrt((x_dot - x_centr) ** 2 + (y_dot - y_centr) ** 2)

        if place < radius:
            print("1")
        elif place == radius:
            print("0")
        elif place > radius:
            print("2")
