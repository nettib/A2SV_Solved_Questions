class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        for i, num in enumerate(nums):
            nums[i] = [num, i]
        
        ans = [0] * len(nums)
        nums.sort()
        smaller = 0

        for i in range(1, len(nums)):
            if nums[i][0] == nums[i - 1][0]:
                ans[nums[i][-1]] = smaller
            else:
                smaller = i
                ans[nums[i][-1]] = smaller
        
        return ans


            
