class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        graph = defaultdict(list)

        for node, pnode in enumerate(parent):
            if pnode != -1:
                graph[pnode].append(node)

        height = 0
        depths = [0] * len(parent)

        def dfs(node, depth):
            nonlocal height
            depths[node] = depth
            height = max(height, depth)

            for nei in graph[node]:
                dfs(nei, depth + 1)
        
        dfs(0, 1)
        
        ans = 0
        for node in range(len(parent)):
            ans += (nums[node] * ((height - depths[node]) + 1))
        
        return ans

 
        





        

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna