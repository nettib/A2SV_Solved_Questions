t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    r = list(map(int, input().split()))

    m = int(input().strip())

    b = list(map(int, input().split()))

    def get_max(arr):
        _max = 0

        curr = 0
        for num in arr:
            curr += num
            _max = max(_max, curr)

        return _max

    print(get_max(r) + get_max(b))
