class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        track = set()

        for l, r in ranges:
            for num in range(l, r + 1):
                track.add(num)
            
        for num in range(left, right + 1):
            if num not in track:
                return False
        
        return True
