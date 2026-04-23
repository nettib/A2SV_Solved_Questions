from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for courses in prerequisites:
            c1, c2 = courses
            graph[c2].append(c1)
        
        colors = {}

        for node in range(numCourses):
            colors[node] = 'W'

        visited = set()
        cycle = False
        def dfs(node):
            nonlocal cycle
            visited.add(node)
            colors[node] = 'G'

            if cycle:
                return

            for neighbor in graph[node]:
                if colors[neighbor] == 'W':
                    dfs(neighbor)
                elif colors[neighbor] == 'G':
                    cycle = True
            colors[node] = 'B'
        
        for node in range(numCourses):
            if node not in visited:
                dfs(node)
        
        return not cycle
        

        


