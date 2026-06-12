class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            graph[a].append((b, v))
            graph[b].append((a, (1 / v)))

        def dfs(a, b, res):
            if a not in graph or b not in graph:
                return float(-1)
            if a == b:
                return float(res)

            for nei, nei_w in graph[a]:
                if nei in visited:
                    continue

                visited.add(nei)
                result = dfs(nei, b, res * nei_w)
                if int(result) != -1:
                    return float(result)

            return -1

        ans = []
        for a, b in queries:
            visited = {a}
            ans.append(dfs(a, b, 1))

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna