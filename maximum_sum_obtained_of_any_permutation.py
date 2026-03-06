class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # [1, 1, -1, 0, -1]
        # [1, 2, 1, 1, 0]
        # 5 * 2 + 4 + 3 + 2 = 10 + 4 + 5 = 9

        # O(nlogn)
        # O(n)   

        # [1, -1, 1, 1, 2, -4]
        # [1, 0, 1, 2, 4]   

        mark = [0] * (len(nums) + 1)  

        for start, end in requests:
            mark[start] += 1
            mark[end + 1] -= 1

        
        for i in range(1, len(mark)):
            mark[i] += mark[i - 1]
        
        mark = mark[: -1]

        mark.sort()
        nums.sort()

        res = 0
        for i in range(len(nums)):
            res += (nums[i] * mark[i])
        
        return res % (10**9 + 7)
