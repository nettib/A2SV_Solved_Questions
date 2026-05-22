from collections import defaultdict, deque
t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    r = list(map(int, input().split()))

    def solve(n, r):
        graph = defaultdict(list)
        degree = [0] * (n + 1)

        for i in range(1, n + 1):
            graph[i].append(r[i - 1])
            degree[r[i - 1]] += 1

        q = deque()

        for i in range(1, n + 1):
            if degree[i] == 0:
                q.append(i)
        t = 0
        while q:
            for _ in range(len(q)):
                spider = q.popleft()

                for nei in graph[spider]:
                    degree[nei] -= 1
                    if degree[nei] == 0: q.append(nei)

            t += 1

        return t + 2

    print(solve(n, r))