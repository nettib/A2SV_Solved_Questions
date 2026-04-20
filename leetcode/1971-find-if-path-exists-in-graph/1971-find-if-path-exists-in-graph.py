from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(curr, dest, graph, visited):
            if curr == dest:
                return True
            if curr in visited:
                return False
            visited.add(curr)

            for neighbour in graph[curr]:
                if dfs(neighbour, dest, graph, visited):
                    return True
            return False
        
        return dfs(source, destination, graph, set())        