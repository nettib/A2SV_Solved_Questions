class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        mark = len(nums)
        def backtrack(nums):
            if len(path) == mark:
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:])
                path.pop()

        backtrack(nums)
        
        return ans
            
            
