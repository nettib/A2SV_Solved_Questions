class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        curr = []
        
        def backtrack(num):
            if len(curr) == k:
                ans.append(curr.copy())
                return
            if num > n:
                return

            curr.append(num)
            backtrack(num + 1)
            curr.pop()
            backtrack(num + 1)
    
        backtrack(1)

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna