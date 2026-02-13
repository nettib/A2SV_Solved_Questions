class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        markers = [1, 1]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    if r == 0:
                        markers[0] = 0
                    if c == 0:
                        markers[1] = 0
        
        
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        for r in range(1):
            for c in range(len(matrix[0])):
                if markers[0] == 0:
                    matrix[r][c] = 0
        
        for r in range(len(matrix)):
            for c in range(1):
                if markers[1] == 0:
                    matrix[r][c] = 0
        
