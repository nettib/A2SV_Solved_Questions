class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(num, curr):
            if len(curr) == k:
                ans.append(curr[:])
                return
            if num > n:
                return

            curr.append(num)
            backtrack(num + 1, curr)
            curr.pop()
            backtrack(num + 1, curr)
        
        backtrack(1, [])
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna