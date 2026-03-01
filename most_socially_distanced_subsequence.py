t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().split()))

    ans = [p[0]]
    flag = 0

    if p[1] > p[0]:
        flag = 1

    for i in range(1, len(p)):
        if not flag and p[i] > p[i - 1]:
            ans.append(p[i - 1])
            flag = 1
        elif flag and p[i] < p[i - 1]:
            ans.append(p[i - 1])
            flag = 0

    ans.append(p[-1])

    print(len(ans))
    print(*ans)
