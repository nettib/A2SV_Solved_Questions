class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_first(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            
            return l if l > -1 and l < len(nums) and nums[l] == target else - 1

        def get_second(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            
            return r  if r > -1 and r < len(nums) and nums[r] == target else - 1
        
        if not len(nums):
            return [-1, -1]
        s = get_first(nums, target)
        e = get_second(nums, target)
    
        return [s, e]