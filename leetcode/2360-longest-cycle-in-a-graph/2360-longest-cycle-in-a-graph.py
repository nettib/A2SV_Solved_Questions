class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        degree = [0] * len(edges)

        for node in edges:
            if node == -1:
                continue
            degree[node] += 1

        q = deque([])

        for node in range(len(degree)):
            if degree[node] == 0:
                q.append(node)
        
        while q:
            node = q.popleft()

            nei = edges[node]
            if nei == -1:
                continue
            degree[nei] -= 1

            if degree[nei] == 0:
                q.append(nei)

        def dfs(node):
            nonlocal l
            l += 1
            visited.add(node)

            nei = edges[node]
            if nei not in visited:
                dfs(nei)
            
            return l

        visited = set()
        _max = 0
        for node in range(len(edges)):
            if node in visited or degree[node] == 0:
                continue
            l = 0
            dfs(node)
            _max = max(_max, l)

        return _max if _max else -1
            



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna