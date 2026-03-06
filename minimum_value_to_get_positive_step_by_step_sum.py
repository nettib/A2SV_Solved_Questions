class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        min_startValue = 1

        for num in nums:
            if num < 0:
                min_startValue = max(abs(num) + 1, min_startValue)
        
        return min_startValue
