class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _min = float("inf")
        
        ans = -float("inf")
        
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]

            ans = max(ans, curr, curr - _min)
            _min = min(_min, curr)
        
        return ans
