class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def get_subset(idx):
            ans.append(curr[:])
            if idx == len(nums):
                return


            for i in range(idx, len(nums)):
                curr.append(nums[i])
                get_subset(i + 1)
                curr.pop()
        
        get_subset(0)
        return ans
