class Solution:
    def rob(self, nums: list[int]) -> int:
        track = {}
        
        def best(i):
            if i < 0:
                return 0
            if i not in track:
                track[i] = max(best(i - 1), nums[i] + best(i - 2))

            return track[i]
        
        return best(len(nums) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna