class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        perimeter = 0
        l = 0
        curr = sum(nums[: 3])

        if nums[0] + nums[1] > nums[2]:
            perimeter = max(perimeter, curr)
        
        for i in range(3, len(nums)):
            curr -= nums[i - 3]
            curr += nums[i]
            if (curr - nums[i]) > nums[i]:
                perimeter = max(perimeter, curr)
        
        return perimeter 

        
