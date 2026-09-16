class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []

        def backtrack(i, path):
            if i == len(nums):
                ans.append(path[:])
                return
            

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)

        backtrack(0, [])

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna