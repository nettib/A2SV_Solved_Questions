class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        groups = [-1] * (n + 1)
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if groups[nei] == groups[node]:
                    return False
                if nei in visited:
                    continue

                groups[nei] = 1 - groups[node]

                if not dfs(nei):
                    return False

            return True

        visited = set()

        for node in range(1, n + 1):
            if node in visited:
                continue
            groups[node] = 1
            if not dfs(node):
                return False
        
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna