class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacement = 0

        last = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i]
            if curr <= last:
                last = curr
            
            else:
                k = math.ceil(curr / last)
                replacement += (k - 1)
                last = curr // k
            
        return replacement
            

