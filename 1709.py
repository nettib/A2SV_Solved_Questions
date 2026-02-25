t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = []

    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ans.append([1, j + 1])

    for i in range(len(b)):
        for j in range(len(b) - i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                ans.append([2, j + 1])

    for i in range(len(a)):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ans.append([3, i + 1])

    print(len(ans))

    for oper in ans:
        print(*oper)
