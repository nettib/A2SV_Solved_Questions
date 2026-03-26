class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def get_subset(i):
            if i == len(nums):
                ans.append(curr[:])
                return 
            
            curr.append(nums[i])
            get_subset(i + 1)
            curr.pop()
            get_subset(i + 1)
        
        get_subset(0)
        return ans



