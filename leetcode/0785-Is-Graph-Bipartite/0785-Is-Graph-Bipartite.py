from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)
        
        visited = set()
        
        def dfs(node):

            for nei in graph[node]:
                if nei in visited: 
                    if colors[node] == colors[nei]: return False
                    continue
                visited.add(nei)
                if colors[node] == 'B':
                    colors[nei] = 'W'
                else:
                    colors[nei] = 'B'
                if not dfs(nei):
                    return False
            return True
        
        for node in range(len(graph)):
            if node in visited: continue
            visited.add(node)
            colors[node] = 'B'
            if not dfs(node): return False
        
        return True