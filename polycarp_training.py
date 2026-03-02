n = int(input().strip())

contests = list(map(int, input().split()))

contests.sort()

days = 0

idx = 0
for day in range(1, max(contests) + 1):
    if idx >= len(contests):
        break
    while day > contests[idx]:
        idx += 1

    if day <= contests[idx]:
        days += 1
        idx += 1

print(days)
