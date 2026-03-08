class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        r, c = 0, len(grid[0]) - 1

        while r < len(grid) and c >= 0:
            if grid[r][c] < 0:
                count += (len(grid) - r)
                c -= 1
            else:
                r += 1
        
        return count
