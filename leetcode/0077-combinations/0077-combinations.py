class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []


        def backtrack(num, path):
            if len(path) == k:
                ans.append(path[:])
                return
            if num > n:
                return
            

            path.append(num)
            backtrack(num + 1, path)
            path.pop()
            backtrack(num + 1, path)
        
        backtrack(1, [])

        return ans
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna