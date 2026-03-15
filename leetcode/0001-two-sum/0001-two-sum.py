class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i in range(len(nums)):
            if target - nums[i] in track:
                return [track[target - nums[i]], i]
        
            track[nums[i]] = i


        
