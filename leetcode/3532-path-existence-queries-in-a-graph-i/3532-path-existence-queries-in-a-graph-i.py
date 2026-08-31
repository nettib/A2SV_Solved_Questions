class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n

        comp = 0

        for i in range(n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            
            component[i] = comp
        
        ans = []
        for n1, n2 in queries:
            ans.append(component[n1] == component[n2])
        
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna