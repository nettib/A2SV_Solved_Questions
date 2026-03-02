import math

n = int(input().strip())

points = list(map(int, input().split()))

points.sort()

print(points[math.ceil(n / 2) - 1])
