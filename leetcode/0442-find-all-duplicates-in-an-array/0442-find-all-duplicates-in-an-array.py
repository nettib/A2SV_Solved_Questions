class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while i != nums[i] - 1:
                if nums[i] < 0:
                    break

                pos = nums[i] - 1

                if nums[pos] - 1 == pos:
                    res.append(nums[i])
                    nums[i] = -(nums[i])
                    break 
                    
                nums[i], nums[pos] = nums[pos], nums[i]
        
        return res

        