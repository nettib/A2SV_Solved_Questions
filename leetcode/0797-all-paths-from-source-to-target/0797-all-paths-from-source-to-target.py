class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans = []

        def dfs(node, path):
            
            path.append(node)
            if node == len(graph) - 1:
                ans.append(path[:])
                path.pop()
                return 

            for nei in graph[node]:
                dfs(nei, path)
            
            path.pop()
        
        dfs(0, [])

        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna