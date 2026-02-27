t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    stripes = input().strip()

    min_recolor = float("inf")

    track = {"W": 0, "B": 0}

    for i in range(k):
        track[stripes[i]] += 1

    min_recolor = min(min_recolor, track["W"])

    for i in range(k, len(stripes)):
        track[stripes[i]] += 1

        track[stripes[i - k]] -= 1

        min_recolor = min(min_recolor, track["W"])

    print(min_recolor)
