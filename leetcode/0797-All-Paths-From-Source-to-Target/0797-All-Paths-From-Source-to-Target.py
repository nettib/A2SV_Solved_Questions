from collections import defaultdict
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        ans = []

        for node in range(len(graph)):
            adj[node] = graph[node]
        
        path = []
        def dfs(node):
            path.append(node)

            if node == len(graph) - 1:
                ans.append(path[:])
                path.pop()
                return
            
            for neighbor in adj[node]:
                dfs(neighbor)
            
            path.pop()
            
        dfs(0)

        return ans