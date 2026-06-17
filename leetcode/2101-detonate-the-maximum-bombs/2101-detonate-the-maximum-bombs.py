class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def check_distance(x1, y1, x2, y2, r):
            d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

            return d <= r

        graph = defaultdict(list)

        for i, [x1, y1, r1] in enumerate(bombs):
            for j, [x2, y2, r2] in enumerate(bombs):
                if i == j:
                    continue
                if check_distance(x1, y1, x2, y2, r1):
                    graph[i].append(j)

        def dfs(bomb):
            nonlocal count

            count += 1
            for nei in graph[bomb]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)

        _max = 0
        for i in range(len(bombs)):
            count = 0
            visited = set()
            visited.add(i)
            dfs(i)
            _max = max(_max, count)

        return _max

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna