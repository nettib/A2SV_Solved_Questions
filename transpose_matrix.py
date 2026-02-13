class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix_transposed = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for r in range(len(matrix_transposed)):
            for c in range(len(matrix_transposed[0])):
                matrix_transposed[r][c] = matrix[c][r]
        
        return matrix_transposed
