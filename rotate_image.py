class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mark = 0
        for r in range(len(matrix)):
            for c in range(mark, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            mark += 1
            
        for i in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]

                l += 1
                r -= 1
            

