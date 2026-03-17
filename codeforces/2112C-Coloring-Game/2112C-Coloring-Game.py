t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))

    count = 0
    _max = a[-1]
    for k in range(2, n):
        need = max(_max, 2 * a[k])
        l = 0
        r = k - 1

        while l < r:
            if a[l] + a[r] + a[k] > need:
                count += (r - l)
                r -= 1
            else:
                l += 1

    print(count)