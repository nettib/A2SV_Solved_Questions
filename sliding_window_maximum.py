from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = deque([])
        ans = []

        for i in range(k):
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            max_q.append(nums[i])

        ans.append(max_q[0])

        for i in range(k, len(nums)):
            while max_q and max_q[-1] < nums[i]:
                max_q.pop()
            max_q.append(nums[i])
        
            if max_q[0] == nums[i - k]:
                max_q.popleft()
            
            ans.append(max_q[0])
        
        return ans

