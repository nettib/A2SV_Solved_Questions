class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(node):

            for nei in graph[node]:
                if nei in visited:
                    if color[nei] != -1 and color[node] == color[nei]:
                        return False
                    continue
                
                visited.add(nei)
                color[nei] = 1 - color[node]
                if not dfs(nei):
                    return False
            
            return True
    
        visited = set()
        for node in range(len(graph)):
            if node not in visited:
                visited.add(node)
                color[node] = 0
                if not dfs(node):
                    return False
        
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna