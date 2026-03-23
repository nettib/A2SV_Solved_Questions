from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        def helper(charge, run, budget):
            prefix_sum = [0]

            for i in range(len(run)):
                prefix_sum.append(prefix_sum[i] + run[i])
            
            q = deque()

            max_robot = 0

            l = 0
            for r in range(len(charge)):
                while q and q[-1] < charge[r]:
                    q.pop()
                
                q.append(charge[r])

                while q and (q[0] + ((r - l + 1) *  (prefix_sum[r + 1] - prefix_sum[l])) > budget):
                    if q and q[0] == charge[l]:
                        q.popleft()
                    l += 1
                
                max_robot = max(max_robot, r - l + 1)
            
            return max_robot
        
        return helper(chargeTimes, runningCosts, budget)

                        