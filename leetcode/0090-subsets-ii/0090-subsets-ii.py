class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(subsets[:])
                return
            
            subsets.append(nums[i])
            backtrack(i + 1)
            subsets.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res