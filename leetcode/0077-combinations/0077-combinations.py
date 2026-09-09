class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(num, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            

            for num2 in range(num, n + 1):
                path.append(num2)
                backtrack(num2 + 1, path)
                path.pop()
        
        backtrack(1, [])
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna