def bs(prev, curr, b):
        l, r = 0, len(b) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if b[m] - curr >= prev:
                r = m - 1
            else:
                l = m + 1

        return l

    def solve(n, m, a, b):

        for i in range(n):
            idx = bs(a[i - 1] if i != 0 else -float("inf"), a[i], b)
            if idx > -1 and idx < len(b):
                _max = max(b[idx] - a[i], a[i])
                _min = min(b[idx] - a[i], a[i])
            else:
                _max = a[i]
                _min = a[i]

            if i > 0 and _max < a[i - 1]:
                return "NO"

            if i == 0 or _min >= a[i - 1]:
                a[i] = _min
            else:
                a[i] = _max

        return "YES"


    print(solve(n, m, a, b))