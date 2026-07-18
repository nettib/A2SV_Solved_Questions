class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for node in range(len(parent)):
            graph[parent[node]].append(node)
        
        ans = 0
        def dfs(node):
            nonlocal ans
            longest = second_longest = 0

            for nei in graph[node]:
                length = dfs(nei)

                if s[node] != s[nei]:
                    if length > longest:
                        second_longest = longest
                        longest = length
                    elif length > second_longest:
                        second_longest = length
                    
            ans = max(ans, longest + second_longest + 1)

            return longest + 1
        
        dfs(0)

        return ans




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna