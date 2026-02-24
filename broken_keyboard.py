t = int(input().strip())

for _ in range(t):
    s = input().strip()

    l, r = 0, 1
    res = set()

    while l < len(s):
        if r >= len(s):
            res.add(s[l])
            l += 1
        elif s[l] == s[r]:
            l += 2
            r += 2
        else:
            res.add(s[l])
            l += 1
            r += 1

    print("".join(sorted(list(res))))
