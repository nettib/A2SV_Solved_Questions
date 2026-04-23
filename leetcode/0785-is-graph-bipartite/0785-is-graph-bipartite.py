class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Coloring
        color = [0] * len(graph)

        visited = set()
        def dfs(node):
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if color[node] == "B":
                        color[neighbor] = "W"
                    else:
                        color[neighbor] = "B"
                    dfs(neighbor)
        
        for node in range(len(graph)):
            if color[node] == 0:
                color[node] = "B"
                dfs(node)
        
        # checking if the graph is bipartite or not
        for node in range(len(graph)):
            c = color[node]
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False
        
        return True
                



                
