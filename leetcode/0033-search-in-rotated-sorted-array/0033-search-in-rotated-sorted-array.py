class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_pivot(nums):
            l, r = 0, len(nums) - 1

            while l < r:
                m = l + ((r - l) // 2)
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
                
            return l
        
        def bs(nums, l, r, target):

            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        pivot = get_pivot(nums)
        if nums[-1] < target:
            ans = bs(nums, 0, pivot, target)
        else:
            ans = bs(nums, pivot, len(nums) - 1, target)
        
        return ans