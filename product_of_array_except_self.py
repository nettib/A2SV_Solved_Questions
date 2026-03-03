class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        curr = nums[0]
        for i in range(1, len(nums)):
            res[i] *= curr
            curr *= nums[i]
        
        curr = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        
        return res
