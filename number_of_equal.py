n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def get_equal_pairs(a, b):
    ap = 0
    bp = 0
    count = 0

    while ap < len(a) and bp < len(b):
        if a[ap] < b[bp]:
            ap += 1
        elif a[ap] > b[bp]:
            bp += 1
        else:
            val = a[ap]
            ca = 0
            cb = 0

            while ap < len(a) and a[ap] == val:
                ca += 1
                ap += 1

            while bp < len(b) and b[bp] == val:
                cb += 1
                bp += 1

            count += (ca * cb)

    return count

print(get_equal_pairs(a, b))
