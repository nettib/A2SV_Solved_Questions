class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        graph = defaultdict(list)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    graph[r].append(c)
                

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei in visited:
                    continue
                dfs(nei)
        
        visited = set()
        provinces = 0
        for node in range(len(grid)):
            if grid[node][node] == 1 and node not in visited:
                dfs(node)
                provinces += 1
        
        return provinces

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna