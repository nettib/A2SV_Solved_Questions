class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        cand = points[0][:]
        balloons = 1

        for s, e in points:

            if cand[0] <= s <= cand[1]:
                cand[0] = max(cand[0], s)
                cand[1] = min(cand[1], e)
            else:
                cand[0] = s
                cand[1] = e
                balloons += 1
            
        return balloons
