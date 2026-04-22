from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(graph, curr, d, visited):
            if curr == d:
                return True
            visited.add(curr)

            for neighbor in graph[curr]:
                if neighbor not in visited:
                    if dfs(graph, neighbor, d, visited):
                        return True
                
            return False

        return dfs(graph, source, destination, set())
