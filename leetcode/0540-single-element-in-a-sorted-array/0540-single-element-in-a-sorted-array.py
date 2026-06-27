class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def get_duplicate(i):
            if i <= len(nums) - 2 and nums[i + 1] == nums[i]:
                return [i, i + 1]
            elif i > 0 and nums[i - 1] == nums[i]:
                return [i - 1, i]
            else:
                return []
        

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            res = get_duplicate(m)
            if not res:
                return nums[m]
            
            if res[0] % 2:
                r = res[0] - 1
            else:
                l = res[-1] + 1
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna