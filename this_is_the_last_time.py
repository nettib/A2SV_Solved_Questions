t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().split())
    casinos = []

    for _ in range(n):
        casino = list(map(int, input().split()))
        casinos.append(casino)

    casinos.sort()

    max_coin = k
    for i in range(len(casinos)):
        l, r, coin = casinos[i]
        if max_coin >= l and max_coin <= r:
            max_coin = max(max_coin, coin)

    print(max_coin)
