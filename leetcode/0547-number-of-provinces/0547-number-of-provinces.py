class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if r == c:
                    continue
                if isConnected[r][c]:
                    graph[r].append(c)
        
        visited = set()
        def dfs(node):

            for nei in graph[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                dfs(nei)
        
        provinces = 0
        for node in range(len(isConnected)):
            if node in visited:
                continue
            visited.add(node)
            dfs(node)
            provinces += 1
        
        return provinces
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna