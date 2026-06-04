class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS
        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                stack.append(nei)

        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna