class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        _len = len(nums)

        def backtrack(nums, path):
            if len(path) == _len:
                ans.append(path[:])
                return
            

            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:], path)
                path.pop()
            
        backtrack(nums, [])

        return ans 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna