class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(mat, target):
            l, r = 0, len(mat) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if mat[m] == target:
                    return True
                elif mat[m] < target:
                    l = m + 1
                else:
                    r = m -1
                
            return False
        
        l, r = 0, len(matrix) - 1

        while l < r:
            m = l + ((r - l) // 2)
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                l = m
                r = m
            
        if l == r:
            return bs(matrix[l], target)
        
        return False