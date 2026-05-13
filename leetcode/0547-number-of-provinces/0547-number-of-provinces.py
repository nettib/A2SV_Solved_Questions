class Solution:
    def findCircleNum(self, cities: List[List[int]]) -> int:
        adj = {}

        for r in range(len(cities)):
            for c in range(len(cities[0])):
                if cities[r][c] == 1:
                    if r not in adj: adj[r] = set()
                    if c not in adj: adj[c] = set()
                    adj[r].add(c)
                    adj[c].add(r)
        
        for node in adj:
            adj[node] = list(adj[node])

        visited = set()
        def dfs(node):

            for nei in adj[node]:
                if nei in visited: continue
                visited.add(nei)
                dfs(nei)
        
        provinces = 0
        for node in adj:
            if node in visited: continue
            dfs(node)
            provinces += 1
        
        return provinces

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna