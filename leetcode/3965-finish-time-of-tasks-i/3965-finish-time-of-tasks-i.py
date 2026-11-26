class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        tree = defaultdict(list)

        for n1, n2 in edges:
            tree[n1].append(n2)
        
        def dfs(node):
            vals = []
            for child in tree[node]:
                vals.append(dfs(child))
            
            if not vals:
                vals.append(0)
            latest = max(vals)
            earliest = min(vals)
            ownDuration = (latest - earliest) + baseTime[node]

            return latest + ownDuration
        
        return dfs(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna