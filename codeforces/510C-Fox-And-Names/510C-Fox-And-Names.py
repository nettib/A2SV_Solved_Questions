from collections import defaultdict, deque

n = int(input().strip())

authors = []
for _ in range(n):
    author = input().strip()
    authors.append(author)


def solve(n, authors):
    graph = defaultdict(list)
    degree = {}
    vals = set()

    for i in range(1, n):
        pre = authors[i - 1]
        suf = authors[i]

        l = min(len(pre), len(suf))

        mark = 0
        for j in range(l):
            if pre[j] != suf[j]:
                vals.add(pre[j])
                vals.add(suf[j])
                graph[pre[j]].append(suf[j])
                if suf[j] not in degree: degree[suf[j]] = 0
                degree[suf[j]] += 1
                mark = 1
                break

        if not mark and len(suf) < len(pre):
            return 0

    if not vals:
        return 1

    q = deque()
    res = []

    for char in vals:
        if char not in degree:
            degree[char] = 0
        if not degree[char]: q.append(char)

    while q:
        char = q.popleft()
        res.append(char)

        for nei in graph[char]:
            degree[nei] -= 1
            if not degree[nei]: q.append(nei)


    if len(res) != len(degree.keys()):
        return 0

    return res

ans = solve(n, authors)

if ans == 1:
    print("abcdefghijklmnopqrstuvwxyz")
elif not ans: print("Impossible")
else:
    res = []
    track = set(ans)

    for char in "abcdefghijklmnopqrstuvwxyz":
        if char in track: continue
        res.append(char)

    res.extend(ans)
    print("".join(res))